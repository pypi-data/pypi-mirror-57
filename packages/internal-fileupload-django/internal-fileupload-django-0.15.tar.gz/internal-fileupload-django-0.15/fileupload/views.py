from django.http import JsonResponse, Http404
from uuid import uuid4
from datetime import datetime, timedelta
from google.cloud import storage
from os import path
from django.views.decorators.csrf import csrf_exempt
import json
from .models import fileupload
from django.conf import settings

bucketname = settings.GOOGLE_BUCKET


def connect():
    return storage.Client()


@csrf_exempt
def generateKey(request):
    if (request.method) == 'POST':

        baseDir = 'cloud/'

        # Generate the Unique ID for the folder
        uu = str(uuid4())
        # Setup the settings
        # https://docs.djangoproject.com/en/2.1/ref/files/uploads#django.core.files.uploadedfile.UploadedFile

        if (request.content_type == "application/json"):
            jsonRequest = json.loads(request.body.decode('utf-8'))
            fileName = jsonRequest['fileName']
            contentType = jsonRequest['contentType']
        else:
            fileName = request.POST.get('fileName')
            contentType = request.POST.get('contentType')

        expiration = datetime.now() + timedelta(hours=1)

        # the finalPath needs to be saved in a DB
        finalBlobPath = path.join(baseDir, uu, fileName)

        storage_client = connect()
        bucket = storage_client.bucket(bucketname)
        blob = bucket.blob(finalBlobPath)

        try:
            signed_url = blob.generate_signed_url(
                expiration=expiration,
                method="PUT",
                client=storage_client,
                version="v4"
            )
        except Exception:
            return JsonResponse({'error': True,

                                 'message': 'Error getting signed URL'})
        else:
            hash = str(uuid4())
            db = fileupload(file=finalBlobPath,
                            fileType=contentType,
                            location="GCL",
                            hash=hash,
                            status="OK"
                            )
            db.save()

            return JsonResponse({'success': True,
                                 'id': db.id,
                                 'uuid': hash,
                                 'filePath': finalBlobPath,
                                 'expiration': expiration,
                                 'signed_url': signed_url})
    else:
        return Http404('Method not allowed')


def deleteURL(request):
    try:
        signed_url, expiration = GenerateDeleteURL(request.GET.get('hash', False))
    except Exception:
        return JsonResponse({'error': True,
                             'message': 'Error getting delete signed URL'}
                            , status=500)
    else:
        return JsonResponse({'success': True,
                             'expiration': expiration,
                             'signed_url': signed_url})


# todo refactor function to allow any kind of commands
def GenerateDeleteURL(hash):
    data = fileupload.objects.get(hash=hash)
    if (data.file):
        storage_client = connect()
        bucket = storage_client.bucket(bucketname)
        blob = bucket.blob(data.file)
        expiration = datetime.now() + timedelta(minutes=10)

        try:
            signed_url = blob.generate_signed_url(
                expiration=expiration,
                method="DELETE",
                client=storage_client,
                version="v4"
            )
        except Exception as e:
            raise e
        else:
            return [signed_url, expiration]


def viewURL(request):
    data = fileupload.objects.get(hash=request.GET.get('hash', False))
    if (data.file):
        storage_client = connect()
        bucket = storage_client.bucket(bucketname)
        blob = bucket.blob(data.file)
        expiration = datetime.now() + timedelta(hours=2)

        try:
            signed_url = blob.generate_signed_url(
                expiration=expiration,
                method="GET",
                client=storage_client,
                version="v4"
            )
        except:
            return JsonResponse({
                'error': True,
                'message': 'Something went wrong when getting the URL'
            }, status=500)
        else:
            return JsonResponse({
                'success': True,
                'expiration': expiration,
                'signed_url': signed_url
            })


def markAsDelete(request):
    try:
        hash = str(request.GET.get('hash'))
        entry = fileupload.objects.get(hash=hash).delete()
    except Exception:
        return JsonResponse({'status': 'error', 'message': 'Cannot delete the file'}, status=500)
    else:
        return JsonResponse({'status': 'ok', 'message': 'Item deleted'})

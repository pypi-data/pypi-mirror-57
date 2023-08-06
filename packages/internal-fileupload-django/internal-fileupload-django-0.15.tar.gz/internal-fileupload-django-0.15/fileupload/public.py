from django.shortcuts import redirect
from django.test.client import Client
from django.http import Http404, HttpRequest, QueryDict, HttpResponse
import requests, json
from . import views


def viewFile(request):
    hash = request.GET.get('hash', False)
    if (hash != False):

        req = HttpRequest()
        req.GET = QueryDict("hash=" + hash, mutable=False)
        jsonResponse = views.viewURL(req)
        jsonData = json.loads(jsonResponse.content)

        if (jsonResponse.status_code == 200):
            return redirect(jsonData['signed_url'])
        else:
            raise Http404('Error cannot get url')
    else:
        raise Http404('Cannot find the file')


def deleteFile(request):
    hash = request.GET.get('hash', False)
    if (hash != False):
        req = HttpRequest()
        req.GET = QueryDict("hash=" + hash, mutable=False)
        jsonResponse = views.deleteURL(req)
        jsonData = json.loads(jsonResponse.content)
        if (jsonResponse.status_code == 200):
            DeleteResponse = requests.request("DELETE", jsonData['signed_url'])
            return HttpResponse('<p>File deleted</p>')
        else:
            raise Http404('Error cannot get the url')
    else:
        raise Http404('Cannot find the file')

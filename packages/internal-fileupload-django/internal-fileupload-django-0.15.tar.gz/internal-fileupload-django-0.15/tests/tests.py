from datetime import datetime, timedelta
from os import path
from uuid import uuid4

import google
import requests
from django.conf import settings
from django.test import TestCase, Client
from google.cloud import storage


# Create your tests here.
class upload(TestCase):

    FILE = ""
    IMAGE = ""
    DIRNAME = path.dirname(path.dirname(path.abspath(__file__)))

    @classmethod
    def setUpClass(cls):
        super(upload, cls).setUpClass()
        cls.FILE = path.join(cls.DIRNAME, 'tests', 'testfile', 'kier.txt')
        cls.IMAGE = path.join(cls.DIRNAME, 'tests', 'testfile', 'image.jpg')
        cls.storage_client = storage.Client()

    def test_gcloud(self):
        # Instantiates a clientuck
        # @todo setup better and new bucket names
        bucketname = settings.GOOGLE_BUCKET

        if (type(self.storage_client._credentials) is not google.oauth2.service_account.Credentials):
            print('error')

        # setup only 30min
        expiration = datetime.now() + timedelta(minutes=30)

        # setup a UUID
        uu = str(uuid4())

        uploaded_file = uu + '/kier.txt'

        # connect to a bucket
        test_bucket = self.storage_client.bucket(bucketname)
        blob = test_bucket.blob(uploaded_file)

        signed_url = blob.generate_signed_url(
            expiration=expiration,
            method="PUT",
            client=self.storage_client,
            version="v4"
        )

        with open(self.FILE, 'rb') as data:
            mdata = data.read()
            response = requests.put(signed_url, data=mdata)

        self.assertEqual(response.status_code, 200)

        delete_url = blob.generate_signed_url(
            expiration=expiration,
            method="DELETE",
            client=self.storage_client,
            version="v4"

        )

        DeleteResponse = requests.request("DELETE", delete_url)

        self.assertEqual(DeleteResponse.status_code, 204)

    def test_create(self):
        c = Client()

        response = c.post('/fileupload/generate/',
                          data={
                              "fileName": "test.jpeg",
                              "contentType": "image/jpeg"
                          }

                          )
        self.assertEqual(response.json()['success'], True)
        self.assertEqual(response.status_code, 200)
        with open(self.IMAGE, 'rb') as data:
            mdata = data.read()
            uploadResponse = requests.put(response.json()['signed_url'], data=mdata)
        self.assertEqual(uploadResponse.status_code, 200)
        uuid_ = response.json()['uuid']
        self.checkFiles(uuid_)
        self.deletefile(uuid_)

    # this is getting the signed url to delete the file when Delete is called
    def deletefile(self, hash):
        c = Client()

        response = c.get('/fileupload/deleteHash/', data={
            'hash': hash
        })

        self.assertEqual(response.status_code, 200)
        DeleteResponse = requests.request("DELETE", response.json()['signed_url'])

        res = c.get('/fileupload/markDeleted/',data={
            'hash':hash
        })
        self.assertEqual(res.status_code,200)

        self.assertEqual(DeleteResponse.status_code, 204)

    def checkFiles(self, hash):
        # here we'll have to test getting an image that we've uploaded.

        c = Client()
        response = c.get('/fileupload/getfile/', data={
            'hash': hash
        })

        # check if the link came back
        self.assertEqual(response.status_code, 200)

        # now that we've checked that we've got a valid link. Let's do a request to the image
        fileResponse = requests.get(response.json()['signed_url'])

        self.assertEqual(fileResponse.headers.get('Content-Type'), "application/octet-stream")

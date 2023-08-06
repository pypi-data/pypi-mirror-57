=====
Icelabz File Upload
=====

This is a basic file upload using Google Docs

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'fileupload',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('fileupload/', include('fileupload.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Use the following link http://127.0.0.1:8000/fileupload/ to upload



## To build the package you need to run

```
python setup.py sdist
```

## Building

For some reason we cannot test this on circleCI so we have to manually run the test

the build instruction goes like this after updatin the setup.py verions

```shell script
python runtest.py
python setup.py sdist
```


# TODO
```text
- @todo: make sure we add a google credential setup guide
- @TODO: Add a cron job that can be checked for expiry
```

from django.urls import include, path

urlpatterns = [
    path('fileupload/', include('fileupload.urls'))
]

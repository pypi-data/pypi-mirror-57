from . import views, public
from django.urls import path

# urls for fileuplaod

urlpatterns = [
    path('generate/', views.generateKey),
    path('deleteHash/', views.deleteURL),
    path('getfile/', views.viewURL),
    path('markDeleted/', views.markAsDelete),
    path('justGetFile/', public.viewFile, name="fileupload.getfile"),
    path('justDelete/', public.deleteFile)
]

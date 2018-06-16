"""face_cluster URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin

from . import controller
from . import controller_image
from . import feedback

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search_img', controller.recognise),
    url(r'^load_img', controller_image.download_img),
    url(r'^image_splite', controller.imagesplite),
    url(r'^image_feedback',controller.image_feedback),
    url(r'^image_vector',feedback.feedback),
    url(r'^', controller.home),    
    
]

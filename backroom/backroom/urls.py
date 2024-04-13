"""
URL configuration for backroom project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include,re_path
from tea.views import PrepodViewSet, StudViewSet, TeoriaViewSet, FaaViewSet, PrepodList, StudList
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register(r'Prepod', PrepodViewSet)
router.register(r'Stud', StudViewSet)
router.register(r'Teoria', TeoriaViewSet)
router.register(r'Faa', FaaViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path('api/Prepod(?P<name>.+)/$',PrepodList.as_view()),
    re_path('api/Stud(?P<name>.+)/$',StudList.as_view()),
]
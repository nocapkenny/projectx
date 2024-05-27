# -*- coding: windows-1251 -*-
from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework import routers
from tea.views import OsenViewSet,TeoriaViewSet, FaaViewSet, GroupViewSet,UserViewSet
from tea.views import GroupList, FaaList, TeoriaList, FileDownloadView,register_user, user_login, user_logout,UserList

router = routers.DefaultRouter()
router.register(r'Osenki', OsenViewSet)
router.register(r'User', UserViewSet)
router.register(r'Teoria', TeoriaViewSet)
router.register(r'Faa', FaaViewSet)
router.register(r'Gro',GroupViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    # path('api/auth/',include('rest_framework.urls')),
    re_path('api/User(?P<name>.+)/$', UserList.as_view()),
    re_path('api/User(?P<group>.+)/$', UserList.as_view()),
    re_path('api/Teoria(?P<predmet>.+)/$', TeoriaList.as_view()),
    re_path('api/Faa(?P<name>.+)/$', FaaList.as_view()),
    re_path('api/Gro(?P<faculty>.+)/$', GroupList.as_view()),
    path('files/<int:id>/dw/', FileDownloadView.as_view(), name='file-download'),
    path('api/register/', register_user, name='register'),
    path('api/login/', user_login, name='login'),
    path('api/logout/', user_logout, name='logout'),
]

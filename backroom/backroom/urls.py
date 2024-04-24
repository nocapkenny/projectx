from django.contrib import admin
from django.urls import path,include,re_path
from tea.views import PrepodViewSet, StudViewSet, TeoriaViewSet, FaaViewSet, PrepodList, StudList,TeoriaList
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register(r'Prepod', PrepodViewSet)
router.register(r'Stud', StudViewSet)
router.register(r'Teoria', TeoriaViewSet)
router.register(r'Faa', FaaViewSet)

urlpatterns = [
    # path('files/<str:tema>', DownloadFileFromDBView.as_view(), name='download_file_from_db'),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path('api/Prepod(?P<name>.+)/$',PrepodList.as_view()),
    re_path('api/Stud(?P<name>.+)/$',StudList.as_view()),
   re_path('api/Teoria(?P<predmet>.+)/$',TeoriaList.as_view()),
]

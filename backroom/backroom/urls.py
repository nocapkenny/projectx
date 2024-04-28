from django.contrib import admin
from django.urls import path,include,re_path
from tea.views import PrepodViewSet, StudViewSet, TeoriaViewSet, FaaViewSet, PrepodList, StudList,TeoriaList,FileDownloadView,FileDownload1View
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register(r'Prepod', PrepodViewSet)
router.register(r'Stud', StudViewSet)
router.register(r'Teoria', TeoriaViewSet)
router.register(r'Faa', FaaViewSet)
# router.register(r'files', FileViewSet)
urlpatterns = [
    path('files/<str:filename>/', FileDownload1View.as_view()),
    path('files/<int:pk>/dw/', FileDownloadView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    re_path('api/Prepod(?P<name>.+)/$',PrepodList.as_view()),
    re_path('api/Stud(?P<name>.+)/$',StudList.as_view()),
   re_path('api/Teoria(?P<predmet>.+)/$',TeoriaList.as_view()),
]

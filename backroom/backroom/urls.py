from django.contrib import admin
from django.urls import path,include,re_path
from tea.views import PrepodViewSet, StudViewSet, TeoriaViewSet, FaaViewSet, PrepodList, StudList,TeoriaList,FileDownloadView,GroupViewSet
from rest_framework import routers
 
router = routers.DefaultRouter()
router.register(r'Prepod', PrepodViewSet)
router.register(r'Stud', StudViewSet)
router.register(r'Teoria', TeoriaViewSet)
router.register(r'Faa', FaaViewSet)
router.register(r'Gro',GroupViewSet)

urlpatterns = [
    
    path('files/<int:pk>/dw/', FileDownloadView.as_view()),
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/auth/',include('rest_framework.urls')),
    re_path('api/Prepod(?P<name>.+)/$',PrepodList.as_view()),
    re_path('api/Stud(?P<name>.+)/$',StudList.as_view()),
   re_path('api/Teoria(?P<predmet>.+)/$',TeoriaList.as_view()),
]

from django.contrib import admin
from django.urls import path,include,re_path
from tea.views import PrepodViewSet, StudViewSet, TeoriaViewSet, FaaViewSet, PrepodList
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
]

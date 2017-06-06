from rest_framework import routers
from apps.hear import views 


router = routers.DefaultRouter()

router.register(r'^', router.get_api_root_view(), 'API_root')
router.register(r'v1/hear', views.HearAPIView, 'hear')

urlpatterns = router.urls

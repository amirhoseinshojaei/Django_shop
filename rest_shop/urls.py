from rest_framework.routers import SimpleRouter
from . import views


app_name = 'rest_shop'

router = SimpleRouter()
router.register('category',views.CategoryViewSet,basename='category')
urlpatterns = router.urls

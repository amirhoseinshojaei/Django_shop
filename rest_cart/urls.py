from rest_framework.routers import SimpleRouter
from . import views


app_name = 'rest_cart'

router = SimpleRouter()

router.register('cart',views.CartViewset,basename='cart')

urlpatterns = router.urls
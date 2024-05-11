from rest_framework.routers import SimpleRouter
from . import views

app_name = 'rest_order'

router = SimpleRouter()

router.register('orders',views.OrderViewset,basename='orders')
router.register('paid/orders',views.OrderPaidViewset,basename='paid_orders')
router.register('orders/items',views.OrderItemViewset,basename='order_item')


urlpatterns = router.urls
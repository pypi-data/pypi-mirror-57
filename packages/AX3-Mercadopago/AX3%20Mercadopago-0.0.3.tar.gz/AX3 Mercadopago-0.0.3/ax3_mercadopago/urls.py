from django.urls import path

from . import views


app_name = 'mercadopago'
urlpatterns = [
    path(
        'puntos-de-venta/',
        views.MercadopagoNotificationView.as_view(),
        name='notification',
    ),
]

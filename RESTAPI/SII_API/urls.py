from SII_API import views
from django.urls import path



urlpatterns = [
    path('sensors/', views.sensors),
    path('sensor/<int:id>', views.sensors_id),
    path('alerts/', views.alerts),
    path('sensor/id/alerts/<int:id>', views.sensors_id_alerts),
    path('login/', views.login),
    path('auth/', views.authenticate),
]
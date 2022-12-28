from django.urls import path
from . import views

urlpatterns = [
    path('post_br_data/', views.battery_report_data),
    path('get_br_data/', views.battery_report_data_all),
    path('get_br_data/<uid>', views.battery_report_data_user),
    # path('get_br_data/<uid>/lts', views.battery_report_data_user_lts),
    path('get_br_data/<uid>/power', views.battery_report_data_user_power),
]

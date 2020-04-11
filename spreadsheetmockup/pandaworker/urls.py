from django.urls import path
from . import views

urlpatterns = [
    path('', views.landing, name='home'),
    path('report/<pk>', views.report_detail, name='detail'),
    path('Create_template/', views.create_file_template, name='create'),
    path('Update_template/<pk>', views.update_file_template, name='update'),
    path('Submit_Report/<pk>', views.submit_live_report, name='submit')
]
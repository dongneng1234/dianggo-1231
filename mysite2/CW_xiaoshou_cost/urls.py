from django.urls import path
from . import views

urlpatterns = [
    path('test_upload', views.test_upload),
    path('test_csv', views.test_csv),
    # path('make_page_csv', views.make_page_csv),
    path('all_cost',views.all_cost),
    path('upload_view',views.upload_view),

]
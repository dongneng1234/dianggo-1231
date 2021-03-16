from django.urls import path
from . import views

urlpatterns = [
    path('test_upload', views.test_upload),
    path('test_csv', views.test_csv),
    # path('make_page_csv', views.make_page_csv),
    path('page_1',views.page_1),

]
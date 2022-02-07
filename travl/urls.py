from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('facilities/', views.FacilityList.as_view(), name='facility_list'),
    path('facilities/<int:pk>', views.FacilityDetail.as_view(),
         name='facility_detail'),
    path('locations/', views.LocationList.as_view(), name='location_list'),
    path('locations/<int:pk>', views.LocationDetail.as_view(),
         name='location_detail'),
    path('users/<int:pk>', views.UserList.as_view(), name='user_list'),
    path('users/<int:pk>', views.UserDetail.as_view(), name='user_detail'),

]

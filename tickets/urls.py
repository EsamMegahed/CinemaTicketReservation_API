from django.urls import path
from. import views


urlpatterns = [
    # [1] - Without Rest and no model query FBV
    path('django/jsonResbonseNoModel/',views.no_rest_no_model),
    # [2] - model data default django without rest
    path('django/jsonResbonseFromModel/',views.no_rest_from_model),
    # [3] - Function Based View
    path('django/fbv-list/',views.FBV_List),
   
]

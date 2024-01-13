from django.urls import path
from. import views


urlpatterns = [
    # ---- Strat Function Based Views ----

    # [1] - Without Rest and no model query FBV
    path('django/jsonResbonseNoModel/',views.no_rest_no_model),
    # [2] - model data default django without rest
    path('django/jsonResbonseFromModel/',views.no_rest_from_model),
    # [3.1] - Function Based View
    path('django/fbv-list/',views.FBV_List),
    # [3.2] - Function Based View
    path('django/fbv-list/<int:pk>',views.FBV_pk),

    # ---- End Function Based Views ----

    # ---- Strat Class Based Views ----

    
    # ---- End Class Based Views ----
]

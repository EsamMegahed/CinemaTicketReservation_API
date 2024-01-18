from django.urls import path,include
from. import views
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

router = DefaultRouter()

router.register('guests',views.ViewsetsGuest)
router.register('movie',views.ViewsetsMovie)
router.register('reservation',views.ViewsetsReservation)

urlpatterns = [
    # ---- Strat Function Based Views ----

    # [1] - Without Rest and no model query FBV
    path('django/jsonResbonseNoModel/',views.no_rest_no_model),
    # [2] - model data default django without rest
    path('django/jsonResbonseFromModel/',views.no_rest_from_model),
    # [3.1] - Function Based View GET POST
    path('django/fbv-list/',views.FBV_List),
    # [3.2] - Function Based View GET PUT DELETE
    path('django/fbv-list/<int:pk>',views.FBV_pk),

    # ---- End Function Based Views ----

    # ---- Strat Class Based Views ----
    # [4.1] - Class Based View GET POST
    path('django/CBV_List/',views.CBV_List.as_view()),
    # [4.1] - Class Based View GET PUT DELETE
    path('django/CBV_List/<int:pk>',views.CBV_pk.as_view()),

    # ---- End Class Based Views ----


    # ---- Strat Mixins Views ----
    # [5.1] - Mixins View GET POST
    path('django/Mixins/',views.Mixinslist.as_view()),
    # [5.1] - Mixins View GET PUT DELETE
    path('django/Mixins/<int:pk>',views.MixinsPk.as_view()),

    # ---- End Mixins Views ----

    # ---- Strat Generices Views ----
    # [6.1] - Generices View GET POST
    path('django/Generics/',views.GenericsList.as_view()),
    # [6.2] - Generices View GET PUT DELETE
    path('django/Generics/<int:pk>',views.GenericsPk.as_view()),

    # ---- End Generices Views ----

    # ---- Strat Viewsets Views ----
    # [7] - Viewsets View GET POST
    path('django/Viewsets/',include(router.urls)),
    
    # ---- End Viewsets Views ----

    # [8] - find movie
    path('fbv/find-movie/',views.find_movie),
    
    # [9] - New Reservation
    path('fbv/new_reservation/',views.new_reservation),
    
    # [10] - Api Log In or Log OUT
    path('api-auth',include('rest_framework.urls')),

    # [11] - Token Authentication
    path('api-token-auth/',obtain_auth_token),

    # [11] - Post Pk    
    #path('post/Generics/',views.PostList.as_view()),
    path('post/Generics/<int:pk>',views.PostPk.as_view()),


]

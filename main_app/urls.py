from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView


urlpatterns = [
    # not sure we need this once we have eras/dest up and running 
    path('', views.home, name='home'),

    # ------Itineraries (/itins/)-----------------------------  
    path('itins/', views.itins_index, name='itins_index'),
    path('itins/<int:itin_id>/', views.itins_detail, name='itins_detail'),
    path('itins/create/', views.ItinCreate.as_view(), name='itins_create'),
    path('itins/<int:pk>/update/', views.ItinUpdate.as_view(), name='itins_update'),
    path('itins/<int:pk>/delete/', views.ItinDelete.as_view(), name='itins_delete'),

    # ------Stops (/itins/)-----------------------------  
    # path('itins/<int:itinerary_id>/addstop/', views.add_stop, name='add_stop'),
    # amended add stop with new path 
    path('eras/<int:era_id>/destination/<int:dest_id>/addstop/', views.add_stop, name='add_stop'),
    # ------Delete Stops (/itins/)-----------------------------  
    path('itins/<int:itin_id>/<int:stop_id>/delete/', views.delete_stop, name='delete_stop'),

    #---------path to head directly to the admin site-------------
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),

    #----------- user sign up (/accounts)--------------
    path('accounts/signup/', views.signup, name='signup'),

    # ------Destinations (/dests/)--------- 
    # AB - index page for destinations (aka detail page for an era)
    path('eras/<int:era_id>/', views.destinations_index, name='dest_index'),
    # AB - details page for destination
    path('eras/<int:era_id>/destination/<int:dest_id>', views.destinations_detail, name="dest_detail")
    

]


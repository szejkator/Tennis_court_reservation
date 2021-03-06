from django.contrib import admin
from django.urls import path
from . import views


app_name = 'reservations_urls'

urlpatterns = [
    path('admin/', admin.site.urls),

    path('courts/', views.CourtsListView.as_view(), name='courts'),

    path('courts-details/', views.CourtsListDetailView.as_view(), name='courts-details'),

    path(
        'reserved-courts-list-view/',
        views.ReservedCourtsListView.as_view(),
        name='reserved_courts_list_views'),

    path(
        'reserved-courts-details-view/',
        views.ReservedCourtsDetailsView.as_view(),
        name='reserved_courts_details_views'),


    path('index/', views.IndexListView.as_view(), name='index-list-view'),

    path('reservations/', views.ReservationSystemListView.as_view(), name='reservations'),

    path('login/', views.Login.as_view(), name='login_main'),

    path('logout/', views.Logout.as_view(), name='logout'),

    path('admin-panel/', views.AdminPanel.as_view(), name='admin-panel'),

    path('reservation-form/', views.CreateReservationFormView.as_view(), name='reservation-form'),

    path('add-court/', views.AddCourtFormView.as_view(), name='add-court'),

    # path('date-form/', views.get_name, name='date-form')

]

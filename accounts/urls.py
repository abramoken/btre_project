from django.urls import path

from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),

    path('dashboard', views.dashboard, name='dashboard'),
    path('inquiries-list', views.inquiryList, name='inquiries-list'),
    path('delete-inquiry/<str:inquiry_id>/', views.deleteInquiry, name='delete-inquiry'),

    path('create-realtor', views.createRealtor, name='create-realtor'),
    path('realtors-list', views.realtorsList, name='realtors-list'),
    path('edit-realtor/<str:realtor_id>/', views.realtorEdit, name='edit-realtor'),
    path('delete-realtor/<str:id>/', views.deleteRealtor, name='delete-realtor'),

    path('list_listings', views.listingsList, name='list_listings'),
    path('create-listing', views.createListing, name='create-listing'),
    path('edit-listing/<str:listing_id>/', views.listingEdit, name='edit-listing'),
    path('delete-listing/<str:listing_id>', views.deleteListing, name='delete-listing'),

    path('users-list', views.usersList, name='users-list'),
    path('edit-user/<int:user_id>/', views.userEdit, name='edit-user'),
    path('delete-user/<str:id>/', views.deleteUser, name='delete-user'),

    path('admin-delete-inquiry/<str:admin_inquiry_id>/', views.adminDeleteInquiry, name='admin-delete-inquiry'),

    path('profile', views.profile, name='profile')
]

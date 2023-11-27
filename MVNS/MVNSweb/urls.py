from django.urls import path
from . import views

urlpatterns = [
    # path('', views.index, name='MVNS-index'),
    path('view/', views.view, name='MVNS-view'),
    path('add/', views.add_data, name='MVNS-add-data'),
    path('edit/<int:pk>/', views.edit_data, name='MVNS-edit-data'),
    path('delete/<int:pk>', views.delete_data, name='MVNS-delete-data'),
    path('', views.loginUser, name='MVNS-login'),
    path('logout/', views.logoutUser, name='MVNS-logout'),
    path('register/', views.register, name='MVNS-register'),
    path('profile/', views.profile, name='MVNS-profile'),
    path('changepass/', views.changepass.as_view(template_name = 'MVNSweb/mvns_changepass.html'), name='MVNS-changepass'),
    path('password_change_success/', views.password_change_success, name='MVNS-password-change-success'),
    path('user_list/', views.user_list, name='MVNS-user-list'),
    path('user_list_profile/<int:pk>', views.user_list_profile, name='MVNS-user-list-profile'),
    path('reset_password/<int:pk>', views.reset_password, name='MVNS-reset-password'),
    path('delete_user/<int:pk>', views.delete_user, name='MVNS-delete-user'),
]
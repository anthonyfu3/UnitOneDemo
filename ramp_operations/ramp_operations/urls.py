from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import path
from fuel_notes import views


urlpatterns = [
    path("admin/", admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('user_redirect/', views.user_redirect, name='user_redirect'),
    path('admin_ui/', views.admin_ui, name='admin_ui'),
    path('admin_ui/', views.admin_ui, name='admin_ui'),
    path('unit_one_ui/', views.unit_one_ui, name='unit_one_ui'),
    path('fueler_ui/', views.fueler_ui, name='fueler_ui'),
    path('overview_ui/', views.overview_ui, name='overview_ui'),
    path('unit_one_notes/', views.unit_one_notes, name='unit_one_notes'),
]

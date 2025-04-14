"""
URL configuration for Inventory_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


from django.contrib import admin
from django.urls import path

from dashboard import views
from user import views as user_view

from django.contrib.auth import views as auth_views

from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('dashboard', views.index, name='index'),
    path('staff', views.staff, name='staff'),
    path('staff/datails/<int:pk>', views.staff_details, name='staff_details'),
    path('product', views.product, name='product'),
    path('product/delete/<int:pk>', views.product_delete, name='product_delete'),
    path('product/update/<int:pk>', views.product_update, name='product_update'),
    path('order', views.order, name='order'),

    path('admin/', admin.site.urls),
    path('register', user_view.register, name='user_register'),
    path('profile', user_view.profile, name='user_profile'),
    path('profile/update', user_view.profile_update, name='user_profile_updates'),
    path('', auth_views.LoginView.as_view(template_name='user/login.html'), name='user_login'),
    path('logout', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='user_logout'),
    # path('password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    # path('password_reset/done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    # path('password_reset_confirm<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    # path('password_reset_complete', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),



]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

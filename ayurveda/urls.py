"""
URL configuration for ayurveda project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
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
from ayurvedic_app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #path('admin/', admin.site.urls),
    path('', views.indexpage, name = "indexpage"),
    path('aboutpage/', views.aboutpage, name = "aboutpage"),
    path('remediespage/', views.remediespage, name = "remediespage"),
    path('blogpage/', views.blogpage, name = "blogpage"),
    path('contactpage/', views.contactpage, name = "contactpage"),
    path('loginpage/', views.loginpage, name = "loginpage"),
    path('login/', views.login, name = "login"),
    path('registration/', views.resgistration, name = "resgistration"),
    path('registrationpage/', views.registrationpage, name = "registrationpage"),
    path('mydashboard/', views.mydashboardpage, name = "mydashboardpage"),
    path('updateinfo_code/',views.updateinfo_code,name="updateinfo_code"),
    path('updatepage/', views.updatepage, name = "updatepage"),
    path('logout/', views.logout_view, name = "logout_view"),
    path('admin/', views.adminloginpage, name = "adminloginpage"),
    path('adminlogin/', views.adminlogin, name = "adminlogin"),
    path('adminpage/', views.admindashboardpage, name = "admindashboardpage"),
    path('adminlogout/', views.logout_admin, name = "logout_admin"),
    path('searchusers/', views.search_users, name = "search_users"),
    path('adminremedies/', views.admin_remedies, name = "admin_remedies"),
    #path('remedylist/', views.remedieslist, name ="remedieslist"),
    path('adminupload/', views.admin_upload, name = "admin_upload"),
    path('useremediespage/', views.useremediespage, name = "useremediespage"),
    path('useruploadremedies/', views.user_upload, name = "user_upload"),
    path('pendinglistpage/', views.pending_remedies, name = "pending_remedies"),
    path('approve_remedy/<int:id>/',views.approve_remedy,name="approve_remedy"),
    path('disapprove_remedy/<int:id>/',views.disapprove_remedy,name="disapprove_remedy"),
    path('approved_remedies/', views.approved_remedies, name = "approved_remedies"),
    path('decline_remedies/', views.decline_remedies, name = "decline_remedies"),
    path('pending_remedies/', views.pending_remedies, name = "pending_remedies"),
    path('approve_remedy/', views.approved_remedy, name = "approved_remedy"),
    path('allremedies/', views.allremedies, name = "allremedies"),
    path('email/', views.sender_email, name = "sender_email"),
    path('search_remedy/', views.search_remedies, name = "search_remedies"),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
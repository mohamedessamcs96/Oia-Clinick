from django.urls import path

from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from django.shortcuts import render,redirect


# app_name="accounts"

def custom_error404(request, param):
    return render(request,template_name="404.html")

urlpatterns=[
    path('register/',views.register_request,name='register'),
    path('contact/',views.contactus,name='contactus'),
    path('add_dr/',views.add_dr,name='adddr'),
    path('edit_dr/<int:pk>/',views.edit_dr,name='editdr'),
    path('user_contact/',views.user_contact,name='usercontact'),
    path('add_work/',views.add_work,name='addwork'),
    path('admin_panel/',views.admin_panel,name='adminpanel'),
    path('contacts_page/',views.contacts_page,name='contactspage'),
    path('about_us/',views.about_us,name='aboutus'),
    path('show_dr_details/<int:pk>/',views.show_dr_details,name='showdrdetails'),
    path('show_work_details/<int:pk>/',views.show_work_details,name='showworkdetails'),
    path('login/',views.login_request,name='login'),
    path('logout/',views.logout_request,name='logout'),
    path('',views.home_page,name='homepage'),
    path('dr_page/',views.dr_page,name='drpage'),
    path('work_page/',views.work_page,name='workpage'),
    path('home_info/',views.home_info,name='homeinfo'),
    path('delete_dr/<int:pk>/',views.delete_dr,name='deletedr'),
    path('delete_work/<int:pk>/',views.delete_work,name='deletework'),
    path('edit_work/<int:pk>/',views.edit_work,name='editwork'),
    path('<str:param>',custom_error404),

    # path('admin_panel/add_price/',views.add_price,name='addprice'),

    #path('change-language/<str:language_code>/',views.change_language,name='changelanguage'),
    path('password_reset/',auth_views.PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('reset/done/',auth_views.PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
        


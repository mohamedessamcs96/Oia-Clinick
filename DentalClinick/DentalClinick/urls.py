"""Archives URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path,include
from django.shortcuts import redirect

import django

# def custom_page_not_found(request, exception=None, template_name="404.html"):
#     return render(request, template_name, status=404)
handler404 = 'Accounts.views.custom_404_view'
handler500 = 'Accounts.views.custom_500_view'


def custom_page_not_found(request, *args, template_name="404.html", **kargs):
    return render(request, template_name, status=404)



# def custom_page_not_found(request):
#     return django.views.defaults.page_not_found(request, None)

def custom_server_error(request):
    return django.views.defaults.server_error(request)

def default_home(request):
    return redirect('ar/')

urlpatterns = [
    path("admin/", admin.site.urls),
    path('en/', include(('Accounts.urls'))),
    path('ar/', include(('Accounts.urls'))),
    path('',default_home),
    path("404/", custom_page_not_found),
    path("500/", custom_server_error),
]


"""
urlpatterns += i18n_patterns(
    url(r'^set_language/(?P<language_code>[\w-]+)/$', switch_language, name='switch_language'),
    # ... other URL patterns
)
"""

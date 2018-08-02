from django.conf.urls import include, url
from django.contrib import admin
from leads import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'leadtracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^leads/', include('leads.urls')),
    url(r'^$', include('leads.urls')),
    url(r'home/', views.home),
    url(r'login/', views.login),
    url(r'register/', views.register),
    url(r'walkins/', views.walkins),
    url(r'students/', views.students),
    url(r'status/', views.status),
]

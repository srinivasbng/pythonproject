from django.conf.urls import include, url
from django.contrib import admin
from leads import views
urlpatterns = [
    # Examples:
    # url(r'^$', 'leadtracker.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', views.index,name='index'),
    url(r'^$', views.home,name='home'),
]
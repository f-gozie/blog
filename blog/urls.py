from django.conf.urls import url
from blog import views
from django.contrib import admin

app_name = 'blog'

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^detail/(?P<post_slug>[\w\-]+)/$', views.detail, name='detail'),
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$', views.about, name='about'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.handle_login, name='handle_login'),
    url(r'^logout/$', views.handle_logout, name='handle_logout'),
    url(r'^(?P<comment_id>[0-9]+)/delete_comment/$', views.delete_comment, name='delete_comment'),
]

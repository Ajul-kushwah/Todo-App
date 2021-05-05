from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns= [
    path('', views.index, name='index'),
    path('create', views.create, name='create'),
    path('edit/<int:id>', views.edit, name='edit'),
    path('edit/update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]

# urlpatterns= [
#     url(r'^$', views.index, name='index'),
#     url(r'^create$', views.create, name='create'),
#     url(r'^edit/(?P<id>\d+)$', views.edit, name='edit'),
#     url(r'^edit/update/(?P<id>\d+)$', views.update, name='update'),
#     url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
# ]
from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [


    url(r'^getdata/', views.new),


]


urlpatterns = [
    path('', views.login, name='login'),
    path('database/home', views.home, name='home'),
    path('database/homex', views.homex, name='homex'),
    path('database/search', views.search, name='search'),
    path('database/searchx', views.searchx, name='searchx'),
    path('database/view/<key>/', views.view, name='view'),
    path('database/viewx/<keyx>/', views.viewx, name='viewx'),
    path('database/edit_record/<key>/', views.edit_record, name='edit_record'),
    path('database/edit_intern_history/<keyy>/<key>', views.edit_intern_history, name='edit_intern_history'),
    path('database/edit_intern_qualification/<keyy>/<key>/', views.edit_intern_qualification, name='edit_intern_qualification'), 
    path('database/edit_recordx/<keyx>/', views.edit_recordx, name='edit_recordx'),
    path('database/edit_xemployee_history/<keyyx>/<keyx>/', views.edit_xemployee_history, name='edit_xemployee_history'),
    path('database/edit_xemployee_degrees/<keyyx>/<keyx>/', views.edit_xemployee_degrees, name='edit_xemployee_degrees'),
    path('database/edit_xemployee_countries/<keyyx>/<keyx>/', views.edit_xemployee_countries, name='edit_xemployee_countries'),
    path('database/update_record/<key>/', views.update_record, name='update_record'),
    path('database/update_intern_history/<keyyx>/<key>/', views.update_intern_history, name='update_intern_history'),
    path('database/update_intern_qualification/<keyyx>/<key>/', views.update_intern_qualification, name='update_intern_qualification'), 
    path('database/update_recordx/<keyx>/', views.update_recordx, name='update_recordx'),
    path('database/update_xemployee_history/<keyyx>/<keyx>/', views.update_xemployee_history, name='update_xemployee_history'),
    path('database/update_xemployee_degrees/<keyyx>/<keyx>/', views.update_xemployee_degrees, name='update_xemployee_degrees'),
    path('database/update_xemployee_countries/<keyyx>/<keyx>/', views.update_xemployee_countries, name='update_xemployee_countries'), 
    path('database/new', views.new, name='new'),
   
]
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),


    path('about/', views.about, name='blog-about'),
    path('page1/', views.page1, name='blog-page1'),
    path('page2/', views.page2, name='blog-page2'),
    path('page3/', views.page3, name='blog-page3'),

    path('page4/', views.page4, name='blog-page4'),
    path('page5/', views.page5, name='blog-page5'),
    path('page6/', views.page6, name='blog-page6'),
    path('page7/', views.page7, name='blog-page7'),
    path('page8/', views.page8, name='blog-page8'),
    path('page9/', views.page9, name='blog-page9'),


    path('', views.home, name='home'),



# this is for the about page
    path('page1/', views.about, name='page1'),
    path('page2/', views.about, name='page2'),
    path('page3/', views.about, name='page3'),
    path('page4/', views.about, name='page4'),
    path('page5/', views.about, name='page5'),
    path('page6/', views.about, name='page6'),
    path('page7/', views.about, name='page7'),
    path('page8/', views.about, name='page8'),
    path('page9/', views.about, name='page9'),
# this is for page 1
    path('about/', views.page1, name='about'),
    path('page2/', views.page1, name='page2'),
    path('page3/', views.page1, name='page3'),
    path('page4/', views.page1, name='page4'),
    path('page5/', views.page1, name='page5'),
    path('page6/', views.page1, name='page6'),
    path('page7/', views.page1, name='page7'),
    path('page8/', views.page1, name='page8'),
    path('page9/', views.page1, name='page9'),
# this is for page 2
    path('about/', views.page2, name='about'),
    path('page1/', views.page2, name='page1'),
    path('page3/', views.page2, name='page3'),
# this is for page 3
    path('about/', views.page3, name='about'),
    path('page2/', views.page3, name='page2'),
    path('page1/', views.page3, name='page1'),


#this is for page 4
    path('about/', views.page4, name='about'),
    path('page1/', views.page4, name='page1'),
    path('page2/', views.page4, name='page2'),
    path('page3/', views.page4, name='page3'),
    path('page4/', views.page4, name='page4'),
    path('page5/', views.page4, name='page5'),
    path('page6/', views.page4, name='page6'),
#this is for page 5
    path('about/', views.page5, name='about'),
    path('page2/', views.page5, name='page2'),
    path('page1/', views.page5, name='page1'),
#this is for page6
    path('about/', views.page6, name='about'),
    path('page2/', views.page6, name='page2'),
    path('page1/', views.page6, name='page1')


]

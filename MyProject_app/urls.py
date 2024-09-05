from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('about/',views.about,name='about'),
    path('projects/',views.projects,name='projects'),
    # path('experience/',views.experience,name='experience'),
    path('certification/',views.certification,name='certification'),
    path('contact/',views.contact,name='contact'),
    path('resume/',views.resume,name='resume'),
]
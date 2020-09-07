from django.urls import path
from .views import (
   Courseview,
   CourseListview,
   CourseCreateview,
   CourseUpdateview,
   CourseDeleteview
    #my_fbv

)
app_name = 'courses'
urlpatterns = [
    
    path('<int:id>/update/', CourseUpdateview.as_view(), name='courses-updaate'),
    path('<int:id>/delete/', CourseDeleteview.as_view(), name='courses-delete'),
    path('create/', CourseCreateview.as_view(), name='courses-create'),
    path('', CourseListview.as_view(), name='courses-list'),
    #path('', my_fbv, name='courses-list'),
    path('<int:id>/', Courseview.as_view(), name='courses-detail'),
]
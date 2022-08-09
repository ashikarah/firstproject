from . import views
from django.urls import path

urlpatterns = [
     path('',views.add,name='add'),
     path('delete/<int:taskid>/', views.delete, name='delete'),
     # path('update/<int:id>/', views.update, name='update'),
     path('hhome/',views.tasklistview.as_view(),name='hhome'),
     path('detail/<int:pk>/',views.taskdetailview.as_view(),name='detail'),
     path('update/<int:pk>/',views.taskupdateview.as_view(),name='update'),
     path('delete/<int:pk>/',views.taskdeleteview.as_view(),name='delete')
]


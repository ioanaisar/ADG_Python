from django.contrib import admin
from django.urls import path
from .views import List, TaskDetail, add_Task, add_List, Update, CategoryView, UpdateList, DeleteTask, Login, Register, ViewFinishedTasks, ListAll, ListDetail, DeleteList, add_Category
from django.contrib.auth.views import LogoutView


urlpatterns = [
   # path('', List, name='tasks')
    #path('',List.as_view(), name='tasks')
    #path('', List.as_view(), name='view_all'),
    path('', List.as_view(), name='view_all'),
    path('lists/', ListAll.as_view(), name='lists'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'task'),
    path('list/<int:pk>/', ListDetail.as_view(), name = 'list'),
    path('task-create/', add_Task, name = 'task-create'),
    path('list-create/', add_List.as_view(), name = 'list-create'),
    path('category-create/', add_Category.as_view(), name = 'category-create'),
    path('task-update/<int:pk>/', Update.as_view(), name = 'update-task'),
    path('list-update/<int:pk>/', UpdateList.as_view(), name = 'list-update'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name = 'delete-task'),
    path('list-delete/<int:pk>/', DeleteList.as_view(), name = 'delete-list'),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'),
    path('register/', Register.as_view(), name='register'),
    path('finished-tasks', ViewFinishedTasks.as_view(), name='finished-tasks'),

]
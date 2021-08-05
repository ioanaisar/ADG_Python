from django.contrib import admin
from django.urls import path
from .views import List, TaskDetail, AddTask, AddList, Update, CategoryView, UpdateList, DeleteTask, Login, Register, \
    ViewFinishedTasks, ListAll, ListDetail, DeleteList, AddCategory, send_request, accept_request, SeeRequests, \
    SendRequests, FriendsView
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('send_request/<int:userID>/',send_request, name = 'send-request'),
    path('accept_request/<int:requestID>/',accept_request, name = 'accept-request'),
    path('send_requests/', SendRequests.as_view(), name='choose_requests'),
    path('see_requests/', SeeRequests.as_view(), name='see_requests'),
    path('see_friends/', FriendsView.as_view(), name='see_friends'),
    path('', List.as_view(), name='view_all'),
    path('lists/', ListAll.as_view(), name='lists'),
    path('categories/', CategoryView.as_view(), name='categories'),
    path('task/<int:pk>/', TaskDetail.as_view(), name = 'task'),
    path('list/<int:pk>/', ListDetail.as_view(), name = 'list'),
    path('task-create/', AddTask.as_view(), name ='task-create'),
    path('list-create/', AddList.as_view(), name ='list-create'),
    path('category-create/', AddCategory.as_view(), name ='category-create'),
    path('task-update/<int:pk>/', Update.as_view(), name = 'update-task'),
    path('list-update/<int:pk>/', UpdateList.as_view(), name = 'list-update'),
    path('task-delete/<int:pk>/', DeleteTask.as_view(), name = 'delete-task'),
    path('list-delete/<int:pk>/', DeleteList.as_view(), name = 'delete-list'),
    path('login/', Login.as_view(), name = 'login'),
    path('logout/', LogoutView.as_view(next_page='login'), name = 'logout'),
    path('register/', Register.as_view(), name='register'),
    path('finished-tasks', ViewFinishedTasks.as_view(), name='finished-tasks'),

]
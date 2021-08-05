from django.contrib import admin
from .models import  Task, ToDoList, Category, User

admin.site.register(Task)
admin.site.register(ToDoList)
admin.site.register(Category)
admin.site.register(User)
# Register your models here.

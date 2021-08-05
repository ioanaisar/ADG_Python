from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser, models.Model):
    friends = models.ManyToManyField("User", blank=True)

class FriendRequest(models.Model):
    from_user = models.ForeignKey(User, related_name='from_user', on_delete=models.CASCADE)
    to_user = models.ForeignKey(User, related_name='to_user', on_delete=models.CASCADE)


class Category(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title", default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['title']

    def __str__(self):
        return self.title

class Task(models.Model):
    # one to many relationship
    # se sterge utilizatorul se va sterge si lista, poate fi nula
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank = True)
    title = models.CharField(max_length=300, null=False, blank=True)
    resume = models.TextField(null=True, blank = True)
    status = models.BooleanField(default=False)
    createTime = models.DateTimeField(auto_now_add=True)
    main_list = models.CharField(max_length=300, null=False, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['status']


class ToDoList(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, related_name='related_lists')
    user_list = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    list_title = models.CharField(max_length=300, null=False, blank=True)
    list_state = models.CharField(max_length=100, null=False, blank=True)
    all_tasks = models.ManyToManyField(Task)
    # all_tasks = Task.objects.filter(main_list=list_title)
    list_status = models.BooleanField(default=False)

    def __str__(self):
        return self.list_title

    class Meta:
        ordering = ['list_status']
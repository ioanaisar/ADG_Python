from django import forms
from .models import Task, ToDoList, Category, User
from django.contrib.auth.forms import UserCreationForm


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class AddCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        custom_id = [rec.id for rec in self.request.user.friends.all()]
        custom_id.append(self.request.user.id)
        self.fields['user'].queryset = User.objects.filter(id__in=custom_id)

    class Meta:
        model = Category
        fields = ['title', 'user']
        exclude = []


class AddTaskForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(AddTaskForm, self).__init__(*args, **kwargs)
        custom_id = [rec.id for rec in self.request.user.friends.all()]
        custom_id.append(self.request.user.id)
        self.fields['user'].queryset = User.objects.filter(id__in=custom_id)

    class Meta:
        model = Task
        fields = ['title', 'resume', 'status', 'user']
        exclude = []


class AddListForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request')
        super(AddListForm, self).__init__(*args, **kwargs)
        self.fields['all_tasks'].queryset = Task.objects.filter(
            user=self.request.user)

        custom_id = [rec.id for rec in self.request.user.friends.all()]
        custom_id.append(self.request.user.id)
        self.fields['user_list'].queryset = User.objects.filter(id__in=custom_id)
        self.fields['category'].queryset = Category.objects.filter(user=self.request.user)
        # self.fields['user_list'].queryset = self.request.user.friends.all()

    class Meta:
        model = ToDoList
        fields = ['list_title', 'list_state', 'user_list', 'all_tasks', 'category']

    list_title = forms.CharField()
    list_state = "Not done"
    all_tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(), required=False,
        widget=forms.CheckboxSelectMultiple
    )

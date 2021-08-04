from django import forms
from .models import Task, ToDoList, Category, User
from django.contrib.auth.forms import UserCreationForm



class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields


class AddCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(AddCategoryForm, self).__init__(*args, **kwargs)
        self.user = self.request.user

    class Meta:
        model = Category
        # fields = ['name', 'quantity']
        fields = ['title', 'user']
        exclude = []
        # tasks = Task.objects.all().filter(user=request.user)




class AddTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = ['name', 'quantity']
        fields = ['title', 'resume', 'status', 'main_list', 'user']
        exclude = []


class AddListForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        """ Grants access to the request object so that only members of the current user
        are given as options"""

        self.request = kwargs.pop('request')
        super(AddListForm, self).__init__(*args, **kwargs)
        self.fields['all_tasks'].queryset = Task.objects.filter(
            user=self.request.user)

    class Meta:
        model = ToDoList
        fields = ['list_title', 'list_status', 'user_list', 'all_tasks', 'list_state', 'category']
    list_title = forms.CharField()
    list_status = forms.BooleanField
    list_state = "Not done"
    all_tasks = forms.ModelMultipleChoiceField(
        queryset=Task.objects.all(),
        # tasks = Task.objects.all().filter(user=request.user)
        widget=forms.CheckboxSelectMultiple
    )


class FilterLists(forms.Form):
    has_image = forms.BooleanField(label='Show finished lists')

    def get_lists(self):
        lists = ToDoList.objects.all()
        filter_done_lists = self.cleaned_data.get('has_image', False)

        if filter_done_lists:
            lists = lists.exclude(list_state="Done")
        return lists
from django.shortcuts import render, Http404, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from .models import Task, ToDoList, Category, User, FriendRequest
from .forms import AddTaskForm, AddListForm, AddCategoryForm, FilterLists, CustomUserCreationForm
from django.contrib import messages
from django.views.generic.edit import UpdateView, DeleteView, FormView
from django.urls import reverse_lazy
from django.contrib.auth import login
from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#def List(request, LoginRequiredMixin):
 #    if request.method == 'GET':
  #        data = Task.objects.all()

   #  return render(request, 'list_app/task_list.html', {
    #      'tasks': data,
     #     })


def send_request(request, userID):
    from_user = request.user
    to_user = User.objects.get(id=userID)
    friend_request, created = FriendRequest.objects.get_or_create(from_user=from_user, to_user=to_user)
    if created:
        return HttpResponse('friend request sent')
    else:
        return HttpResponse('friend request was already sent')


def accept_request(request, requestID):
    friend_request = FriendRequest.objects.get(id=requestID)
    if friend_request.to_user == request.user:
        friend_request.to_user.friends.add(friend_request.from_user)
        friend_request.from_user.friends.add(friend_request.to_user)
        friend_request.delete()
        return HttpResponse('friend request accepted')
    else:
        return HttpResponse('friend request was not accepted')



class CategoryView(ListView):
    model = Category
    context_object_name = 'categories'
    template_name = 'list_app/category_show.html'
    def get_context_data(self, **kwargs):
        all_lists = super().get_context_data(**kwargs)
        all_lists['categories'] = all_lists['categories'].filter(user=self.request.user)
        return all_lists

class FriendsView(ListView):
    model = User
    context_object_name = 'user'
    template_name = 'list_app/friends.html'
    def get_context_data(self, **kwargs):
        all_lists = super().get_context_data(**kwargs)
        all_lists['user']=self.request.user
        return all_lists



class SendRequests(LoginRequiredMixin, ListView):
    model = User
    context_object_name = 'all_users'
    template_name = 'list_app/choose_request.html'

class SeeRequests(LoginRequiredMixin, ListView):
    model = FriendRequest
    context_object_name = 'all_users'
    template_name = 'list_app/receive_request.html'

class ListAll(LoginRequiredMixin, ListView):
    model = ToDoList
    context_object_name = 'lists'
    template_name = 'list_app/todolist_list.html'


    def get_context_data(self, **kwargs):
        all_lists = super().get_context_data(**kwargs)
        all_lists['lists'] = all_lists['lists'].filter(user_list=self.request.user)
        all_lists['count'] = all_lists['lists'].filter(list_status=False).count()

        new_list = []
        for list1 in all_lists['lists']:
            state = "Done"
            for task in list1.all_tasks.all():
                if task.status == False:
                    state = "Not done"
            list1.list_state = state
            new_list.append(list1)
        all_lists['lists'] = new_list


        return all_lists


class List(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    def get_context_data(self, **kwargs):
        all_data = super().get_context_data(**kwargs)
        all_data['tasks'] = all_data['tasks'].filter(user=self.request.user)
        all_data['count'] = all_data['tasks'].filter(status=False).count()

        wanted_input = self.request.GET.get('search-area') or ''
        if wanted_input:
            all_data['tasks'] = all_data['tasks'].filter(title__icontains=wanted_input)
        all_data['wanted_input'] = wanted_input


        # all_data['tasks'] = all_data['tasks'].filter(status=True)
        return all_data


class ViewFinishedTasks(LoginRequiredMixin, ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'list_app/task_finished.html'

    def get_context_data(self, **kwargs):
        all_data = super().get_context_data(**kwargs)
        all_data['tasks'] = all_data['tasks'].filter(user=self.request.user)
        all_data['count'] = all_data['tasks'].filter(status=False).count()
        all_data['tasks'] = all_data['tasks'].filter(status=True)

        return all_data


class TaskDetail(LoginRequiredMixin, DetailView):
     model = Task
     context_object_name = 'task'
     template_name = 'list_app/task_template.html'


class ListDetail(LoginRequiredMixin, DetailView):
    model = ToDoList
    context_object_name = 'list'
    template_name = 'list_app/list_template.html'


def add_Task(request):
    if request.method == 'GET':
        form = AddTaskForm()

        return render(request, 'list_app/task_form.html', {
            'form': form,
        })

    if request.method == 'POST':
        form = AddTaskForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()

            messages.success(request, 'Product was successfully added!')

            data = Task.objects.all()
            return redirect(reverse('view_all'))
        return render(request, 'list_app/task_form.html', {
            'form': form,
        })
    raise Http404('Method not allowed!')
            #return render(request, 'list_app/task_list.html', {
             #   'tasks': data,
            #})

class add_List(CreateView):
    model = ToDoList
    form_class = AddListForm
    template_name = 'list_app/list_form.html'
    success_url = reverse_lazy('view_all')

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(add_List, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class add_Category(CreateView):
    model = Category
    form_class = AddCategoryForm
    template_name = 'list_app/category.html'
    success_url = reverse_lazy('view_all')
    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(add_Category, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

class Update(LoginRequiredMixin, UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('view_all')


class UpdateList(LoginRequiredMixin, UpdateView):
    model = ToDoList
    form_class = AddListForm
    template_name = 'list_app/list_form.html'
    success_url = reverse_lazy('view_all')
    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(UpdateList, self).get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs


class DeleteTask(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('view_all')


class DeleteList(LoginRequiredMixin, DeleteView):
    model = ToDoList
    context_object_name = 'list'
    success_url = reverse_lazy('view_all')
    template_name = 'list_app/list_delete.html'


class Login(LoginView):
    template_name = 'list_app/login.html'
    fields = '__all__'
    redirect_authenticated_user = True
    def get_success_url(self):
        return reverse_lazy('view_all')


class Register(FormView):
    template_name = 'list_app/register.html'
    form_class = CustomUserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('view_all')

    def form_valid(self, form):
        new_user = form.save()
        if new_user is not None:
            login(self.request, new_user)
        return super(Register, self).form_valid(form)
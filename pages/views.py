from django.shortcuts import render, redirect
# from django.views import View
# from django.views.generic import (
#     ListView,
#     DetailView,
#     CreateView,
#     UpdateView,
#     DeleteView,
# )
# from django.http import HttpResponse
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from .models import *
# from .forms import *
# from blogSite.urls import *
# from .forms import PostForm, PostEditForm, CommentPostForm
from django.urls import reverse_lazy
# from pages.templates import *

from django.contrib.auth.views import LoginView 
from django.contrib.auth.mixins import LoginRequiredMixin 





# def index(request):
#     data = Student.objects.all()
#     context = {"data": data}
#     return render(request, "display.html", context)


# def uploadok(request):
#     return HttpResponse("succesful")


# # Create your views here.


# class homePageView(ListView):
#     model = Post
#     template_name = "index.html"
#     context_object_name = "home"

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['home'] = context['home'].filter(User=self.request.user)


    #     return context


# class secondHomePageView(ListView):
#     model = Student
#     template_name = "student.html"


# def loginView(request):
#     return render(request, "index2.html")


# class BlogDetailView(DetailView):
#     model = Post
#     template_name = "content_prev.html"


# class CommentView(CreateView):
#     model = Comment
#     template_name = "comment_new.html"
#     form_class = CommentPostForm


# class CommentDeleteView(CreateView):
#     model = Post
#     template_name = "post_prev.html"
#     form_class = PostForm

# class BlogCreateView(CreateView):
#     model = Post
#     template_name = "post_new.html"
#     form_class = PostForm


# class BlogUpdateView(UpdateView):
#     model = Post
#     template_name = "post_edit.html"
#     form_class = PostEditForm


# class BlogDeleteView(DeleteView):
#     model = Post
#     template_name = "post_delete.html"
#     success_url = reverse_lazy("home")


# def CategoryView(request, category):
#     category_posts = Post.objects.filter(category=category)
#     return render(
#         request,
#         "category.html",
#         {"category_posts": category_posts, "category": category},
#     )


from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    FormView,
)

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import login

class CustomLoginView(LoginView):
    template_name = 'login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')
    
class RegisterPage(FormView):
    template_name = 'signup.html'
    form_class = UserCreationForm 
    redirect_authenticated_user = True
    success_url = reverse_lazy('login')

    def form_valid(self, form):
        user = form.save()
        if user is not None:
            login(self.request, user)
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return reverse_lazy('login')  
        return super(RegisterPage, self).get(*args, **kwargs)



class TaskList(LoginRequiredMixin ,ListView):
    model = Task 
    template_name = 'task.html'
    context_object_name = 'tasks'
    fields = ["Is_task_complete_skip_if_no"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(Is_task_complete_skip_if_no=False).count()
        context['counter'] = context['tasks'].filter(Is_task_complete_skip_if_no=True).count()




        return context
class TaskDetail(LoginRequiredMixin,DetailView):
    model = Task
    template_name = 'content_prev.html'
    context_object_name = 'task'

class TaskCreate(LoginRequiredMixin,CreateView):
    model = Task
    template_name = 'post_new.html'
    fields = ['title','description','Is_task_complete_skip_if_no']
    success_url = reverse_lazy('tasks')
    context_object_name = 'create'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)
        

class TaskEdit(LoginRequiredMixin,UpdateView):
    model = Task
    template_name = 'post_edit.html'
    fields = ['title','description','Is_task_complete_skip_if_no']
    success_url = reverse_lazy('tasks')
    context_object_name = 'edit'

class TaskDelete(LoginRequiredMixin,DeleteView):
    model = Task
    template_name = 'post_delete.html'
    # fields = '__all__'
    success_url = reverse_lazy('tasks')
    context_object_name = 'delete' 


class HomePage(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'home'

class DashBoard(LoginRequiredMixin ,ListView):
    model = Task
    template_name = 'dashboard.html'
    context_object_name = 'dashboard'
    fields = ["Is_task_complete_skip_if_no"] 

    def get_context_data(self, **kwargs):
        context_1 = super().get_context_data(**kwargs)
        context_1['dashboard'] = context_1['dashboard'].filter(user=self.request.user)
        context_1['count'] = context_1['dashboard'].filter(Is_task_complete_skip_if_no=False).count()
        context_1['counter'] = context_1['dashboard'].filter(Is_task_complete_skip_if_no=True).count()
        context_1['count3'] = context_1['dashboard'].filter(Is_task_complete_skip_if_no=True).count() + context_1['dashboard'].filter(Is_task_complete_skip_if_no=False).count() 

        # context_2 = super().get_context_data(**kwargs)
        # context_2['dashboard2'] = context_2['dashboard2'].filter(user=self.request.user)
        # context_2['note_count'] = context_2['dashboard2'].filter(Is_note_complete_skip_if_no=False).count()
        # context_2['note_counter'] = context_2['dashboard2'].filter(Is_note_complete_skip_if_no=True).count()
        # context_2['note_count3'] = context_2['dashboard2'].filter(Is_note_complete_skip_if_no=True).count() + context_2['dashboard2'].filter(Is_note_complete_skip_if_no=False).count() 



        

        return context_1

        

# class DashBoard2(LoginRequiredMixin ,ListView):
#     model = Note
#     template_name = 'dashboard.html'
#     context_object_name = 'dash'
#     fields = ["completed"]

#     def get_context_data(self, **kwargs):
#         context_1 = super().get_context_data(**kwargs)
#         context_1['dash'] = context_1['dash'].filter(user=self.request.user)
#         context_1['counts'] = context_1['dash'].filter(completed=False).count()
      
#         return context_1    

class NoteView(LoginRequiredMixin ,ListView):
    model = Note
    template_name = 'note.html'
    context_object_name = 'notes'
    fields = ["Is_note_complete_skip_if_no"]

    def get_context_data(self, **kwargs):
        context_2 = super().get_context_data(**kwargs)
        context_2['notes'] = context_2['notes'].filter(user=self.request.user)
        context_2['counts'] = context_2['notes'].filter(Is_note_complete_skip_if_no=False).count()
        context_2['counter'] = context_2['notes'].filter(Is_note_complete_skip_if_no=True).count()




        return context_2

class NoteCreate(LoginRequiredMixin,CreateView):
    model = Note
    template_name = 'new_note.html'
    fields = ['title','description','Is_note_complete_skip_if_no']
    success_url = reverse_lazy('notes')
    context_object_name = 'create_note'

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(NoteCreate, self).form_valid(form)

class NoteDetail(LoginRequiredMixin,DetailView):
    model = Note
    template_name = 'content_prev.html'
    context_object_name = 'note'   

class NoteEdit(LoginRequiredMixin,UpdateView):
    model = Note
    template_name = 'post_edit.html'
    fields = ['title','description','Is_note_complete_skip_if_no']
    success_url = reverse_lazy('notes')
    context_object_name = 'edit'

class NoteDelete(LoginRequiredMixin,DeleteView):
    model = Note
    template_name = 'post_delete.html'
    # fields = '__all__'
    success_url = reverse_lazy('notes')
    context_object_name = 'delete'          












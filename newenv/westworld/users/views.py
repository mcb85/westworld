from django.shortcuts import render, get_object_or_404, redirect

from django.http import HttpResponse, Http404
from django.views.generic import ListView, DetailView
from .forms import UserForm

from .models import User

def index(request):

    context = { 'name' : 'Adonis', 'users' : User.objects.all() }

    return render(request, 'users/index.html', context)

def detail(request, user_id):
    # try:
    # context = {
    #     'user': User.objects.get(pk=user_id),
    # }
    # except User.DoesNotExist:
    #     raise Http404("does not exist")
    
    user= get_object_or_404(User, pk=user_id)
    context={
    'user': User.objects.get(pk=user_id),
     }
    return render(request, 'users/detail.html', context)

# def add(request):

#     context = { 'header' : 'This is the add view!'}

#     return render(request, 'users/add.html', context)


class UserListView(ListView):
    model = User
    template_name = 'users/index.html'

    def get_context_data(self, **kwargs):
        context = super(UserListView, self).get_context_data(**kwargs)
        context['power_level'] = "Superhero"
        return context
        
class DetailListView(DetailView):
    model = User
    template_name = 'users/detail.html'

def add(request):
    context = { 'header' : 'GET', 'form': UserForm() }
    return render(request, 'users/add.html', context)

    def add(request):
        if request.method == "POST":
            form = UserForm(request.POST)

            if form.is_valid():
                User(
                    name=form.cleaned_data['name'],
                    nickname=form.cleaned_data['nickname'],
                    email=form.cleaned_data['email'],
                    age=form.cleaned_data['age']
                ).save()

                return redirect('users:index')
            
            else:
                return render(request, 'users/add.html', {'form': form})

        else:
         context = { 'header' : 'GET', 'form': UserForm() }
         return render(request, 'users/add.html', context)


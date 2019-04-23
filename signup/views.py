from django.shortcuts import render,get_object_or_404,redirect
from .forms import signupform,rawsignupform
from .models import signup
from django.urls import reverse
from django.views.generic import(
    CreateView,
    DeleteView,
    ListView,
    DetailView,
    ListView,
    UpdateView

)
# Create your views here.
class SignupCreateView(CreateView):
    template_name = 'signup/signup_create.html'
    form_class = signupform
    queryset = signup.objects.all()

class SignupDetailView(DetailView):
    template_name = 'signup/signup_detail.html'
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(signup, id=id_)

class SignupUpdateView(UpdateView):
    template_name = 'signup/signup_update.html'
    form_class = rawsignupform
    queryset = signup.objects.all()
    def get_object(self):
        id_ = self.kwargs.get("id")
        return get_object_or_404(signup, id=id_)
    def get_success_url(self):
         return reverse('signup:signup-list')
class SignupListView(ListView):
    template_name = 'signup/signup_list.html'
    queryset = signup.objects.all()

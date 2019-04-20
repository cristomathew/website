from django.shortcuts import render,get_object_or_404,redirect
from .forms import signupform,rawsignupform
from .models import signup
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
def signup_create_view(request):
    form = signupform(request.POST or None)
    if form.is_valid():
        form.save()
        form = signupform()
    context = {
        'form' : form
    }
    return render(request,"signup/signup_create.html",context)
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

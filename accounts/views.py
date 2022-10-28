from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView
from .models import Profile
from .forms import CustomUserCreationForm

# Create your views here.

class SignUpView(CreateView):
    form_class = CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/signup.html'

class ProfileEditView(UpdateView):
    model = Profile
    fields = ['fav_author']
    template_name = 'registration/edit_profile.html'
    success_url = reverse_lazy('home')

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'


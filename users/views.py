from django.shortcuts import render
from django.views import View

from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
class ProfileViewProfile(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        return render(request, 'users/profile.html')
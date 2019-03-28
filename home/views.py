from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin



class HomePageView(LoginRequiredMixin, View):
    template_name = 'home/home.html'

    def get(self, request):

        context = {
        'title': 'Home Page',
        }
        return render(request, self.template_name, context)

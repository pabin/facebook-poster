from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db import transaction
import datetime

from .forms import (
    UserLoginForm,
    FacebookPageIDAddForm,
    FacebookAccessTokenAddForm,
)

from .models import (
    FacebookPageID,
    FacebookAccessToken,
)

class UserLoginView(View):
    template_name = 'accounts/login.html'
    form_class = UserLoginForm
    title = 'User Login'
    year = (datetime.datetime.now()).year

    def get(self, request):
        user = request.user
        form = self.form_class

        context = {
        'title': self.title,
        'form': form,
        'year': self.year,
        }
        if user.is_authenticated:
            context['authentication'] = True
            print('logged in')
            return HttpResponseRedirect(reverse('home'))
        print('logged out')
        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user
        form = self.form_class(request.POST or None)

        context = {
        'title': self.title,
        'form': form,
        'year': self.year,
        }

        context['authentication'] = True if user.is_authenticated else False
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(username=username, password=password)

            if user:
                login(request, user)
                print('logged in')
                return HttpResponseRedirect(reverse('home'))
            else:
                context['login_failure'] = True
                return render(request, self.template_name, context)

        context['login_failure'] = False
        return render(request, self.template_name, context)


def user_logout(request):
    user = request.user
    if user.is_authenticated:
        logout(request)
        print('logged out')
        return HttpResponseRedirect(reverse('login'))
    return HttpResponseRedirect(reverse('login'))



class FacebookPageIDAddView(LoginRequiredMixin, View):
    template_name = 'accounts/form.html'
    form_class = FacebookPageIDAddForm
    title = 'Add Facebook Page ID'

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {
            'form': form,
            'title': self.title,
        }

        if form.is_valid():
            page = form.save(commit=False)
            page.user = request.user

            page.save()

            messages.success(request, 'New Facebook Page Added Successfully!', extra_tags='success')
            return HttpResponseRedirect(reverse('facebook_page_list'))

        context['failure'] = True
        messages.error(request, 'Error! on Facebook Page Addition!', extra_tags='danger')
        return render(request, self.template_name, context)


class FacebookAccessTokenAddView(LoginRequiredMixin, View):
    template_name = 'accounts/form.html'
    form_class = FacebookAccessTokenAddForm
    title = 'Add Facebook Access Token'

    def get(self, request):
        form = self.form_class()
        context = {
            'form': form,
            'title': self.title,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {
            'form': form,
            'title': self.title,
        }

        if form.is_valid():
            access_token = form.save(commit=False)
            access_token.user = request.user
            access_token.save()

            context['success'] = True
            return render(request, self.template_name, context)

        context['failure'] = True
        return render(request, self.template_name, context)


class FacebookAccessTokenUpdateView(LoginRequiredMixin, View):
    template_name = 'accounts/form.html'
    form_class = FacebookAccessTokenAddForm
    title = 'Update Facebook Access Token'

    def get(self, request, access_token_id):
        form = self.form_class()

        context = {
            'title': self.title,
            'form': form,
        }

        return render(request, self.template_name, context)

    def post(self, request, access_token_id):
        access_token = get_object_or_404(FacebookAccessToken, id=access_token_id)
        form = self.form_class(instance=access_token, data=request.POST)

        context = {
            'title': self.title,
            'form': form,
        }

        if form.is_valid():
            instance = form.save()

            context['success'] = True
            return render(request, self.template_name, context)

        context['failure'] = True
        return render(request, self.template_name, context)


class FacebookPageListView(LoginRequiredMixin, View):
    template_name = 'accounts/fb_page_list.html'

    def get(self, request):
        pages = FacebookPageID.objects.filter(is_archived=False, user=request.user)

        context = {
        'title': 'Facebook Pages',
        'pages': pages,
        }
        return render(request, self.template_name, context)


class FacebookPageDeleteView(LoginRequiredMixin, View):

    def get(self, request, page_id):
        try:
            with transaction.atomic():
                page = FacebookPageID.objects.get(id=page_id)
                page.is_archived = True
                page.save()
                messages.success(request, page.name+ ' Page Deleted Successfully!', extra_tags='success')

        except Exception as e:
            print('Exception: ', e)
            messages.error(request, 'Error! Selected Page doesnot exist,', extra_tags='danger')

        return HttpResponseRedirect(reverse('facebook_page_list'))

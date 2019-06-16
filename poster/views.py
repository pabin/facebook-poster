from django.shortcuts import render, get_object_or_404
from django.views import View
import facebook
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from .forms import (
    StatusUpdateForm,
)


from accounts.models import (
    FacebookPageID,
    FacebookAccessToken,
)


class StatusUpdateView(LoginRequiredMixin, View):
    template_name = 'accounts/form.html'
    form_class = StatusUpdateForm
    title = 'FB POST'

    def get(self, request):
        form = self.form_class(user=request.user)
        context = {
            'form': form,
            'title': self.title
        }
        return render(request, self.template_name, context)

    def post(self, request):
        token_object = FacebookAccessToken.objects.filter().first()

        form = self.form_class(request.POST, user=request.user)
        context = {
            'form': form,
            'title': self.title
        }

        if form.is_valid():
            try:
                msg = form.cleaned_data.get('message')
                image_url = form.cleaned_data.get('image_url')
                all_page = form.cleaned_data.get('all_page')
                multiple_pages = form.cleaned_data.get('multiple_pages')

                if all_page and not multiple_pages:
                    selected_pages = FacebookPageID.objects.filter(user=request.user, is_archived=False, is_active=True)

                elif multiple_pages and not all_page:
                    selected_pages = []
                    for page_id in multiple_pages:
                        pages = get_object_or_404(FacebookPageID, id=page_id)
                        selected_pages.append(pages)

                elif all_page and multiple_pages:
                    selected_pages = FacebookPageID.objects.filter(user=request.user, is_archived=False, is_active=True)

                else:
                    messages.error(request, 'Error! Please Select at least One Page to Post', extra_tags='warning')
                    return render(request, self.template_name, context)


                # Facebook API call
                graph = facebook.GraphAPI(token_object.token)

                resp = graph.get_object('me/accounts')

                for fb_page in selected_pages:
                    page_access_token = None
                    for page in resp['data']:
                        if page['id'] == fb_page.page_id:
                            page_access_token = page['access_token']

                    graph = facebook.GraphAPI(page_access_token)

                    if msg and not image_url:
                        status = graph.put_object(
                            parent_object = "me",
                            connection_name = "feed",
                            message=msg)

                    elif msg and image_url:
                        status = graph.put_object(
                            parent_object = "me",
                            connection_name = "photos",
                            url = image_url,
                            message=msg)

                context['success'] = True
                messages.success(request, 'Status Message Posted Successfully!', extra_tags='success')
                return render(request, self.template_name, context)

            except Exception as e:
                print('Exception', e)
                messages.error(request, 'Error! on Status Message Posting!', extra_tags='danger')
                return render(request, self.template_name, context)

        messages.error(request, 'Error! Invalid Form Submitted!', extra_tags='warning')
        return render(request, self.template_name, context)

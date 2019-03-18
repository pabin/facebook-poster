from django.shortcuts import render
from django.views import View
import facebook

from .forms import (
    StatusUpdateForm,
)
from .tokens import cfg

class StatusUpdateView(View):
    template_name = 'home/home.html'
    form_class = StatusUpdateForm

    def get(self, request):
        form = self.form_class()
        context = {
        'form': form,
        }
        return render(request, self.template_name, context)

    def post(self, request):
        form = self.form_class(request.POST)
        context = {
            'form': form,
        }

        if form.is_valid():
            try:
                msg = form.cleaned_data.get('message')
                image_url = form.cleaned_data.get('image_url')
                print(msg)

                # Facebook API call
                graph = facebook.GraphAPI(self.cfg["access_token"])
                resp = graph.get_object('me/accounts')
                page_access_token = None

                for page in resp['data']:
                    if page['id'] == self.cfg['page_id']:
                        page_access_token = page['access_token']

                graph = facebook.GraphAPI(page_access_token)

                # Status Posting with API
                status = graph.put_object(
                    parent_object = "me",
                    connection_name = "feed",
                    message=msg)

                context['status'] = 'success'
                return render(request, self.template_name, context)

            except Exception as e:
                print('Exception', e)
                context['status'] = 'failure'
                return render(request, self.template_name, context)

        context['status'] = 'failure'
        return render(request, self.template_name, context)

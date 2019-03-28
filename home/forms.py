from django import forms

from accounts.models import (
    FacebookPageID,
)

class StatusUpdateForm(forms.Form):
    message = forms.CharField(label='Message')
    image_url = forms.URLField(label='Image URL', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        pages = FacebookPageID.objects.all()

        # for p in pages:
        #     self.fields.update(p.name)

        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
                })

        # self.fields['is_active'].widget.attrs.update({
        #     'class': 'bootstrap-switch',
        #     'data-on-text': "YES",
        #     'data-off-text': "NO",
        #     'checked': 'checked',
        # })

from django import forms

from accounts.models import (
    FacebookPageID,
)

class StatusUpdateForm(forms.Form):
    message = forms.CharField(label='Status/Caption*', widget=forms.Textarea(attrs={'rows':4, 'cols':15}))
    image_url = forms.URLField(label='Image URL', required=False)
    # video_url = forms.URLField(label='Video URL', required=False)
    # video_description = forms.CharField(label='Video Description', required=False)
    all_page = forms.BooleanField(label="Post on All Page", required=False)
    multiple_pages = forms.MultipleChoiceField(label='Select Pages to Post', required=False)

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')

        super().__init__(*args, **kwargs)

        self.fields['multiple_pages'].choices = [
            (a.id, a) for a in FacebookPageID.objects.filter(user=user, is_archived=False, is_active=True)]

        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
            })

        self.fields['all_page'].widget.attrs.update({
            'class': 'checkbox-inline',
            'data-toggle': 'toggle',
            'data-onstyle': "success",
            'data-offstyle': "danger",
            'data-on': "Yes",
            'data-off': "No",
        })

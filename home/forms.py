from django import forms



class StatusUpdateForm(forms.Form):
    message = forms.CharField(label='Message')
    image_url = forms.URLField(label='Image URL', required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for _, field in self.fields.items():
            field.widget.attrs.update({
                'class': 'form-control'
                })

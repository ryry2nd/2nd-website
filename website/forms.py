from django import forms

class SetUsername(forms.Form):
    rowNumber = forms.IntegerField(max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['rowNumber'].widget.attrs['autocomplete'] = 'off'
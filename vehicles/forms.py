from django import forms
from .models import PhoneInspection


class PhoneInspectionForm(forms.ModelForm):
    brand = forms.CharField(
        max_length=100,
        label='Phone Brand',
        widget=forms.TextInput(attrs={
            'placeholder': 'e.g. Apple, Samsung, Xiaomi...',
            'autocomplete': 'off',
            'id': 'brandInput',
        })
    )

    class Meta:
        model = PhoneInspection
        fields = ['brand', 'condition', 'image']

    def __init__(self, *args, **kwargs):
        kwargs.pop('user', None)
        super().__init__(*args, **kwargs)
        self.fields['condition'].label = 'Device Condition'
        self.fields['image'].label = 'Photo'

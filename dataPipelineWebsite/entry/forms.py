from django import forms

from dataPipelineWebsite.entry.models import Data

kinds = (
    ('', 'Choose...'),
    ('corner', 'Corner shop'),
    ('super', 'Supermarket'),
    ('farm', 'Farm shop'),
    ('market', 'Food market')
)


class DataEntryForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tesco'}))
    distance = forms.FloatField(widget=forms.TextInput(attrs={'placeholder': '1.5'}))
    location = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Shop location'}))
    kind = forms.ChoiceField(choices=kinds)

    class Meta:
        model = Data
        fields = "__all__"

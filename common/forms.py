from django import forms


class CityForm(forms.Form):
    your_city = forms.CharField(initial='Brooklyn', max_length=50, label='')

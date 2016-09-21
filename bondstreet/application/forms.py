from django import forms

from .models import Application


class ApplicationForm1(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['favorite_animal']


class ApplicationForm2(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['favorite_body_part', 'favorite_color']


class ApplicationForm3(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['favorite_smell']


class ApplicationForm4(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['favorite_taste']


class ApplicationForm5(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['favorite_texture', 'favorite_word']

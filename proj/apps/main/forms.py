from django import forms
from django.forms import ModelForm

from django_summernote.widgets import SummernoteWidget
# from apps.maven.widgets import MavenImageSelectorWidget

# from .models import Challenge, Task
from .models import Cache, Team

class TeamLoginForm(forms.Form):
    team = forms.CharField(
        label='Team Name',
        required=True,
    )
    password = forms.CharField(
        label='Password',
        required=True,
        widget=forms.PasswordInput(),
    )

class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        exclude = []
        widgets = {
            'data': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        }

class CacheForm(forms.ModelForm):
    class Meta:
        model = Cache
        exclude = []
        widgets = {
            'game': forms.Textarea(attrs={'cols': 80, 'rows': 20})
        }

class ChallengeForm(forms.Form):
    field0  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field1  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field2  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field3  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field4  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field5  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field6  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field7  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field8  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field9  = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field10 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field11 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field12 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field13 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field14 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field15 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field16 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field17 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field18 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field19 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    field20 = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': "form-control"}))
    scroll_pos = forms.HiddenInput()
    penalty = forms.HiddenInput()

# class ChallengeEditForm(ModelForm):
#     class Meta:
#         model = Challenge
#         exclude = []
#         exclude = []
#             'image': MavenImageSelectorWidget(url="Challenges"),
#         }

# class TaskEditForm(ModelForm):
#     class Meta:
#         model = Task
#         exclude = []
#         widgets = {
#             'pre_text': SummernoteWidget(),
#             'post_text': SummernoteWidget(),
#         }
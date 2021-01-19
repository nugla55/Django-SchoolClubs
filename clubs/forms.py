from django import forms
from django.forms import ModelForm
from clubs.models import *


class addSurveyForm(ModelForm):
    question = forms.Textarea()
    end_date = forms.DateTimeField(label="Pick Up Date",
                                   widget=forms.DateTimeInput(attrs={
                                       "type": "datetime-local", "name": "tookDate", "id": "first", "min": "",
                                       "class": "form-control datepicker px-3"
                                   }))

    class Meta:
        model = Survey
        fields = ['question', 'element1', 'element2', 'end_date']
        widgets = {
            'question': forms.Textarea(attrs={'rows': 2, 'cols': 50}),
        }


class addPostForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['content', 'post_pic']

        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
        }


class addDiscussionForm(ModelForm):
    class Meta:
        model = Discussion
        fields = ['topic', 'content']

        widgets = {
            'content': forms.Textarea(attrs={'rows': 5, 'cols': 50}),
            'topic': forms.Textarea(attrs={'rows': 1, 'cols': 50})
        }


class addEventForm(ModelForm):
    until_date = forms.DateTimeField(label="Pick Up Date",
                                     widget=forms.DateTimeInput(attrs={
                                         "type": "datetime-local", "name": "tookDate", "id": "first", "min": "",
                                         "class": "form-control datepicker px-3"
                                     }))

    class Meta:
        model = Event
        fields = ['location', 'event_name', 'content', 'until_date']

        widgets = {

        }


from django.forms.widgets import FileInput
from django.utils.translation import gettext_lazy as _


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ('profile_pic',)

        labels = {
            'profile_pic': _('Profile image:'),
        }

        widgets = {
            'profile_pic': FileInput(),
        }


class AddClubForm(ModelForm):
    class Meta:
        model = Club
        fields = ('club_name', 'email', 'advisor', 'club_pic', )


class AddAdministrationForm(ModelForm):
    class Meta:
        model = Administration
        fields = ("__all__")

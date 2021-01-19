from django import forms

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class SignupForm(UserCreationForm):
    department_category = (
        ('Computer Engineering', 'Computer Engineering'),
        ('Software Engineering', 'Software Engineering'),
        ('Electrical and Electronics Engineering', 'Electrical and Electronics Engineering'),
        ('Industrial Engineering', 'Industrial Engineering'),
        ('Mechanical Engineering', 'Mechanical Engineering'),
        ('Civil  Engineering', 'Civil  Engineering'),
    )
    dep = forms.ChoiceField(choices=department_category)
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2','dep')

    def clean(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email exists")

        return self.cleaned_data
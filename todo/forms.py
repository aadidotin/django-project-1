from django import forms
from .models import Todo
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# Create User Registration Form
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        # widgets = {
        #     "username": forms.TextInput(attrs={"class": "form-control"})
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            # For <select>
            if isinstance(field.widget, forms.Select):
                field.widget.attrs.update(
                    {'class': 'form-select custom-select'}
                )
            # For <input>, <textarea>, etc.
            else:
                field.widget.attrs.update(
                    {'class': 'form-control custom-input'}
                )


# Create Todo Form
class TodoForm(forms.ModelForm):

    class Meta:
        model = Todo
        fields = ("title", "photo")
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            # "photo": forms.FileField(attrs={"class": "form-control"}, required=False)
            # "photo": forms.FileField(required=False)
        }

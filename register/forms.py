from django.contrib.auth.forms import UserCreationForm
from django.forms import EmailField
from .models import CustomUser


class UserCreateForm(UserCreationForm):

    class Meta:
        model = CustomUser
        fields = ("first_name", "last_name", "email", "username",
                  "password")

    def save(self, commit=True):
        user = super(UserCreateForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

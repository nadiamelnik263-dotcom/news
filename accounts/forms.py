from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):  #форма для користувача
    class Meta:
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ("age",)


class CustomUserChangeForm(UserChangeForm): #форма для суперкористувача
    class Meta:
        model = CustomUser
        fields = UserChangeForm.Meta.fields
from django.contrib.auth.forms import UserCreationForm

from .models import CustomUser


# class UserForm(forms.ModelForm):
#     class Meta:
#         model = CustomUser
#         fields = ("username", "password", "confirm_password", "first_name", "last_name", "mobile", "place")
#         widgets={'confirm_password':forms.PasswordInput(),}
#     def clean(self):
#         cleaned_data = super(UserCreationForm, self).clean()
#         password = cleaned_data.get("password")
#         confirm_password = cleaned_data.get("confirm_password")
#
#         if password != confirm_password:
#             raise forms.ValidationError(
#                 "password and confirm_password does not match"
#             )
class UserForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = UserCreationForm.Meta.fields + ('first_name', 'last_name', 'email', 'mobile', 'place')

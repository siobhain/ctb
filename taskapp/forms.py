from django import forms
from django.core.validators import RegexValidator
from allauth.account.forms import SignupForm
from .models import Task, Profile


class CustomSignupForm(SignupForm):
    ROI = [('083', '083'), ('085', '085'), ('086', '086'), ('087', '087')]
    firstname = forms.CharField(max_length=15, required=True)
    surname = forms.CharField(max_length=15, required=True)
    mobile_prefix = forms.ChoiceField(choices=ROI, required=True)
    mobile_number = forms.CharField(max_length=7, required=True, validators=[RegexValidator(regex='^\d{7}$', message='Mobile needs 7 digits please')])
 
    def save(self, request):
        # self.fields.pop('email')
        user = super(CustomSignupForm, self).save(request)
        user_profile = Profile.objects.create(
            user=user,
            firstname=self.cleaned_data['firstname'],
            surname=self.cleaned_data['surname'],
            mobile_prefix=self.cleaned_data['mobile_prefix'],
            mobile_number=self.cleaned_data['mobile_number'],
         )
        user_profile.save()
        return user

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ('category', 'description', 'completed')
        help_texts = {
            'category': ('Please choose category most related to Task'),
            'description': ('Max 120 characters & Remember as you create this task - only you can delete this task')
            }
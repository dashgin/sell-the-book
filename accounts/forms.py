from allauth.account.forms import SignupForm
from django import forms
from django.utils.translation import ugettext_lazy as _


class CustomSignupForm(SignupForm):
    full_name = forms.CharField(max_length=50, label=_('field'),
                                widget=forms.TextInput(
                                    attrs={"placeholder": _('Full name'),
                                           'autocomplete': 'name', }
                                ), )

    def save(self, request):
        user = super(CustomSignupForm, self).save(request)
        user.full_name = self.cleaned_data['full_name']
        user.save()
        return user

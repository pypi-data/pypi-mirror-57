from django.contrib.auth import get_user_model

from django_registration.forms import RegistrationForm
from djangoldp_account.models import LDPUser


class LDPUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = get_user_model()

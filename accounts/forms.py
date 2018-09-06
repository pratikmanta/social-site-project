from django.forms import ModelForm
from accounts.models import UserProfile

class UserProfileForm(ModelForm):

    class Meta:
        model = UserProfile
        fields = ('bio','company','school','college','image')

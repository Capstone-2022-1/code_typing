# profileapp/forms.py에서 수작업으로 다시 적어줄 수 있으나,
# ModelForm을 상속하고, Profile Model을 적용하여 fileds=[ ~ ]만으로 Form을 간단하게 만들어 줄 수 있다.

from django.forms import ModelForm
from profileapp.models import Profile


class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['m_emoticon', 'user_nick']
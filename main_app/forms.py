from django.forms import ModelForm
from .models import *

class WidgetForm(ModelForm):
    class Meta:
        model = Widget
        fields = "__all__"
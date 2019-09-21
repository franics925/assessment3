from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm

# Create your views here.


def home(request):
    widget_list = Widget.objects.all()
    form = WidgetForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = WidgetForm()
    return render(request, 'home.html', {'form': form, 'widget_list': widget_list})
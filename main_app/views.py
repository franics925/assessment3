from django.shortcuts import render, redirect
from .models import Widget
from .forms import WidgetForm


def home(request):
    widget_list = Widget.objects.all()
    form = WidgetForm(request.POST)
    if form.is_valid():
        form.save()
        return redirect('home')
    else:
        form = WidgetForm()
    return render(request, 'home.html', {'form': form, 'widget_list': widget_list})

def delete(request, widget_id):
    widget =  Widget.objects.get(id= widget_id)
    widget.delete()
    return redirect('home')
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import ShowForm


@login_required
def create_show(request):
    if request.method == 'POST':
        form = ShowForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage:homepage')
    else:
        form = ShowForm()
    return render(request, 'plays/create_show.html', {'form': form})
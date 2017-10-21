from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import StudentLoginForm


def index(request):
    return render(request, 'classes/index.html')


def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            # do stuff
            return HttpResponseRedirect('')
    else:
        form = StudentLoginForm()

    return render(request, 'classes/student_login.html', context={'form':form})


def student_waiting(request):
    pass
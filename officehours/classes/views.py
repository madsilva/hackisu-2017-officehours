from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import DetailView

from .forms import StudentLoginForm
from .models import Question, Student, Session


def index(request):
    return render(request, 'classes/index.html')


def student_login(request):
    if request.method == 'POST':
        form = StudentLoginForm(request.POST)
        if form.is_valid():
            student = Student.objects.get(canvas_id=form.cleaned_data['canvas_id'])
            session = Session.objects.get(password=form.cleaned_data['session_password'])
            question = Question.objects.create(text=form.cleaned_data['question'], student=student, session=session)
            student.times_signed_in_to_session += 1
            student.save()
            question.save()
            return HttpResponseRedirect('/waiting')
    else:
        form = StudentLoginForm()

    return render(request, 'classes/student_login.html', context={'form':form})


def student_waiting(request):
    return render(request, 'classes/student_waiting.html')


class SessionDetailView(DetailView):
    model = Session
    template_name = 'classes/session_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SessionDetailView, self).get_context_data(**kwargs)
        context['question_list'] = Question.objects.filter(session=self.object, status='waiting').order_by('time_asked')
        context['range'] = range(1, len(context['question_list']))
        return context

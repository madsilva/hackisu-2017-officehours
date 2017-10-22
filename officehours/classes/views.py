from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, DeleteView

from .forms import StudentLoginForm, CreateSessionForm
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


def ta_dashboard(request):
    current_user = request.user
    if current_user is None:
        pass
    context = {}
    sessions = Session.objects.filter(owned_by=current_user)
    if sessions.count() != 0:
        context['session_exists'] = 'true'
        context['session'] = Session.objects.get(owned_by=current_user)
        context['question_list'] = Question.objects.filter(session=context['session']).all()

    return render(request, 'classes/ta_dashboard.html', context)


def create_session(request):
    if request.method == 'POST':
        form = CreateSessionForm(request.POST)
        if form.is_valid():
            session = Session.objects.create(owned_by=request.user, password=form.cleaned_data['session_password'])
            session.save()
            return HttpResponseRedirect('/ta_dashboard')
    else:
        form = CreateSessionForm()

    return render(request, 'classes/create_session.html', context={'form': form})


def student_waiting(request):
    return render(request, 'classes/student_waiting.html')


class SessionDetailView(DetailView):
    model = Session
    template_name = 'classes/session_detail.html'

    def get_context_data(self, **kwargs):
        context = super(SessionDetailView, self).get_context_data(**kwargs)
        statuses = ['waiting', 'working']
        context['question_list'] = Question.objects.filter(session=self.object, status__in=statuses).order_by('time_asked')
        context['range'] = range(1, len(context['question_list']))
        return context


class SessionDeleteView(DeleteView):
    model = Session
    success_url = reverse_lazy('ta_dashboard')
    template_name = 'classes/session_delete.html'

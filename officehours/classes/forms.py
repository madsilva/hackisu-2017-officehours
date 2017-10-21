from django import forms

from .models import Student, Session, Question

class StudentLoginForm(forms.Form):
    canvas_id = forms.CharField()
    session_password = forms.CharField()
    question = forms.CharField()

    def is_valid(self):
        valid = super(StudentLoginForm, self).is_valid()
        if not valid:
            return valid

        try:
            student = Student.objects.get(canvas_id=self.cleaned_data['canvas_id'])
        except Student.DoesNotExist:
            self.errors['no_student'] = 'Invalid Canvas ID'
            valid = False

        try:
            session = Session.objects.get(password=self.cleaned_data['session_password'])
        except Session.DoesNotExist:
            self.errors['no_session'] = 'Invalid session password'
            valid = False

        if valid:
            existing_question = Question.objects.filter(student=student, session=session).all()
            if len(existing_question) != 0:
                self.errors['question_already_asked'] = 'This student already has a question for this session.'
                valid = False

        return valid

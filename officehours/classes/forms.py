from django import forms


class StudentLoginForm(forms.Form):
    canvas_id = forms.CharField()
    session_password = forms.CharField()
    question = forms.CharField()

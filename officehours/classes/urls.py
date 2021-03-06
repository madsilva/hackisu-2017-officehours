"""officehours URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^student_login$', views.student_login, name='student_login'),
    url(r'^waiting$', views.student_waiting, name='student_waiting'),
    url(r'^session/(?P<pk>[0-9]+)', views.SessionDetailView.as_view(), name='session_detail_view'),
    url(r'^ta_dashboard$', views.ta_dashboard, name='ta_dashboard'),
    url(r'^create_session$', views.create_session, name='create_session'),
    url(r'^delete_session/(?P<pk>[0-9]+)', views.SessionDeleteView.as_view(), name='delete_session'),
    url(r'^change_question_status', views.change_question_status, name='change_question_staus'),
]

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    # signup page
    url(r'^signup', views.SignUp.as_view(), name='signup'),
    # used to handle form submit on signup page
    url(r'^signup/submit', views.signup_submit, name='signup_submit'),

]

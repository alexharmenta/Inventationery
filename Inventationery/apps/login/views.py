#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Alex
# @Date:   2015-12-29 23:06:33
# @Last Modified by:   Alex
# @Last Modified time: 2015-12-29 23:10:27
from django.views.generic import FormView
from django.contrib.auth import authenticate, login
from .forms import LoginForm

# Create your views here.


class LoginView(FormView):
    form_class = LoginForm
    template_name = 'Login/login.html'
    success_url = '/'

    def form_valid(self, form):
        user = authenticate(username=form.cleaned_data[
                            'username'],
                            password=form.cleaned_data['password'])
        if user is not None:
            if user.is_active:
                login(self.request, user)
        return super(LoginView, self).form_valid(form)

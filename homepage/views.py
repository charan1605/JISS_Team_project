#views
from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.template import loader
from django.views import View
from django.views.generic import View
from django.views.generic.list import ListView
from django.utils import timezone
from .forms import getregistrar,getlawyer,getjudge
from .models import registrar,judge,lawyer

def home(request): 
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def about(request):
    template = loader.get_template('about.html')
    return HttpResponse(template.render())

def help(request):
    template = loader.get_template('help.html')
    return HttpResponse(template.render())


def login(request):
    return render(request,"homepage/3signin_form.html")


class lawyerlogin(View):
    form_class = getlawyer
    template_name = 'homepage/lawyerlogin.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            users = lawyer.objects.filter(password = password,username = username)
            for user in users:
               template = template = loader.get_template('lawyer.html')
               return HttpResponse(template.render())
                
        return render(request, self.template_name, {'form': form})

        
class judgelogin(View):
    form_class = getjudge
    template_name = 'homepage/judgelogin.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            users = judge.objects.filter(password = password,username = username)
            for user in users:
              template = template = loader.get_template('judge.html')
              return HttpResponse(template.render())
                
        return render(request, self.template_name, {'form': form})


class registrarlogin(View):
    form_class = getregistrar
    template_name = 'homepage/registrarlogin.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            users = registrar.objects.filter(password = password,username = username)
            for user in users :
              template = template = loader.get_template('registrar.html')
              return HttpResponse(template.render())
                
        return render(request, self.template_name, {'form': form})

from django.urls import path
from . import views

urlpatterns = [
   path('',views.home,name = "home"),
   path('about/',views.about,name ="about"), 
   path('help/',views.help,name="help"),
   path('login/',views.login, name="login"),
   path('lawyer_login/',views.lawyerlogin.as_view(),name="lawyerlogin"),
   path('judge_login/',views.judgelogin.as_view(),name="judgelogin"),
   path('registrar_login/',views.registrarlogin.as_view(),name="registrarlogin")
]

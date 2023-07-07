from django.urls import path
from . import views

urlpatterns = [
    path('',views.judge,name = "judge"),
    path('pastcase/',views.pastcase.as_view(), name = "resolved cases")
]
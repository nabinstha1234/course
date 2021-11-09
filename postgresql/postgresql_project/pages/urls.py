#pages/urls.py

from django.urls import  path

from .views import HomePageView,view_pdf

urlpatterns = [
    path('',HomePageView.as_view(), name="home"),
    path('export/',view_pdf,name="export-pdf")
]
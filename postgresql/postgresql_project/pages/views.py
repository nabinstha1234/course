from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.


class HomePageView(TemplateView):
    template_name = 'home.html'

def view_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Desposition'] = 'attachement; filename=Expenses'+str(datetime.datetime.now())+'.pdf'
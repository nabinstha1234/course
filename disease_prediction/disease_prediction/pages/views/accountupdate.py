from django.views.generic import TemplateView


class AccountUpdateView(TemplateView):
    template_name = 'pages/accountupdate.html'
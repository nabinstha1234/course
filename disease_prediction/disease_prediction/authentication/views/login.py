from django.conf import settings
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages


class CustomLoginView(LoginView):
    template_name = 'authentication/login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['retailer_trackly_oauth_url'] = settings.CORE_TRACKFLY_OAUTH_LOGIN_URL
        return context

    def post(self, request, *args, **kwargs):
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return redirect('dashboard:dashboard')
            else:
                messages.error(request, "Can't login! The user is not active!")
                messages.error(request, 'User Is Not Active!')
        else:
            messages.error(request, 'Cannot Authenticate with Given credentials')

        return self.render_to_response(self.get_context_data())

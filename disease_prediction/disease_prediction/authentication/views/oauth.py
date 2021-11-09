import requests
from django.conf import settings
from django.contrib.auth import get_user_model
from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import redirect


def trackfly_oauth_callback(request):
    code = request.GET.get('code')
    if not code:
        # sample error format
        # ?error=invalid_request&error_description=Invalid+or+missing+response+type
        error_msg_or_default_error_msg = request.GET.get('error_description', 'Error occurred')
        return HttpResponse(error_msg_or_default_error_msg)

    response = requests.post(
        settings.CORE_TRACKFLY_OAUTH_TOKEN_URL,
        data={
            'grant_type': 'authorization_code',
            'client_id': settings.CORE_TRACKFLY_OAUTH_CLIENT_ID,
            'client_secret': settings.CORE_TRACKFLY_OAUTH_CLIENT_SECRET,
            'code': code
        }
    )
    if response.status_code != 200:
        return HttpResponse('Please try back later.Could\'t login')

    data = response.json()

    response = requests.get(
        settings.CORE_TRACKFLY_OAUTH_USER_INFO_URL,
        params={
            'access_token': data['access_token']
        }
    )
    if response.status_code != 200:
        return HttpResponse("Couldn't Fetch User Info")
    data = response.json()
    user, _ = get_user_model().objects.update_or_create(
        email=data['user_email'],
        defaults={
            'first_name': data['display_name'].split()[0],
            'last_name': "".join(data['display_name'].split()[1:]),
            'is_active': True,
        }
    )

    login(request, user)

    return redirect('dashboard:dashboard')

from django.shortcuts import render,redirect
from disease_prediction.user.models import User,UserProfile
from django.views.generic.edit import UpdateView
from disease_prediction.authentication.forms import UserProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



class BusinessDetailUpdateView(UpdateView):
    def get(self, request, id):
        user = User.objects.get(id=id)
        user_profile = UserProfile.objects.filter(user_id=user.id).first()
        return render(request, 'pages/businessdetailupdate.html', {
            'user': user,
            'user_profile': user_profile
        })
    def post(self, request,id):
        user = User.objects.get(id=id)
        user_profile = UserProfile.objects.filter(user_id=user.id).first()
        form = UserProfileUpdateForm(request.POST, instance=user_profile)
        if form.is_valid():
            user_profile = form.save()
            user_profile.user_status = request.POST.get('user_status')
            user_profile.save()
        messages.success(request, 'Business Detail was updated successfully!')
        return render(request, 'pages/businessdetailupdate.html', {'user': user, 'user_profile': user_profile})


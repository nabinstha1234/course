from django.shortcuts import render,redirect
from disease_prediction.user.models import User
from disease_prediction.authentication.forms import UserUpdateForm
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin

class ProfileUpdateView(UpdateView):
    def get(self, request,id):
        user = User.objects.get(id=id)
        return render(request, 'pages/profileupdate.html',{'user':user})

    def post(self, request,id):
        print(request)
        context ={}
        user = User.objects.get(id=id)
        current = request.POST['old_password']
        new_password = request.POST['new_password1']
        check = user.check_password(current)
        print(check)
        form = UserUpdateForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
        if current:
            if check==True:
                print("suresh")
                user.set_password(new_password)
                user.save()
        messages.success(request, 'User was updated successfully!')
        return render(request, 'pages/profileupdate.html',{'user':user, 'context':context})
from django.shortcuts import render,redirect
from disease_prediction.user.models import User,UserProfile,Country,State
from disease_prediction.authentication.forms import UserProfileUpdateForm, ShippingAddressForm
from django.contrib import messages
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


class BillingAddressView(UpdateView):
    def get(self,request,id):
        user = User.objects.get(id=id)
        user_profile = UserProfile.objects.filter(user_id=user.id).first()
        countries = Country.objects.all()
        country = Country.objects.filter(id=user_profile.country_id).first()
        states = State.objects.filter(country_id=country.id)
        return render(request, 'pages//billingdetail.html', {
            'user': user,
            'user_profile':user_profile,
            'countries':countries,
            'states':states
        })

    def post(self, request, id):
        user = User.objects.get(id=id)
        user_profile = UserProfile.objects.filter(user_id=user.id).first()
        countries = Country.objects.all()
        states = State.objects.all()
        form = UserProfileUpdateForm(request.POST, instance=user_profile)
        print(request.POST.get('country'))
        if request.POST.get('state'):
            state_id = request.POST.get('state')
            state = State.objects.get(id=state_id)
            state_name = state.name
        else:
            state_name = request.POST.get('state_name')
        if form.is_valid():
            user_profile = form.save()
            user_profile.country_id = request.POST.get('country')
            user_profile.apartment = request.POST.get('apartment')
            user_profile.state_id = request.POST.get('state')
            user_profile.state_name = state_name

            user_profile.save()
        messages.success(request, 'Billing Address was updated successfully!')
        return render(request, 'pages/billingdetail.html', {
            'user': user,
            'user_profile': user_profile,
            'countries':countries,
            'states':states})


class ShippingAddressView(UpdateView):
    def get(self, request,id):
        user = User.objects.get(id=id)
        shipping_address = ShippingAddress.objects.filter(user_id=user.id).first()
        country = Country.objects.filter(id=shipping_address.country_id).first()
        countries = Country.objects.all()
        states = State.objects.filter(country_id = country.id)
        return render(request, 'pages//shippingaddress.html', {
            'user': user,
            'shipping_address': shipping_address,
            'countries': countries,
            'states': states
        })

    def post(self, request, id):
        user = User.objects.get(id=id)
        shipping_address = ShippingAddress.objects.filter(user_id=user.id).first()
        countries = Country.objects.all()
        states = State.objects.all()
        form = ShippingAddressForm(request.POST, instance=shipping_address)
        if request.POST.get('state'):
            state_id = request.POST.get('state')
            state = State.objects.get(id=state_id)
            state_name = state.name
        else:
            state_name = request.POST.get('state_name')
        if form.is_valid():
            shipping_address = form.save()
            shipping_address.country_id = request.POST.get('country')
            shipping_address.state_id = request.POST.get('state')
            shipping_address.state_name = state_name

            shipping_address.save()
        messages.success(request, 'Shipping Address was updated successfully!')
        return render(request, 'pages/shippingaddress.html', {
            'user': user,
            'shipping_address': shipping_address,
            'countries': countries,
            'states': states})
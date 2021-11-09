from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render,redirect
from disease_prediction.authentication import utils
from disease_prediction.authentication.forms import UserRegistrationForm
from disease_prediction.user.models import Country,State,User,UserProfile
from django.http import JsonResponse
from django.views.generic import TemplateView
from django.contrib import messages


class RegistrationView(SuccessMessageMixin, CreateView):
  def get(self, request):
    countries = Country.objects.all()
    return render(request, 'authentication/register.html', {'countries': countries})

  def post(self,request):
    form =UserRegistrationForm(request.POST or None)
    print(form.is_valid())
    if form.is_valid():
      user = form.save(commit=False)
      user.is_active =1
      user.save()

      if user:
        userprofile = UserProfile.objects.create(
          user_id=user.id,
          b_firstname= request.POST.get('first_name'),
          b_lastname= request.POST.get('last_name'),
          country_id = request.POST.get('country'),
          state_id = request.POST.get('state'),
          city = request.POST.get('city'),
          phone = request.POST.get('phone'),
          zip = request.POST.get('zip'),
          store_name = request.POST.get('company'),
          address = request.POST.get('address'),
          user_status = request.POST.get('status')
        )
        userprofile.save()
        shippingAddress = ShippingAddress.objects.create(
          user_id=user.id,
          first_name=request.POST.get('first_name'),
          last_name = request.POST.get('last_name'),
          country_id = request.POST.get('country'),
          state_id = request.POST.get('state'),
          city = request.POST.get('city'),
          phone = request.POST.get('phone'),
          zip = request.POST.get('zip'),
          store_name = request.POST.get('company'),
          address = request.POST.get('address'),
        )
        messages.success(request, 'User was created successfully!')
        return redirect('authentication:login')
    else:
      print(form.errors)
    return render(request, 'authentication/login.html')



  # success_message = "Your profile was created successfully!"

  def send_email(self):
    # send email using the self.cleaned_data dictionary
    context = {'name': self.cleaned_data.get('first_name')}
    utils.mail_sender(
      template='emails/welcome_email.html',
      context=context,
      subject="Reset Password",
      recipient_list=[self.cleaned_data.get('email')]
    )
    pass

  # def form_valid(self, form):
  #   # This method is called when valid form data has been POSTed.
  #   # It should return an HttpResponse.
  #   self.send_email()
  #   return super().form_valid(form)


class StateJsonView(TemplateView):
  def get(self, request):
    country_id = request.GET['country']
    country = Country.objects.get(id = country_id)
    states = State.objects.filter(country_code=country.iso2).values('id','name')
    return JsonResponse({'states':list(states)})

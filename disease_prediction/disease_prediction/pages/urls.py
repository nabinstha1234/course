from django.urls import path

from disease_prediction.pages.views.home import HomeView
from disease_prediction.pages.views.profileupdate import ProfileUpdateView
from disease_prediction.pages.views.businessdetailupdate import BusinessDetailUpdateView
from disease_prediction.pages.views.address import BillingAddressView, ShippingAddressView
# from trackfly.pages.views.accountupdate import AccountUpdateView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('profile-update/<int:id>', ProfileUpdateView.as_view(), name='profile-update'),
    path('business-detail/<int:id>', BusinessDetailUpdateView.as_view(), name='business-detail'),
    path('billing-address/<int:id>', BillingAddressView.as_view(), name='billing-address'),
    path('shipping-address/<int:id>', ShippingAddressView.as_view(), name='shipping-address')
    # path('account-update/', AccountUpdateView.as_view(), name='account-update')
]
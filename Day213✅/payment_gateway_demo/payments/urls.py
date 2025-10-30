from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),

    # Stripe
    path("stripe/create-checkout-session/", views.create_checkout_session, name="stripe_checkout"),
    path("stripe/success/", views.stripe_success, name="stripe_success"),
    path("stripe/cancel/", views.stripe_cancel, name="stripe_cancel"),

    # Razorpay
    path("razorpay/order/", views.create_razorpay_order, name="razorpay_order"),
    path("razorpay/handler/", views.razorpay_payment_handler, name="razorpay_handler"),
]

import stripe
import razorpay
from django.conf import settings
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt

# ====== HOME ======
def home(request):
    return render(request, "payments/home.html")


# ====== STRIPE ======
stripe.api_key = settings.STRIPE_SECRET_KEY

def create_checkout_session(request):
    session = stripe.checkout.Session.create(
        payment_method_types=["card"],
        line_items=[{
            "price_data": {
                "currency": "usd",
                "product_data": {"name": "Django Course"},
                "unit_amount": 1000 * 100,  # $100
            },
            "quantity": 1,
        }],
        mode="payment",
        success_url=request.build_absolute_uri("/stripe/success/"),
        cancel_url=request.build_absolute_uri("/stripe/cancel/"),
    )
    return JsonResponse({"id": session.id, "publicKey": settings.STRIPE_PUBLISHABLE_KEY})


def stripe_success(request):
    return render(request, "payments/stripe_checkout.html", {"status": "success"})


def stripe_cancel(request):
    return render(request, "payments/stripe_checkout.html", {"status": "cancel"})


# ====== RAZORPAY ======
client = razorpay.Client(auth=(settings.RAZORPAY_KEY_ID, settings.RAZORPAY_KEY_SECRET))

def create_razorpay_order(request):
    order = client.order.create({
        "amount": 50000,  # Rs 500
        "currency": "INR",
        "payment_capture": "1"
    })
    return render(request, "payments/razorpay_checkout.html", {
        "order_id": order["id"],
        "amount": order["amount"],
        "key_id": settings.RAZORPAY_KEY_ID,
    })


@csrf_exempt
def razorpay_payment_handler(request):
    if request.method == "POST":
        params = {
            "razorpay_order_id": request.POST.get("razorpay_order_id"),
            "razorpay_payment_id": request.POST.get("razorpay_payment_id"),
            "razorpay_signature": request.POST.get("razorpay_signature"),
        }
        try:
            client.utility.verify_payment_signature(params)
        except:
            return HttpResponseBadRequest("Signature verification failed")

        return JsonResponse({"status": "Payment Success"})
    return HttpResponseBadRequest("Only POST allowed")

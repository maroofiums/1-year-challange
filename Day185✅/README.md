# Day 185

Thik hai bhai 🔥
Main tumhe **Stripe + Razorpay** dono ka **full Django project sample code** bana ke dikhata hoon. Isme tumhare paas ready-to-run boilerplate hoga.

---

# 📦 Project Structure

```
payment_gateway_demo/
│
├── manage.py
├── requirements.txt
├── payment_gateway_demo/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
│
└── payments/
    ├── __init__.py
    ├── views.py
    ├── urls.py
    └── templates/
        └── payments/
            ├── home.html
            ├── stripe_checkout.html
            └── razorpay_checkout.html
```

---

# ⚙️ requirements.txt

```txt
Django>=4.2
stripe
razorpay
python-dotenv
```

---

# ⚙️ settings.py (important parts)

```python
import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

SECRET_KEY = "django-insecure-test"  # change for production
DEBUG = True
ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "payments",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "payment_gateway_demo.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "payment_gateway_demo.wsgi.application"

# Static files
STATIC_URL = "static/"

# Payment keys
STRIPE_PUBLISHABLE_KEY = os.getenv("STRIPE_PUBLISHABLE_KEY")
STRIPE_SECRET_KEY = os.getenv("STRIPE_SECRET_KEY")
RAZORPAY_KEY_ID = os.getenv("RAZORPAY_KEY_ID")
RAZORPAY_KEY_SECRET = os.getenv("RAZORPAY_KEY_SECRET")
```

---

# ⚙️ urls.py (project level)

```python
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("payments.urls")),
]
```

---

# 📄 payments/urls.py

```python
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
```

---

# 📄 payments/views.py

```python
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
```

---

# 🖼 Templates

### home.html

```html
<h2>Choose Payment Gateway</h2>
<a href="{% url 'stripe_checkout' %}" id="stripe-btn">Pay with Stripe</a> <br><br>
<a href="{% url 'razorpay_order' %}">Pay with Razorpay</a>

<script src="https://js.stripe.com/v3/"></script>
<script>
document.getElementById("stripe-btn").addEventListener("click", function(e){
    e.preventDefault();
    fetch("{% url 'stripe_checkout' %}")
      .then(res => res.json())
      .then(data => {
        const stripe = Stripe(data.publicKey);
        stripe.redirectToCheckout({ sessionId: data.id });
      });
});
</script>
```

---

### stripe_checkout.html

```html
{% if status == "success" %}
<h1>✅ Stripe Payment Successful!</h1>
{% else %}
<h1>❌ Stripe Payment Cancelled</h1>
{% endif %}
<a href="/">Back Home</a>
```

---

### razorpay_checkout.html

```html
<h2>Pay with Razorpay</h2>
<button id="rzp-button">Pay Rs {{ amount|floatformat:-2 }}</button>

<script src="https://checkout.razorpay.com/v1/checkout.js"></script>
<script>
var options = {
    "key": "{{ key_id }}",
    "amount": "{{ amount }}",
    "currency": "INR",
    "order_id": "{{ order_id }}",
    "handler": function (response){
        fetch("{% url 'razorpay_handler' %}", {
            method: "POST",
            headers: { "Content-Type": "application/x-www-form-urlencoded" },
            body: `razorpay_order_id=${response.razorpay_order_id}&razorpay_payment_id=${response.razorpay_payment_id}&razorpay_signature=${response.razorpay_signature}`
        }).then(res => res.json()).then(data => {
            alert("Payment " + data.status);
            window.location.href = "/";
        });
    }
};
var rzp1 = new Razorpay(options);
document.getElementById("rzp-button").onclick = function(e){
    rzp1.open();
    e.preventDefault();
}
</script>
```

---

# 📄 .env (example)

```
STRIPE_PUBLISHABLE_KEY=pk_test_123456
STRIPE_SECRET_KEY=sk_test_123456
RAZORPAY_KEY_ID=rzp_test_123456
RAZORPAY_KEY_SECRET=abc123456
```

---

# 🚀 Run Project

```bash
python -m venv venv
source venv/bin/activate  # windows: venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Visit → [http://127.0.0.1:8000](http://127.0.0.1:8000)

---


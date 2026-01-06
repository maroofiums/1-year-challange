# Day227 — Django + Stripe Payment Integration

This README documents everything I learned while integrating **Stripe payments** into a **Django project** — step by step, including both **backend logic** and **frontend Stripe Elements**.

---

## 🎯 Overview

In this project, I learned how to:

* Connect Django backend with Stripe’s API.
* Securely manage API keys using `.env`.
* Create and manage a **PaymentIntent** from the backend.
* Use **Stripe Elements** on the frontend to collect card info safely.
* Handle common payment validation errors (like “Your card number is incomplete”).
* Test payments using Stripe’s test cards.

---

## ⚙️ Step-by-Step Understanding

### **1️⃣ Installing Stripe SDK**

I learned that to use Stripe in Django, I must install the official SDK:

```bash
pip install stripe
```

Then import and set `stripe.api_key = settings.STRIPE_SECRET_KEY`.

---

### **2️⃣ Understanding API Keys**

Stripe provides:

* **Publishable key** → used on frontend
* **Secret key** → used on backend

I learned to store them safely in `.env` instead of writing them in code.

---

### **3️⃣ Creating PaymentIntent**

PaymentIntent is the “brain” of each transaction.
I learned that it:

* Defines the **amount** and **currency**
* Generates a **client_secret** used on frontend
* Tracks status (`requires_payment_method`, `succeeded`, etc.)

```python
intent = stripe.PaymentIntent.create(
    amount=5000,  # 50 USD
    currency='usd',
    payment_method_types=['card']
)
```

---

### **4️⃣ Passing `client_secret` to Frontend**

Backend sends `client_secret` to the template:

```python
return render(request, "checkout.html", {
    "client_secret": intent.client_secret,
    "stripe_public_key": settings.STRIPE_PUBLIC_KEY
})
```

Frontend uses this `client_secret` to confirm payment.

---

### **5️⃣ Stripe Elements Integration**

Stripe Elements securely handles card details.
I learned that you never directly handle card data in Django.

```javascript
const stripe = Stripe("{{ stripe_public_key }}");
const elements = stripe.elements();
const cardElement = elements.create('card');
cardElement.mount('#card-element');
```

This creates a **secure input field** inside my HTML.

---

### **6️⃣ Confirming the Payment**

After the user enters card details, we confirm payment using:

```javascript
stripe.confirmCardPayment(clientSecret, {
  payment_method: { card: cardElement }
});
```

This communicates directly with Stripe’s servers.

---

### **7️⃣ Handling Errors**

Stripe automatically validates inputs.
I learned common messages like:

* “Your card number is incomplete” → field not fully filled
* “Your card was declined” → test failed card
* “Payment successful!” → means Stripe confirmed the paymentIntent

---

### **8️⃣ Testing Payments**

Stripe provides test cards (e.g. `4242 4242 4242 4242`).
I learned to use them to simulate real transactions safely.

---

## 🧩 Key Takeaways

✅ **Backend:**

* All secure logic (amount, currency, API calls) stays in Django.

✅ **Frontend:**

* Only interacts with Stripe.js and the `client_secret`.

✅ **Security:**

* Never expose secret key.
* Use `.env` for credentials.

✅ **Workflow:**

```
User enters card → Stripe Elements → Stripe API (via client_secret) → PaymentIntent confirms → Django gets success
```

---

## 🚀 Next Goals

* Add **webhooks** for automatic confirmation on backend.
* Save payment info to **database**.
* Create a **success/failure** page.
* Try **subscription-based payments**.

---

## 💬 My Reflection

Before this project, mujhe Stripe thoda complex lagta tha 😅
But ab samajh aaya ke agar backend (Django) aur frontend (Stripe.js) dono ka flow samjho, to integration simple hai.
The most important part: **`client_secret` must come from backend** — warna paymentIntent error milta hai.

---

## 🧾 Summary Tip

> "Stripe is powerful, but never let frontend handle sensitive logic.
> Django = secure brain, Stripe = payment muscle." 💪

---
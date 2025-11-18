from django.shortcuts import render,redirect
from .models import productinfo, offerinfo
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# Create your views here.
def index(request):
    offerproducts = offerinfo.objects.all()
    context = {
        'offerproducts': offerproducts,
    }
    return render(request, 'index.html', context)

def Store(request):
    products = productinfo.objects.all()
    context = {
        'products': products,
    }
    
    return render(request, 'store.html', context)

def login_page(request):
    return render(request, 'login.html')

def signup_page(request):
    return render(request, 'signup.html')

def productenquire(request, product_id):
    product = productinfo.objects.get(id=product_id)

    phone = "9551566406"   # owner number
    message = f"I want to buy: {product.name}\nPrice: {product.price}\nID: {product.id}"

    context = {
        'product': product,
        'phone_number': phone,
        'message': message,
    }
    return render(request, "store.html", context)

def contact(request):
    if request.method == "POST":
        first = request.POST.get("first_name")
        last = request.POST.get("last_name")
        email = request.POST.get("email")
        subject = request.POST.get("subject")
        message = request.POST.get("message")

        full_message = f"""
        Name: {first} {last}
        Email: {email}
        Subject: {subject}

        Message:
        {message}
        """

        send_mail(
            subject=f"New Contact Form Message: {subject}",
            message=full_message,
            from_email=email,  
            recipient_list=["kreativ2214@gmail.com"],
        )

        return render(request, "contact.html", {
            "success": "Your message has been sent successfully!"
        })

    return render(request, "contact.html")

# def signup_page(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         email = request.POST.get("email")
#         password = request.POST.get("password")

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already exists!")
#             return redirect('signup')

#         user = User.objects.create_user(username=username, email=email, password=password)
#         user.save()

#         messages.success(request, "Account created successfully! Please log in.")
#         return redirect('login')

#     return render(request, "signup.html")

# def login_page(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")

#         user = authenticate(request, username=username, password=password)

#         if user is not None:
#             login(request, user)
#             return redirect('index')  # redirect to home page
#         else:
#             messages.error(request, "Invalid username or password.")
#             return redirect('login')

#     return render(request, "login.html")

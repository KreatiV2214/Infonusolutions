from django.shortcuts import render, redirect
from .models import productinfo, offerinfo, Category
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404


# HOME PAGE
def index(request):
    offerproducts = offerinfo.objects.all()
    categories = Category.objects.all()   # for navbar dropdown
    context = {
        'offerproducts': offerproducts,
        'categories': categories,
    }
    return render(request, 'index.html', context)


# STORE PAGE (with category filter + dropdown)
def Store(request):
    category_slug = request.GET.get('category')
    categories = Category.objects.all()

    if category_slug:
        products = productinfo.objects.filter(category__slug=category_slug)
    else:
        products = productinfo.objects.all()

    context = {
        'products': products,
        'categories': categories,
        'selected_category': category_slug,
    }
    return render(request, 'store.html', context)


# PRODUCT ENQUIRY (WhatsApp link data)
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


# CONTACT PAGE
def contact(request):
    categories = Category.objects.all()   # for navbar dropdown

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
            "success": "Your message has been sent successfully!",
            "categories": categories,   # keep dropdown after form submit
        })

    return render(request, "contact.html", {"categories": categories})

def product_detail(request, product_id):
    product = get_object_or_404(productinfo, id=product_id)
    categories = Category.objects.all()   # for navbar dropdown, if needed

    # WhatsApp message text (URL encoded \n -> %0A)
    whatsapp_link = (
        f"https://wa.me/9551566406"
        f"?text=Hi! I'm interested in this product!!"
        f"%0AName: {product.name}"
        f"%0APrice: ₹{product.price}"
        f"%0ADescription: {product.description}"
    )

    context = {
        'product': product,
        'categories': categories,
        'whatsapp_link': whatsapp_link,
    }
    return render(request, 'product_detail.html', context)
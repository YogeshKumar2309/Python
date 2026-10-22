
from django.shortcuts import render, redirect
from django.contrib import messages


PRODUCTS = [
    {
        "name": "Wireless Keyboard",
        "category": "Accessories",
        "description": "A compact keyboard for everyday work and study.",
        "price": "Check latest price",
        "image": "",
        "url": "",
    },
    {
        "name": "USB-C Hub",
        "category": "Computer Accessories",
        "description": "Explore connectivity options for your laptop.",
        "price": "Check latest price",
        "image": "",
        "url": "",
    },
    {
        "name": "Laptop Stand",
        "category": "Workspace",
        "description": "Compare laptop stands for a more organised desk.",
        "price": "Check latest price",
        "image": "",
        "url": "",
    },
]


def home(request):
    return render(request, "core/home.html", {
        "products": PRODUCTS,
    })


def products(request):
    return render(request, "core/products.html", {
        "products": PRODUCTS,
    })


def about(request):
    return render(request, "core/about.html")


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "").strip()
        email = request.POST.get("email", "").strip()
        message = request.POST.get("message", "").strip()

        if not name or not email or not message:
            messages.error(request, "Please complete all fields.")
        else:
            # Connect email sending or database storage here.
            messages.success(
                request,
                "Your form was submitted. Email delivery is not configured yet."
            )
            return redirect("contact")

    return render(request, "core/contact.html")


def privacy(request):
    return render(request, "core/privacy.html")


def disclaimer(request):
    return render(request, "core/disclaimer.html")


def terms(request):
    return render(request, "core/terms.html")

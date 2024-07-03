# Django imports
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.conf import settings

# App imports
from .utilities import get_data, subscribe
from .models import Bitcoin


def index(request):
    """
    Handle the request for the index page.
    If the request method is POST, subscribe the user to the mailing list.
    Otherwise, fetch the Bitcoin data and render the index page.
    
    Args:
        request (HttpRequest): The request object used to generate the response.

    Returns:
        HttpResponse: The rendered index page with Bitcoin data.
    """
    
    if request.method == "POST":
        # Extract email from the POST request and subscribe the user
        email = request.POST.get('email')
        subscribe(email)   
        # Display a success message to the user
        messages.success(request, "Thank you for your email. ") 
        # Redirect the user to the success page
        return redirect('success')

    # Fetch the latest Bitcoin data
    get_data()
    # Retrieve the Bitcoin instance from the database
    bitcoin = get_object_or_404(Bitcoin, title='btc-usd')
    # Render the index page with Bitcoin data
    return render(request, 'index.html', {'bitcoin': bitcoin})

def success(request):
    """
    Handle the request for the success page.
    
    Args:
        request (HttpRequest): The request object used to generate the response.

    Returns:
        HttpResponse: The rendered success page.
    """
    return render(request, 'success.html')

def page_not_found(response, exception):
    """
    Custom 404 error handler.
    Render the 404 error page when a page is not found.
    
    Args:
        response (HttpResponse): The response object used to generate the error page.
        exception (Exception): The exception that was raised.

    Returns:
        HttpResponse: The rendered 404 error page.
    """
    
    return render(response, '404.html')

def server_error(response):
    """
    Custom 500 error handler.
    Render the 500 error page when a server error occurs.
    
    Args:
        response (HttpResponse): The response object used to generate the error page.

    Returns:
        HttpResponse: The rendered 500 error page.
    """
    
    return render(response, '500.html')







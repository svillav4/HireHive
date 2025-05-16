import requests
from django.shortcuts import render

def external_products_view(request):
    api_url = 'http://52.55.166.15:8000/api/products/'

    try:
        response = requests.get(api_url, timeout=5)
        response.raise_for_status()
        products = response.json()
    except requests.RequestException as e:
        print(f"Error fetching products: {e}")
        products = []

    return render(request, 'external_products.html', {'products': products})

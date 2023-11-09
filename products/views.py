from django.shortcuts import render
import json
from products.models import Product


def index(request):
    context = {
        'object_list': Product.objects.all(),
        'title': 'Товары'
    }
    return render(request, 'products/index.html', context)


def about_product(request, pk):
    context = {
        'object': Product.objects.get(id=pk),
        'title': 'О товаре'
    }
    return render(request, 'products/products.html', context)


def main(request):
    context = {
        'object_list': Product.objects.all()[:3],
        'title': 'Главная'
    }
    return render(request, 'products/main.html', context)


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        to_json = {'name': name,
                   'phone': phone,
                   'message': message}
        print(f'{name} ({phone}): {message}')
        try:
            with open("contacts_data.json", "r", encoding="utf-8") as json_file:
                content = json.load(json_file)
                content.append(to_json)
            with open("contacts_data.json", "w", encoding="utf-8") as json_file:
                json.dump(content, json_file, ensure_ascii=False, indent=2)
        except FileNotFoundError:
            with open("contacts_data.json", "w") as json_file:
                content = [to_json]
                json.dump(content, json_file)
    context = {
        'title': 'Контакты'
    }
    return render(request, 'products/contacts.html', context)

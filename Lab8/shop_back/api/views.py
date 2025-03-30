import json
from django.http import JsonResponse
from django.views import View
from .models import Product, Category

class ProductListView(View):
    def get(self, request):
        products = list(Product.objects.values())
        return JsonResponse(products, safe=False)

class ProductDetailView(View):
    def get(self, request, id):
        try:
            product = Product.objects.get(id=id)
            return JsonResponse({
                "id": product.id,
                "name": product.name,
                "price": product.price,
                "description": product.description,
                "count": product.count,
                "is_active": product.is_active,
                "category": product.category.id,
            })
        except Product.DoesNotExist:
            return JsonResponse({"error": "Product not found"}, status=404)

class CategoryListView(View):
    def get(self, request):
        categories = list(Category.objects.values())
        return JsonResponse(categories, safe=False)

class CategoryDetailView(View):
    def get(self, request, id):
        try:
            category = Category.objects.get(id=id)
            return JsonResponse({"id": category.id, "name": category.name})
        except Category.DoesNotExist:
            return JsonResponse({"error": "Category not found"}, status=404)

class ProductsByCategoryView(View):
    def get(self, request, id):
        products = list(Product.objects.filter(category_id=id).values())
        return JsonResponse(products, safe=False)

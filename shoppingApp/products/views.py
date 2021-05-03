from django.shortcuts import render
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from .models import Post, Categories
from .forms import PostForm, UpdateForm, NewCategoryForm
from django.urls import reverse_lazy

# Create your views here.


class HomeView(TemplateView):
    model = Post
    template_name = 'home.html'


class ProductsListView(ListView):
    model = Post
    template_name = 'products.html'  # Page to render all the Products(list the Product).
    # ordering = ['-publishedDate']
    ordering = ['-id']


class ProductView(DetailView):
    model = Post
    template_name = 'readProduct.html'


class AddNewProductView(CreateView):
    model = Post
    template_name = 'newProduct.html'
    form_class = PostForm


class UpdateProductView(UpdateView):
    model = Post
    template_name = 'updateProduct.html'
    form_class = UpdateForm


class DeleteProductView(DeleteView):
    model = Post
    template_name = 'deleteProduct.html'
    form_class = UpdateForm
    success_url = reverse_lazy('products')


class AddNewCategoryView(CreateView):
    model = Categories
    template_name = 'newCategory.html'
    form_class = NewCategoryForm


def categoryView(request, category):
    categoryPost = Post.objects.filter(category=category.replace('-', ' '))
    return render(
        request, 'category.html', {
            'category': category.title().replace('-', ' '),
            'categoryPost': categoryPost,
        })


def CategoryListView(request):
    categoriesList = Categories.objects.all()
    return render(request, 'categories.html', {'categoryList': categoriesList})

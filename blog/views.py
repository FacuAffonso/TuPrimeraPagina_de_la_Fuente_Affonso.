from django.shortcuts import render, redirect
from .models import Post
from .forms import AuthorForm, CategoryForm, PostForm, SearchForm

def home(request):
    return render(request, 'blog/home.html')

def create_author(request):
    form = AuthorForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save(); return redirect('blog:home')
    return render(request, 'blog/author_form.html', {'form': form})

def create_category(request):
    form = CategoryForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save(); return redirect('blog:home')
    return render(request, 'blog/category_form.html', {'form': form})

def create_post(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save(); return redirect('blog:post_list')
    return render(request, 'blog/post_form.html', {'form': form})

def post_list(request):
    posts = Post.objects.all().order_by('-publicado')
    return render(request, 'blog/post_list.html', {'posts': posts})

def search_posts(request):
    form = SearchForm(request.GET or None)
    posts = Post.objects.none()
    if form.is_valid() and form.cleaned_data['q']:
        posts = Post.objects.filter(titulo__icontains=form.cleaned_data['q'])
    return render(request, 'blog/search.html', {'form': form, 'posts': posts})

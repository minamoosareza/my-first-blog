from django.shortcuts import render
from django.utils import timezone
from django.contrib import messages
from .models import Course, Article, New, Signup, Contact
from django.shortcuts import render, get_object_or_404
from .forms import SignupForm, ContactForm
from django.shortcuts import redirect

def homepage(request):
    courses = Course.objects.filter(is_active = True)
    articles = Article.objects.order_by('-id')[0:3]
    news = New.objects.order_by('-id')[0:4]
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = ContactForm()
	#posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/homepage.html', {'courses':courses, 'articles':articles, 'news':news, 'form' : form}) 
	
def pastcourses_list(request):
    courses = Course.objects.filter(is_active = False)
    return render(request, 'blog/pastcourses_list.html', {'courses' : courses})
	
def current_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'blog/current_course.html', {'course' : course})
	
def signup(request, pk):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            signup = form.save(commit=False)
            signup.course = get_object_or_404(Course, pk=pk)
            signup.save()
            #messages.success(request, 'ثبت نام با موفقیت انجام شد')
            return redirect('signup', pk=pk)
        #else:
            #messages.success(request, 'ثبت نام انجام نشد. لطفا از صحت ورودی‌های خود اطمینان حاصل کنید')
    else:
        form = SignupForm()
        #form.course = get_object_or_404(Course, pk=pk)
    return render(request, 'blog/signup.html', {'form': form})

def past_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'blog/past_course.html', {'course' : course})

def articles_list(request):
    articles = Article.objects.all()
    return render(request, 'blog/articles_list.html', {'articles' : articles})

def article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, 'blog/article.html', {'article' : article})

def news_list(request):
    news = New.objects.order_by('date')
    return render(request, 'blog/news_list.html', {'news' : news})

def new(request, pk):
    new = get_object_or_404(New, pk=pk)
    return render(request, 'blog/new.html', {'new' : new})	
	
	

"""def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
	
def post_new(request):
    form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
	
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})"""
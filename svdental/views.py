from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
from .form import AppoinmentForm
from django.core.mail import send_mail
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    # get home content

    posts = Post.objects.filter(active=True, status=1).exclude(category__name = 'home')

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context=context)


def postDetail(request, pk):
    post = get_object_or_404(Post, pk=pk, active=True, status=1)

    context = {
        'post': post,
    }
    return render(request, "detail.html", context=context)


def postDetailWithSlug(request, slug):
    post = get_object_or_404(Post, slug=slug, active=True, status=1)

    context = {
        'post': post,
    }
    return render(request, "detail.html", context=context)


def getKienThucNhaKhoa(request):
    posts = Post.objects.filter(active=True, status=1)

    print(posts)
    context = {
        'posts': posts,
    }
    return render(request, "list_post.html", context=context)


@login_required
@permission_required('admin', raise_exception=True)
def viewPostDraft(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }

    return render(request, "detail.html", context=context)


def getContact(request):
    return render(request, "contact.html")

def get_post_from_category(request, slug):
    posts = Post.objects.filter(category__name = slug ,active=True, status=1)

    return render(request, 'list_post.html', {'page_obj': posts})


def custom_page_not_found_view(request, exception):
    return render(request, "error_page.html", {})

def custom_error_view(request, exception=None):
    return render(request, "error_page.html", {})

def custom_permission_denied_view(request, exception=None):
    return render(request, "error_page.html", {})

def custom_bad_request_view(request, exception=None):
    return render(request, "error_page.html", {})
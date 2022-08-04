from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Post
from django.contrib.auth.decorators import login_required, permission_required

# home page


def index(request):
    # get home content
    posts = Post.objects.filter(
        active=True, status=1).exclude(category__name='home').order_by("-created_on")[:10]

    context = {
        'posts': posts,
    }

    return render(request, 'index.html', context=context)


# detail pagw
def postDetail(request, pk):
    post = Post.objects.filter(pk=pk, active=True, status=1)
    post_relevant = Post.objects.filter(
        active=True, status=1, category=post.category).order_by("-created_on")[:4]

    context = {
        'post': post,
        'post_relevant': post_relevant,
    }

    return render(request, "detail.html", context=context)

# detail page with slug
def postDetailWithSlug(request, slug):
    # get post detail
    post = get_object_or_404(Post, slug=slug, active=True, status=1)

    # get post relevant
    post_relevant = Post.objects.filter(
        active=True, status=1, category=post.category).order_by("-created_on")[:4]

    context = {
        'post': post,
        'post_relevant': post_relevant,
    }
    return render(request, "detail.html", context=context)

# get page kien thuc nha khoan
def getKienThucNhaKhoa(request):
    posts = Post.objects.filter(active=True, status=1)

    context = {
        'posts': posts,
    }
    return render(request, "list_post.html", context=context)


# trang xem nhap bai viet cho admin
@login_required
@permission_required('admin', raise_exception=True)
def viewPostDraft(request, slug):
    post = get_object_or_404(Post, slug=slug)

    context = {
        'post': post,
    }

    return render(request, "detail.html", context=context)


# trang liên hệ
def getContact(request):
    return render(request, "contact.html")

# trang tìm kiếm bài viết
def get_post_from_category(request, slug):
    posts = Post.objects.filter(category__name=slug, active=True, status=1)

    return render(request, 'list_post.html', {'page_obj': posts})


#======================================================#
# các trang xử lí lỗi 
def custom_page_not_found_view(request, exception):
    return render(request, "error_page.html", {})


def custom_error_view(request, exception=None):
    return render(request, "error_page.html", {})


def custom_permission_denied_view(request, exception=None):
    return render(request, "error_page.html", {})


def custom_bad_request_view(request, exception=None):
    return render(request, "error_page.html", {})

#=====================================================#
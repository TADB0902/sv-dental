from django.urls import path


from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>', views.postDetail, name='post-details'),
    path('post/<slug:slug>', views.postDetailWithSlug, name='post-details'),
    path('post/draft/<slug:slug>', views.viewPostDraft, name='post-draft'),
    path('kien-thuc-nha-khoa/<slug:slug>', views.get_post_from_category, name='post-post-from-category'),
    path('lien-he', views.getContact, name='lien-he'),

]
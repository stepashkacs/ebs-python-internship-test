from django.urls import path
from rest_framework.routers import DefaultRouter

from apps.blog.views import (
    BlogItemView,
    BlogListView,
    CategoryViewSet,
    CreateBlogPostView,
    CreateBlogCommentView,
    CreateCommentView,
    BlogPostDetailView
)

router = DefaultRouter(trailing_slash=False)
router.register(
    r"blog/categories",
    CategoryViewSet,
    basename="category",
)

urlpatterns = [
    path("blog", BlogListView.as_view(), name="blog_list"),
    path("blog/<int:pk>", BlogItemView.as_view(), name="blog_item"),
    path("blog/create", CreateBlogPostView.as_view(), name="create_blog_post"),
    path("blog/<int:pk>/comment", CreateBlogCommentView.as_view(), name="create_comment"),
    path('blog/<int:blog_id>/comment', CreateCommentView.as_view(), name='create_comment'),
    path('blog/<int:id>/', BlogPostDetailView.as_view(), name='blog_detail'),
    *router.urls,
]

from rest_framework import viewsets, generics
from rest_framework.generics import GenericAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response

from apps.blog.models import Blog, Category, BlogPost, BlogComment
from apps.blog.serializers import (
    BlogSerializer,
    CategorySerializer,
    BlogPostSerializer,
    BlogCommentSerializer,
    CommentCreateSerializer
)
from apps.common.permissions import ReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()


class BlogListView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly,)

    def get(self, request: Request) -> Response:
        blogs = Blog.objects.all()
        return Response(self.get_serializer(blogs, many=True).data)


class BlogItemView(GenericAPIView):
    serializer_class = BlogSerializer
    permission_classes = (ReadOnly, IsAuthenticated)

    def get(self, request: Request, pk: int) -> Response:
        blog: Blog = get_object_or_404(Blog.objects.all(), pk=pk)
        return Response(self.get_serializer(blog).data)


class CreateBlogPostView(generics.CreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer


class CreateBlogCommentView(generics.CreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = BlogCommentSerializer


class CreateCommentView(generics.CreateAPIView):
    queryset = BlogComment.objects.all()
    serializer_class = CommentCreateSerializer


class BlogPostDetailView(generics.RetrieveAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer
    lookup_field = 'id'
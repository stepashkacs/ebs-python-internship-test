from rest_framework import serializers
from apps.blog.models import Blog, Category, BlogPost, BlogComment


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = "__all__"


class BlogCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogComment
        fields = ['id', 'text', 'created_at']


class BlogPostSerializer(serializers.ModelSerializer):
    comments = BlogCommentSerializer(many=True, read_only=True)  # Добавляем поле comments для связанных комментариев

    class Meta:
        model = BlogPost
        fields = ['id', 'title', 'content', 'created_at', 'updated_at', 'comments']  # Поле comments включено


class CommentCreateSerializer(serializers.ModelSerializer):
    blog_id = serializers.PrimaryKeyRelatedField(queryset=BlogPost.objects.all(), source='blog', write_only=True)

    class Meta:
        model = BlogComment
        fields = ['id', 'text', 'created_at', 'blog_id']

    def create(self, validated_data):
        return BlogComment.objects.create(**validated_data)

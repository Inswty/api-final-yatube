from django.shortcuts import get_object_or_404
from rest_framework import filters, permissions, status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from api.permissions import IsAuthorOrReadOnly
from api.serializers import (CommentSerializer, FollowSerializer,
                             GroupSerializer, PostSerializer)
from posts.models import Comment, Follow, Group, Post


class BaseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsAuthorOrReadOnly)
    filter_backends = (filters.SearchFilter,)


class PostViewSet(BaseViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    pagination_class = LimitOffsetPagination
    ordering_fields = ('pub_date',)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(BaseViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    search_fields = ('title',)

    def get_post(self):
        return get_object_or_404(Post, id=self.kwargs.get('post_id'))

    def get_queryset(self):
        return self.get_post().comments.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, post=self.get_post())


class GroupViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
    search_fields = ('title',)


class FollowViewSet(BaseViewSet):
    queryset = Follow.objects.all()
    serializer_class = FollowSerializer
    permission_classes = (permissions.IsAuthenticated,)
    search_fields = ('following__username',)
    http_method_names = ('get', 'post',)

    def retrieve(self, request, *args, **kwargs):
        return Response(status=status.HTTP_404_NOT_FOUND)

    def get_queryset(self):
        return self.queryset.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

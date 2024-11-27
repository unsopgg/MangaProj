from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .serializers import CommentSerializer
from .models import Comment


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated, ]

# class CommentLikeViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = [IsAuthenticated, ]
#
#     def get_permissions(self):
#         if self.action in ['list', 'retrieve']:
#             permissions = []
#         elif self.action == 'like':
#             permissions = [IsAuthenticated, ]
#         else:
#             permissions = [IsCommentCreator, ]
#         return [permissions() for permissions in permissions]
#
#

    def get_serializer_context(self):
        return {'request': self.request}

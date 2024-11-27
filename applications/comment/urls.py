from django.urls import path, include

from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('comments', CommentViewSet, )
# router.register('like', CommentLikeViewSet, )

urlpatterns = [
    path('comment/', include(router.urls))
]
urlpatterns.extend(router.urls)
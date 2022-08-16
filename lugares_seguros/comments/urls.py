from django.urls import path
from .views import CommentOnlyView, CommentView


urlpatterns = [
    path('', CommentView.as_view()),
    path('<int:pk>/', CommentOnlyView.as_view())
]
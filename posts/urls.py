from django.urls import path
from .views import PostListView, PostDetailView, PostCreatView, PostUpdateView, PostDeleteView


urlpatterns = [
    path("", PostListView.as_view(), name="post_list"),
    path("detail/<int:pk>/", PostDetailView.as_view(), name='post_detail'),
    path("new/",PostCreatView.as_view(), name="post_new"),
    path("edit/<int:pk>/", PostUpdateView.as_view(), name="post_edit"),
    path("delete/<int:pk>", PostDeleteView.as_view(), name="post_delete")
]
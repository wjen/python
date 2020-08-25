from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView, CategoryListView, LikeView, AddCommentView
urlpatterns = [
    # path('', views.home, name='home'),
    path('', HomeView.as_view(), name='home'),
    path('article/<int:pk>', ArticleDetailView.as_view(), name='article_detail'),
    path('article/new', AddPostView.as_view(), name='post'),
    path('article/add_category', AddCategoryView.as_view(), name='add_category'),
    path('article/<int:pk>/edit', UpdatePostView.as_view(), name='update_post'),
    path('article/<int:pk>/delete', DeletePostView.as_view(), name='delete_post'),
    path('categories/<str:cats>', CategoryView, name='category'),
    path('categories-list', CategoryListView, name='category-list'),
    path('like/<int:pk>', LikeView, name='like_post'),
    path('article/<int:pk>/comment', AddCommentView.as_view(), name='add_comment')

]

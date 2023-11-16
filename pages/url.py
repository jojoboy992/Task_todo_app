from django.urls import path,include
from .views import *
from django.contrib.auth.views import LogoutView 


# # from .views import (
# #     homePageView,
# #     BlogDetailView,
# #     BlogCreateView,
# #     BlogUpdateView,
# #     BlogDeleteView,
# #     CommentView,
# #     CategoryView,
# # )
# # from .views import loginView
# from django.conf import settings
# from django.contrib import admin
# from django.conf.urls.static import static
# from .views import *
# from django.conf import os

# from django.conf.urls.static import static

# urlpatterns = [
#     # path("image_upload/", avatarView, name="image_upload"),
#     # path("success/", name="success"),
#     path("",  name="home"),
#     path("login/", name="login"),
#     path("<int:pk>",  name="content_prev"),
#     path("post/new", name="post_create"),
#     path("comment/new", name="comment_create"),

#     path("post/<int:pk>/edit",  name="post_edit"),
#     path("post/<int:pk>/delete", name="post_delete"),
#     path("category/<str:category>",  name="category_view"),
# ]


# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# # urlpatterns = [path("", homePageView.as_view(), name="home"), path("login", loginView)]

urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page= 'login'), name='logout'),
    path('signup/', RegisterPage.as_view(), name='register'),
    path('', TaskList.as_view(),name='tasks'),

    path('preview/<int:pk>/', TaskDetail.as_view(),name='tasks_detail'),
    path('preview_todo/<int:pk>/', NoteDetail.as_view(),name='notes_detail'),

    path('New_todo/', TaskCreate.as_view(),name='tasks_create'),
    path('New_Note/', NoteCreate.as_view(), name='notes_create'),

    path('Edit_todo/<int:pk>/', TaskEdit.as_view(),name='edit'),
    path('Edit_Note/<int:pk>/', NoteEdit.as_view(),name='edit_note'),

    path('Delete_todo/<int:pk>/', TaskDelete.as_view(),name='delete'),
    path('Delete_Note/<int:pk>/', NoteDelete.as_view(),name='delete_note'),




]

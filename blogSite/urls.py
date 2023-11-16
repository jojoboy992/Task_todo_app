from django.contrib import admin
from django.urls import path, include
from pages.views import *
# # from pages.views import loginView
# from django.conf import settings

# from django.conf.urls.static import static

# # from pages.views import *

# urlpatterns = [
    # path("admin/", admin.site.urls),
#     # path("pages/", include("pages.url")),
#     # path("login/", loginView, name="login"),
#     # path("accounts/", include("django.contrib.auth.urls")),
#     # path("accounts/", include("accounts.url")),
# ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns = [
    path("admin/", admin.site.urls),
    path('tasks/', include('pages.url')),
    path('',HomePage.as_view(), name='home_page'),
    path('home/', DashBoard.as_view(), name="dashboard"),
    path('notes/', NoteView.as_view(), name="notes"),

]

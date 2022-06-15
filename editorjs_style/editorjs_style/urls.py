from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from app import views

urlpatterns = [

    path('', views.home_view, name='home'),
    path('new/', views.AddPostView.as_view(), name='add_post'),
    path('detail/<int:post_id>/', views.detail_view, name='detail'),
    path('edit/<int:pk>/', views.EditPostView.as_view(), name='edit_post'),
    path('delete/<int:post_id>/', views.delete_view, name='delete_post'),

    path('admin/', admin.site.urls),
    path('editorjs/', include('django_editorjs_fields.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

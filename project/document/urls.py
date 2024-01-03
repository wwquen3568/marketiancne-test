from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from document import views


urlpatterns = [
    path('', views.board_read, name='board_read'),
    path('<int:pk>/read/', views.board_detail, name='board_detail'),
    path('create/', views.board_create, name='board_create'),
    path('<int:pk>/edit/', views.board_edit, name='board_edit'),
    path('<int:pk>/delete', views.board_delete, name='board_delete'),

]
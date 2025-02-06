from django.contrib import admin
from django.urls import path, include
from game import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('game/<int:game_id>/', views.game_detail, name='game'),
    path('new-game/', views.new_game, name='new_game'),
] 
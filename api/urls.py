from django.urls import path

from . import views

urlpatterns = [
    path('categories/', views.CategoriesView.as_view(), name='categories'),
    path('levels/', views.LevelsView.as_view(), name='levels'),
    path('themes/', views.ThemesView.as_view(), name='themes'),
    path('themes/<int:theme_id>', views.ThemeView.as_view(), name='theme'),
    path('words/<int:word_id>', views.WordsView.as_view(), name='words'),
]

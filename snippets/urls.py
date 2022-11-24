from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views

urlpatterns = [
    path('snippets/', views.SpinnetList.as_view()),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(0))
]

urlpatterns = format_suffix_patterns(urlpatterns)
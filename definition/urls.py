from django.urls import path
# 
from .views import (
    HackerListView,
    HackerDetailView,
    HackerCreateView,
    HackerUpdateView,
    HackerDeleteView
    )
app_name = 'definitions'
urlpatterns = [
    path('', HackerListView.as_view(), name='definition-list'),
    path('create/', HackerCreateView.as_view(), name='definition-create'),
    path('<int:id>/', HackerDetailView.as_view(), name='definition-detail'),
    path('<int:id>/update/', HackerUpdateView.as_view(), name='definition-update'),
    path('<int:id>/delete/', HackerDeleteView.as_view(), name='definition-delete'), 
]
from django.urls import path
from .views import ClassList

urlpatterns = [
    #path('<int:class_id>', class_by_id),
    path('', ClassList.as_view())
]
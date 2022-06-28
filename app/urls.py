from django.urls import path
from .views import test_get, test_post, test_put, test_delete

urlpatterns = [
    path('', test_get),
    path('post/', test_post),
    path('update/<int:id>/', test_put),
    path('delete/<int:id>/', test_delete),
]
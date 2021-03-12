from django.conf.urls import url
from books import views

urlpatterns = [
    url(r'^api/books$', views.book_list, name='book_list'),
    url(r'^api/books/(?P<pk>[0-9]+)$', views.book_detail),
    url(r'^api/books/published$', views.book_list_published)
]

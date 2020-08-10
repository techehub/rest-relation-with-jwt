from django.urls import path, include
from .views import AuthorView, PublisherView, BookView, UserCreate
from rest_framework.routers import DefaultRouter


author_router = DefaultRouter()
author_router.register('author', AuthorView)

pub_router = DefaultRouter()
pub_router.register('pub', PublisherView)

book_router = DefaultRouter()
book_router.register('book', BookView)

urlpatterns = [

    path('', include(pub_router.urls)),
    path('', include(book_router.urls)),
    path ('', include(author_router.urls)),
    path('account/register', UserCreate.as_view())

]
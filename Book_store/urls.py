from django.db import router
from rest_framework.routers import DefaultRouter
from Book_store.views import BookStoreView


router = DefaultRouter()


router.register(r'Book-op',BookStoreView,basename="book_store")
from django.urls import path
from .views import ScrapeDailyDataView

urlpatterns = [
    path('scrape/', ScrapeDailyDataView.as_view(), name='scrape'),
]
from django.urls import path
from apppage import views

app_name = "pages"

urlpatterns = [
    path('',views.PortfolioView.as_view(),name="home")
]
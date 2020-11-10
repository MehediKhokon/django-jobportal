from django.urls import path
from . import views

urlpatterns = [
    
    # path('', views.home, name='home'),
    path('', views.HomePageView.as_view(), name='home'),
    # path('detail/<int:id>', views.detail, name='detail'),
    path('detail/<int:pk>', views.JobDetailView.as_view(), name='detail'),
    path('search/', views.search, name='search'),
    path('signup', views.SignUpView.as_view(), name='signup'),
    path('create-cv/<int:pk>', views.CvCreateView.as_view(), name='create-cv'),
    path('cv-list-view', views.CvListView.as_view(), name='cv-list-view'),
]
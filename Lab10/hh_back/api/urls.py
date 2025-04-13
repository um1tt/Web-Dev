from django.urls import path
from . import views

urlpatterns = [
    path('companies/', views.company_list),
    path('companies/<int:pk>/vacancies/', views.company_vacancies),
    path('vacancies/', views.VacancyListCreateView.as_view()),
    path('vacancies/<int:pk>/', views.VacancyDetailView.as_view()),
]
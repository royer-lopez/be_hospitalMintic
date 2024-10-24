"""
URL configuration for HospitalMintic project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from hospitalBacked import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', views.userView.UsuarioListView.as_view()),
    path('user/<int:pk>/', views.userView.UsuarioRetrieveupdatetoDeleteView.as_view()),
    path('medico/', views.medicoView.MedicoListView.as_view()),
    path('medico/<int:pk>/', views.medicoView.MedicoRetrieveupdatetoDeleteView.as_view()),

]

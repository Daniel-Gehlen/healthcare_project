from django.urls import path, include

urlpatterns = [
    path('healthcare/', include('healthcare.urls')),  # Adicione esta linha para incluir as URLs do aplicativo 'healthcare'
]

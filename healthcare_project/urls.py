from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include

urlpatterns = [
    path('healthcare_app/', include('healthcare_app.urls')),  # Certifique-se de usar o nome correto do aplicativo
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

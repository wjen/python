from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('catalog/', include('catalog.urls'))
]

#Add URL maps to redirect the base URL to our application
from django.views.generic import RedirectView
urlpatterns += [
    path('', RedirectView.as_view(url='catalog/', permanent=True)),
]

# Use static() to add url mapping to serve static files during development (only)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# another way to do the above
# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('catalog/', include('catalog.urls')),
#     path('', RedirectView.as_view(url='catalog/')),
# ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#Add Django site authentication urls (for login, logout, password management)

urlpatterns += [
    path('accounts/', include('django.contrib.auth.urls')),
]
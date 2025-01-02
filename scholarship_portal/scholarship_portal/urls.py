# scholarship_portal/urls.py
from django.urls import path, include
from . import views  # Import views if needed
from django.contrib import admin
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/users/', include('users.urls')),  # Assuming you have a 'users' app
    path('api/scholarships/', include('scholarships.urls')),  # Assuming you have a 'scholarships' app
    path('', views.home),  # Add this line to handle the root URL
]
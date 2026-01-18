from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    # Added the slash after 'books'
    path('books/', include('relationship_app.urls')), 
    
]
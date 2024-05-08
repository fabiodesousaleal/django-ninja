from django.urls import path, include
from .api import router
urlpatterns = [
    path('exemplo/', include(router.urls_paths) )        
]

from django.urls import path
from . import views
                    
urlpatterns = [
    path('', views.root),
    path('destroy_session', views.destroy_session),
    path('add_2', views.increment_2),
    path('add_custom', views.incrementation),
]
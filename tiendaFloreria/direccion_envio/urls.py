from unicodedata import name
from django.urls import path
from . import views

app_name = 'direccion_envio'


urlpatterns = [
    path('',views.DireccionEnviosListView.as_view(), name='direccion_envio'),
    path('crear', views.crear, name="crear"),
    path('update/<int:pk>',views.DireccionEnviosUpdateView.as_view(),name='update'),
    path('borrar/<int:pk>',views.DireccionEnviosDeleteView.as_view(),name='borrar'),
]


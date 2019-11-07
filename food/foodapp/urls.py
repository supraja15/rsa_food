from django.urls import path,re_path
from foodapp import views

app_name="foodapp"

urlpatterns = [
     path('create/',views.CreateView.as_view(),name="create"),
      re_path(r'^update/(?P<pk>\w+)/',views.UpdateView.as_view(),name='update_view'),
]
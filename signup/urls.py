from django.urls import path

from .views import (
    SignupCreateView,
    SignupDetailView,
    SignupUpdateView,
    SignupListView
)
app_name = "signup"
urlpatterns = [

    path('',SignupListView.as_view(),name="signup-list"),
    path('create/',SignupCreateView.as_view(),name='signup-create'),
    path('<int:id>/',SignupDetailView.as_view(),name="signup-detail"),
    path('<int:id>/update',SignupUpdateView.as_view(),name='signup-update'),
    #path('<int:id>/delete/',product_delete_view,name='product-delete'),




]

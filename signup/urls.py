from django.urls import path

from .views import SignupCreateView,SignupDetailView,SignupUpdateView

app_name = 'signup'
urlpatterns = [

    #path('',product_list_view,name="product-list"),
    path('create/',SignupCreateView.as_view(),name='signup-create'),
    path('<int:id>/',SignupDetailView.as_view(),name="signup-detail"),
    path('<int:id>/update',SignupUpdateView.as_view(),name='signup-update'),
    #path('<int:id>/delete/',product_delete_view,name='product-delete'),




]

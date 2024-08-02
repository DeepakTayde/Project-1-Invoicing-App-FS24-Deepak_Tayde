from django.urls import path
from .views import *
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path("products/", ProductView.as_view(), name="products"),
    path("products/<int:id>/", ProductView.as_view(), name="products"),
    path("products/<slug:name>/", SpecificProductView.as_view(), name="Specific-Product-View"),
    path("carts/", CartView.as_view(), name="Cart-View"),
    path("carts/<int:id>/", CartView.as_view(), name="Cart-View"),
    path("search/", SearchProductView.as_view(), name="search-product-View"),
    path("users/", UserView.as_view(), name="User-View"),
    path("signup/", SignupView.as_view(), name="SignUp-View"),
    path("login/", LoginView.as_view(), name="Login-View"),
    path("invoices/", InvoiceView.as_view(), name="Invoice-View"),
    path("invoices/new/", InvoiceView.as_view(), name="Invoice-View-post"),
    path("invoices/<int:invoice_id>/", InvoiceDetailsView.as_view(), name="Invoice-Details-View"),
    path("invoices/<int:invoice_id>/items/", ItemsView.as_view(), name="Items-View-post"),

]
from django.urls import path

from . import views

urlpatterns = [
    path("legislator/<int:legislator_id>/", views.legislator, name="legislator"),
    path("bill/<int:bill_id>/", views.bill, name="bill")
]
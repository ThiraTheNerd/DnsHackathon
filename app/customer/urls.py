from django.urls import path

urlpatterns = [
    path('customer/', CustomerPrediction.as_view() )
    
]
from django.shortcuts import render
from rest_framework.views import APIView
from .apps import *
from rest_framework import status
from django.http import HttpResponse, JsonResponse, response, Http404
# Create your views here.

class CustomerPrediction(APIView):
    def post(self,request):
        data = request.data
        age= request.GET.get('age')
        gender = request.GET.get('gender')
        bp = request.GET.get('bp')
        cholesterol = request.GET.get('cholesterol')
        salt = request.GET.get('salt')
        dtree = CustomerConfig.model
        #Predict using independent variables
        fields = []
        prediction = dtree.predict(fields)
        return JsonResponse(prediction, status=200)
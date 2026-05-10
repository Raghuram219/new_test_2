from django.shortcuts import render
from rest_framework import viewsets
from .models import *
from .serializer import *

class EducationViewSet(viewsets.ModelViewSet):
    queryset = Education.objects.all()
    serializer_class = EducationSerializer

from rest_framework import serializers
from .models import *

class EducationSerializer(serializers.ModelSerializer):
    class_no = serializers.SerializerMethodField()

    class Meta:
        model = Education
        fields = ('name', 'class_no')

    def get_class_no(self, obj):
        return "Test extra"
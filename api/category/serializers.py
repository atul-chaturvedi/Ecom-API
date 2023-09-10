from rest_framework import serializers
from .models import Category

class CategorySerializers(serializers.Serializer):
    class Meta:
        model = Category
        feild =('name', 'description')
from rest_framework.serializers import ModelSerializer
from .models import TextSnippet

# Serializer Class
class TextSnippetSerializer(ModelSerializer):
    class Meta:
        model = TextSnippet
        fields = '__all__'

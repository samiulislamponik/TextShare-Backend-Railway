
# Django Rest Framework
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Model
from .models import TextSnippet

# Serializers
from .serializers import TextSnippetSerializer

# Universally unique identifier:
# https://www.npmjs.com/package/uuid
import uuid




# Create your views here.

# Saving the text into database
@api_view(['POST'])
def create_text_snippet(request):
    try:
        data = request.data
        text_snippet = TextSnippet.objects.create(content=data['content'], url=generate_unique_url())
        serializer = TextSnippetSerializer(text_snippet, many=False)
        return Response(serializer.data)
    except:
        return Response({'message': 'An error occurred while creating the text snippet.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

# Generating Random String
def generate_unique_url():
    return str(uuid.uuid4())


# Edit the text
@api_view(['PUT'])
def update_text_snippet(request, url):
    try:
        data = request.data
        text_snippet = TextSnippet.objects.get(url=url)
        serializer = TextSnippetSerializer(instance=text_snippet, data=data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)
    except TextSnippet.DoesNotExist:
        return Response({'message': 'The specified text snippet does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'message': 'An error occurred while updating the text snippet.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Get the Text
@api_view(['GET'])
def retrieve_text_snippet(request, url):
    try:
        text_snippet = TextSnippet.objects.get(url=url)
        serializer = TextSnippetSerializer(text_snippet, many=False)
        return Response(serializer.data)
    except TextSnippet.DoesNotExist:
        return Response({'message': 'The specified text snippet does not exist.'}, status=status.HTTP_404_NOT_FOUND)
    except:
        return Response({'message': 'An error occurred while retrieving the text snippet.'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)



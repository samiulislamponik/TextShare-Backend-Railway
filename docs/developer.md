
<p align="center">
  <img src="../markdown_icons/book.png" alt="Image" width="200" height="200">
</p>

<h1 align="center">DEVELOPER GUIDE</h1>

### Project Structure

```
text_share/
├── api/
│ ├── **init**.py
│ ├── admin.py
│ ├── apps.py
│ ├── models.py
│ ├── serializers.py
│ ├── tests.py
│ ├── urls.py
│ └── views.py
├── text_share/
│ ├── **init**.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── db.sqlite3
└── manage.py
```

### Table of Content

-   [models.py](#modelspy)
    -   [TextSnippet Model](#textsnippet-model)
        -   [Fields](#fields)
        -   [Methods](#methods)
            -   [Written codes:](#written-codes)
            -   [Example usage:](#example-usage)
-   [serializers.py](#serializerspy)
    -   [TextSnippetSerializer](#textsnippetserializer)
        -   [Fields](#fields-1)
            -   [Written codes:](#written-codes-1)
            -   [Example usage:](#example-usage-1)
-   [urls.py](#urlspy)
-   [View.Py](#viewpy)
    -   [create_text_snippet ()](#create_text_snippet-)
        -   [API Endpoint](#api-endpoint)
        -   [Description](#description)
        -   [Request Body](#request-body)
        -   [Response](#response)
            -   [Success Response](#success-response)
            -   [Error Response](#error-response)
            -   [Written codes:](#written-codes-2)
        -   [Helper Function](#helper-function)
            -   [generate_unique_url ()](#generate_unique_url-)
            -   [Written codes:](#written-codes-3)
            -   [Example usage:](#example-usage-2)
    -   [update_text_snippet ()](#update_text_snippet-)
        -   [API Endpoint](#api-endpoint-1)
        -   [Description](#description-1)
        -   [Request Body](#request-body-1)
        -   [URL Parameter](#url-parameter)
        -   [Response](#response-1)
            -   [Success Response](#success-response-1)
            -   [Error Response](#error-response-1)
            -   [Written codes:](#written-codes-4)
    -   [retrieve_text_snippet ()](#retrieve_text_snippet-)
        -   [API Endpoint](#api-endpoint-2)
        -   [Description](#description-2)
        -   [URL Parameter](#url-parameter-1)
        -   [Response](#response-2)
            -   [Success Response](#success-response-2)
            -   [Error Response](#error-response-2)
            -   [Written codes:](#written-codes-5)
-   [settings.py](#settingspy)
    -   [INSTALLED_APPS](#installed_apps)
    -   [MIDDLEWARE](#middleware)
    -   [CORS_ORIGIN_ALLOW_ALL](#cors_origin_allow_all)

# models.py

This file defines the models used in the `text_share` application.

## TextSnippet Model

The TextSnippet model represents a text snippet that has been saved by a user. It has two fields: **content**, which stores the content of the text snippet, and **url**, which stores a unique URL generated for the text snippet. The `__str__()` method returns a string representation of the TextSnippet instance, which is used when the instance is displayed in the Django admin site.

### Fields

-   `content`: `TextField` - The content of the text snippet.
-   `url`: `CharField` - A unique string generated for the text snippet URL.

### Methods

-   `__str__()`: Returns a string representation of the `TextSnippet` instance. This method is used when the `TextSnippet` instance is displayed in the Django admin site.

#### Written codes:

```python
class TextSnippet(models.Model):
    content = models.TextField()
    url = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return f"{self.id}: {self.content[:25]}"
```

#### Example usage:

```python
snippet = TextSnippet.objects.create(content='Hello, world!', url='sdjfalsjdfjaweyru2345345')
print(snippet) # Output: 1: Hello, world!
```

# serializers.py

This file defines the serializers used in the `text_share` application.

## TextSnippetSerializer

The TextSnippetSerializer class is used to convert `TextSnippet` model instances to JSON and vice versa. It has two fields: **content**, which represents the content of the text snippet, and **url**, which represents the unique URL generated for the text snippet.

### Fields

-   `content`: `TextField` - The content of the text snippet.
-   `url`: `CharField` - A unique string generated for the text snippet url.

#### Written codes:

```python
from rest_framework.serializers import ModelSerializer
from .models import TextSnippet

class TextSnippetSerializer(ModelSerializer):
    class Meta:
        model = TextSnippet
        fields = '__all__'
```

#### Example usage:

```python
snippet = TextSnippet.objects.create(content='Hello, world!', url='j3j5k343k43jk34kj34')
serializer = TextSnippetSerializer(snippet)
print(serializer.data) # Output: {'id': 1, 'content': 'Hello, world!', 'url': 'j3j5k343k43jk34kj34'}

```

In the example above, we first create a `TextSnippet` instance with content `Hello, world!` and URL `j3j5k343k43jk34kj34`. We then create an instance of the `TextSnippetSerializer` class with the `snippet` instance as the argument. Finally, we print the serialized `data` using the data attribute of the serializer instance.

# urls.py

The following URLs were defined in the `urls.py` file of the `api` app:

**`create_text_snippet`**

-   **Path:** `/text/`
-   **Function:** views.`create_text_snippet`
-   **Name:** `create_text_snippet`
    This URL allows for the creation of a new text snippet.

**`retrieve_text_snippet`**

-   **Path:** `/text/<str:url>/`
-   **Function:** `views.retrieve_text_snippet`
-   **Name:** `retrieve_text_snippet`
    This URL allows for the retrieval of a specific text snippet, where `url` is the unique identifier string for the snippet.

**`update_text_snippet`**

-   **Path:** `/text/<str:url>/edit/`
-   **Function:** `views.update_text_snippet`
-   **Name:** `update_text_snippet`
    This URL allows for the editing of a specific text snippet, where `url` is the unique identifier string for the snippet.

# View.Py

## create_text_snippet ()

### API Endpoint

```bash

@POST /text/

```

### Description

This API endpoint creates a new text snippet object and saves it to the database. The text snippet object has a `content` field which is the text content of the snippet, and a `url` field which is a randomly generated unique string identifier for the snippet.

### Request Body

The request body must be a JSON object with the following fields:

-   content (required): The text content of the text snippet.

**Example Request Body:**

```json
{
    "content": "This is an example text snippet."
}
```

### Response

#### Success Response

-   Status Code: 200 OK
-   Response Body: A JSON object representing the created text snippet.

**Example Response Body:**

```json
{
    "id": 1,
    "content": "This is an example text snippet.",
    "url": "e52f5a3e-569e-4f10-9129-9a199c8f4b4d"
}
```

#### Error Response

-   Status Code: 500 Internal Server Error
-   Response Body: A JSON object with an error message.

**Example Response Body:**

```json
{
    "message": "An error occurred while creating the text snippet."
}
```

#### Written codes:

```python
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

```

### Helper Function

#### generate_unique_url ()

This function generates a random unique identifier using the `uuid.uuid4()` function from the `uuid` module.

#### Written codes:

```python
# Generating Random String
def generate_unique_url():
    return str(uuid.uuid4())
```

#### Example usage:

```python
unique_url = generate_unique_url()
print(unique_url)# Output: e52f5a3e-569e-4f10-9129-9a19

```

## update_text_snippet ()

### API Endpoint

```bash

@PUT /text/<str:url>/edit

```

### Description

This API endpoint updates an existing text snippet object in the database. The text snippet object is identified by its `url` field, which is a unique identifier generated when the object was created.

### Request Body

The request body must be a JSON object with the following fields:

-   content (optional): The updated text content of the text snippet.

**Example Request Body:**

```json
{
    "content": "This is an updated example text snippet."
}
```

### URL Parameter

The `url` parameter is the unique identifier of the text snippet to be updated.
**Example URL:**

```bash
/text/e52f5a3e-569e-4f10-9129-9a199c8f4b4d/edit
```

### Response

#### Success Response

-   Status Code: 200 OK
-   Response Body: A JSON object representing the updated text snippet.

**Example Response Body:**

```json
{
    "id": 1,
    "content": "This is an updated example text snippet.",
    "url": "e52f5a3e-569e-4f10-9129-9a199c8f4b4d"
}
```

#### Error Response

-   Status Code: 404 Not Found
-   Response Body: A JSON object with an error message.

**Example Response Body:**

```json
{
    "message": "The specified text snippet does not exist."
}
```

OR

-   Status Code: 500 Internal Server Error
-   Response Body: A JSON object with an error message.

```json
{
    "message": "An error occurred while updating the text snippet."
}
```

#### Written codes:

```python
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

```

## retrieve_text_snippet ()

### API Endpoint

```bash

@GET /text/<str:url>/

```

### Description

This API endpoint retrieves a single text snippet object from the database based on its unique `url` identifier.

### URL Parameter

The `url` parameter is the unique identifier of the text snippet to be updated.
**Example URL:**

```bash
/text/e52f5a3e-569e-4f10-9129-9a199c8f4b4d/
```

### Response

#### Success Response

-   Status Code: 200 OK
-   Response Body: A JSON object representing the retrieved text snippet.

**Example Response Body:**

```json
{
    "id": 1,
    "content": "This is an example text snippet.",
    "url": "e52f5a3e-569e-4f10-9129-9a199c8f4b4d"
}
```

#### Error Response

-   Status Code: 404 Not Found
-   Response Body: A JSON object with an error message.

**Example Response Body:**

```json
{
    "message": "The specified text snippet does not exist."
}
```

OR

-   Status Code: 500 Internal Server Error
-   Response Body: A JSON object with an error message.

```json
{
    "message": "An error occurred while retrieving the text snippet."
}
```

#### Written codes:

```python
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


```

# settings.py

The following changes were made in the `settings.py` file of a Django project:

## INSTALLED_APPS

The `INSTALLED_APPS` variable contains a list of all the applications and libraries that are installed and being used in the Django project. The following items were added to this list:

-   `api.apps.ApiConfig`: The main app for the project.
-   `rest_framework`: A library for building REST APIs.
-   `corsheaders`: A library for handling CORS (Cross-Origin Resource Sharing).
    `whitenoise.runserver_nostatic`: A library that serves static files during development, including the admin page CSS.

## MIDDLEWARE

The `MIDDLEWARE` variable contains a list of middleware classes that are applied to every request/response cycle in the Django project. The following items were added to this list:

-   `corsheaders.middleware.CorsMiddleware`: Enables CORS handling for all incoming requests.

-   `whitenoise.middleware.WhiteNoiseMiddleware`: Serves static files using WhiteNoise during production.

## CORS_ORIGIN_ALLOW_ALL

The `CORS_ORIGIN_ALLOW_ALL` variable is set to `True`, which means that any origin is allowed to make requests to the server. This is useful during development, but in production it's recommended to specify specific origins that are allowed to make requests.

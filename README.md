# Text Sharing Web Application

A web application for sharing snippets of text, built with Django, Django REST Framework, and React.

## Project Overview

The Text Sharing Web Application is a simple program that allows users to save and share text snippets. Users can enter the text into a text area and save it, and the text is stored in a persistent data store. The program generates a unique URL for each saved text snippet, which can be used to retrieve and edit the text.

## Technologies Used

-   Django
-   Django REST Framework
-   React

## Features

The following features are available in this web application:

-   Users can enter text into a text area and save it.
-   The saved text is stored in a persistent data store.
-   A URL is generated for the saved text which can be used to retrieve and edit the text.
-   When a user follows the URL, the saved text is displayed along with an option to edit the text.
-   When a user clicks the edit button, the text is copied and placed in the same interface used to create new text snippets.

## Getting Started

To get started with the Text Sharing Web Application, follow these steps:

1. Clone the repository: `git clone https://github.com/yourusername/text-sharing-app.git`
2. Install the required dependencies: `pip install -r requirements.txt`
3. Run the server: `python manage.py runserver`
4. Navigate to http://localhost:8000/ in your web browser to access the application.

## User Interface

The user interface for the Text Sharing Web Application consists of two main screens:

1. Home screen: This screen displays a text area where users can enter the text to be shared. Users can save the text by clicking the "Save" button.

2. Text display screen: This screen displays the saved text and provides an option to edit the text.

## Usage

To use this web application, follow these steps:

1. Open your web browser and navigate to `http://localhost:3000/`.
2. Enter text into the text area.
3. Click the "Save" button to save the text.
4. A URL will be generated for the saved text.
5. To retrieve and edit the saved text, follow the URL and click the "Edit" button.
6. The saved text will be displayed and can be edited in the same interface used to create new text snippets.

## API Endpoints

The Text Sharing Web Application exposes the following API endpoints:

-   `POST /api/text-snippets/`: Creates a new text snippet.
-   `PUT /api/text-snippets/<str:url>/`: Updates an existing text snippet.
-   `GET /api/text-snippets/<str:url>/`: Retrieves an existing text snippet.

## Error Handling

The API endpoints are designed to handle errors gracefully. If an error occurs while creating, updating, or retrieving a text snippet, the API returns an appropriate error message along with a status code.

## Future Improvements

Some possible future improvements for the Text Sharing Web Application include:

-   Adding user authentication and authorization to ensure that only authorized users can create, edit, and view text snippets.
-   Improving the user interface to make it more intuitive and user-friendly.
-   Adding support for file uploads, so that users can upload and share files in addition to text snippets.

## Contributing

If you'd like to contribute to this web application, please follow these steps:

1. Fork the repository.
2. Create a new branch: `git checkout -b <branch-name>`
3. Make your changes and commit them: `git commit -m '<commit-message>'`
4. Push your changes to your fork: `git push origin <branch-name>`
5. Create a pull request.

## License

The Text Sharing Web Application is licensed under the MIT License. See LICENSE.txt for more information.

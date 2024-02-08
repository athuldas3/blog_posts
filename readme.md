# Question: 

- Create a Django project and a blog app within the project.

- Design a robust database schema for the blog system. It should include models for:

  - Blog Posts with fields for title, content, publication date, and author.

  - User Profiles with additional information (e.g., profile picture, bio).

  - Comments on blog posts.

  - Tags or Categories for blog posts.

- Implement views  to:

  - Allow users to create, edit, and delete blog posts.

  - Display a list of blog posts with pagination.

  - Allow users to comment on blog posts.

- Implement user authentication and authorization to ensure only authors 
can edit their own posts.

# Blog System

## Project Structure

This project follows a modular structure with packages for models, views, services, validators, and utilities.

- `sub_views`: Contains view logic for handling HTTP requests and generating responses.
- `services`: Includes queries to save data to the database.
- `validators`: Validates input data and returns validation errors.
- `utilities`: Contains utility functions and classes.
  - `exceptions`: Custom API exceptions.
  - `renderer`: Custom renderer to format responses for frontend consumption.

Additionally, the project folder contains:

- `local_urls.py`: Sets server-dependent URLs.
- `local_settings.py`: Allows server-dependent configurations (e.g., database settings).

## Database Schema

The database schema includes the following models:

- **Blog Posts**: Fields for title, content, publication date, and author.
- - **User**: user table for login.
- **Profiles**: Additional information such as profile picture and bio.
- **Comments**: Attached to blog posts.
- **Tags or Categories**: For organizing blog posts.

## Views

Implemented views allow users to perform the following actions:

- Create, edit, and delete blog posts. (used dependency injection to inherit the services)
- Display a paginated list of blog posts with comments.
- Comment on blog posts.

## Authentication and Authorization

User authentication is implemented using Django Rest Framework's default authentication system. Views are protected with decorators to ensure only authorized users can perform certain actions. For example, only authors can edit their own blog posts.

## Usage

1. Install the required packages listed in `requirements.txt`.
2. Set up the database according to the settings in `local_settings.py`. (I am pushing db also to git)
3. Run the Django development server.
4. Access the API endpoints to interact with the blog system using swagger.

## Contributing

Contributions are welcome! Please follow the project's coding conventions and submit pull requests.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.







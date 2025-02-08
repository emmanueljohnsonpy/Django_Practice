# Middlewares in Django (Cornell Method)

## What are Middlewares?
Middlewares are functions or classes in Django that process requests and responses globally before they reach the view or after they leave the view. They help in modifying requests, responses, or performing actions like authentication, security checks, and data transformation.

## Notes Section

### 1. **Purpose of Middleware**
- Middleware acts as a bridge between the request and response cycle.
- Used for processing requests before views are called.
- Can modify responses before they are sent to the client.
- Useful for authentication, logging, security, and request processing.

### 2. **Types of Middleware**
#### a) Security Middleware
- Enhances security by enforcing HTTPS and other security policies.
- Example:
  ```python
  'django.middleware.security.SecurityMiddleware'
  ```

#### b) Authentication Middleware
- Associates users with requests for authentication.
- Example:
  ```python
  'django.contrib.auth.middleware.AuthenticationMiddleware'
  ```

#### c) Session Middleware
- Manages user sessions in Django.
- Example:
  ```python
  'django.contrib.sessions.middleware.SessionMiddleware'
  ```

#### d) Common Middleware
- Provides various features like URL normalization, APPEND_SLASH, etc.
- Example:
  ```python
  'django.middleware.common.CommonMiddleware'
  ```

### 3. **Creating Custom Middleware**
- You can create your own middleware for custom processing.
- Example:
  ```python
  class CustomMiddleware:
      def __init__(self, get_response):
          self.get_response = get_response

      def __call__(self, request):
          print("Before View Execution")
          response = self.get_response(request)
          print("After View Execution")
          return response
  ```

## Cues Section
- What is the main function of middleware?
  - It processes requests and responses globally in Django.
- How does middleware help in authentication?
  - It assigns users to requests for authentication processing.
- Can we create custom middleware in Django?
  - Yes, by defining a class with `__call__` and `__init__` methods.
- How do you enable middleware in Django?
  - By adding it to the `MIDDLEWARE` list in `settings.py`.

## Summary Section
- **Middleware** acts as a filter between request and response.
- Django provides built-in middleware for security, authentication, sessions, etc.
- Custom middleware can be created to handle specific functionalities.
- Middleware is defined in the `MIDDLEWARE` list in `settings.py`.
- It enhances security, authentication, and request-response handling globally.


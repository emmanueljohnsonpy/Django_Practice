
# HTTP Requests in Django (Cornell Method)

## Key Points
- HTTP stands for **HyperText Transfer Protocol**.  
- HTTP requests are how data is sent from the client (browser) to the server.  
- HTTP requests can be of different **methods** (e.g., GET, POST, PUT, DELETE).  
- Requests are handled by views in Django, which are responsible for processing the request and returning a response.

## Detailed Notes

### 1. What is an HTTP Request?
- An HTTP request is a message sent by the client (like a web browser) to a server to request some action or information.
- The request contains different parts such as the **method**, **headers**, **URL**, and **body**.

### 2. HTTP Request Methods:
- **GET**: Used to request data from the server (e.g., loading a webpage). It does not modify any data.
  - Example: When you visit a webpage, the browser sends a GET request to the server to fetch the page.
- **POST**: Used to send data to the server, usually when submitting a form (e.g., user login or registration).
  - Example: When you fill out a form and hit submit, a POST request sends the form data to the server.
- **PUT**: Used to update an existing resource on the server.
  - Example: Updating a user’s information.
- **DELETE**: Used to remove a resource from the server.
  - Example: Deleting a product from a database.

### 3. Structure of an HTTP Request:
- **Method**: The type of action the request is performing (GET, POST, etc.).
- **URL**: The address of the resource you are requesting.
- **Headers**: Metadata that provides information like content type, authorization, or user-agent.
- **Body**: Contains data being sent to the server (typically in POST, PUT requests).

### 4. How Django Handles HTTP Requests:
- When a request is made to a Django application, Django routes the request to the appropriate **view** based on the URL pattern.
- The view processes the request, interacts with the database if needed, and returns an **HTTP response**.
- In Django views, you can access HTTP request data via `request` object (e.g., `request.GET` for GET data, `request.POST` for POST data).
  
  Example:
  ```python
  def my_view(request):
      if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          # Process the data and return a response
  ```

### 5. Django Views and HTTP Requests:
- **GET requests** are typically used to render a template or return data.
- **POST requests** are used to submit data (e.g., forms).
- Django also supports handling other HTTP methods like **PUT**, **DELETE**, etc., using class-based views or decorators.

### 6. Handling Query Parameters:
- GET requests often include query parameters in the URL (e.g., `/search/?q=python`).
- In Django, you can access these parameters using `request.GET`.

### 7. Django's `HttpRequest` Object:
- Django uses the `HttpRequest` object to represent an incoming HTTP request. This object allows access to data like:
  - `request.method`: The HTTP method (GET, POST, etc.).
  - `request.GET`: Data sent with GET requests.
  - `request.POST`: Data sent with POST requests.
  - `request.COOKIES`: Cookies sent with the request.
  - `request.user`: The user making the request (if authenticated).

# Summary (Bottom Column)

HTTP requests are how clients interact with a server. They contain a method, URL, headers, and body (optional).  

Common methods are:  
- **GET**: Fetch data  
- **POST**: Send data  
- **PUT**: Update data  
- **DELETE**: Remove data  

In Django, views handle requests and return responses. You can access request data via `request.GET` and `request.POST`.  

- **GET** is used for fetching data.  
- **POST** is used for sending data, like form submissions.  

# HTTP Methods in Django (Cornell Method)

### What are HTTP Methods?

HTTP methods define the actions that can be performed on a resource in a web application. They specify whether data should be retrieved, sent, updated, or deleted. In Django, HTTP methods are used to determine how views handle requests.

## Notes Section

### 1. **GET**
- Used to retrieve data from the server.
- Safe method (does not modify data).
- Common for rendering pages and fetching data.
- Example:
  ```python
  def product_list(request):
      products = Product.objects.all()
      return render(request, "products.html", {"products": products})
  ```

### 2. **POST**
- Used to send data to the server (e.g., form submission).
- Requires CSRF protection (`{% csrf_token %}`).
- Example:
  ```python
  def add_product(request):
      if request.method == "POST":
          name = request.POST["name"]
          price = request.POST["price"]
          Product.objects.create(name=name, price=price)
          return redirect("product_list")
      return render(request, "add_product.html")
  ```

### 3. **PUT**
- Used to update an existing resource entirely.
- Common in APIs (Django REST Framework).
- Example using DRF:
  ```python
  @api_view(["PUT"])
  def update_product(request, pk):
      product = Product.objects.get(id=pk)
      product.name = request.data["name"]
      product.price = request.data["price"]
      product.save()
      return Response({"message": "Product updated successfully"})
  ```

### 4. **PATCH**
- Used to partially update a resource.
- Example using DRF:
  ```python
  @api_view(["PATCH"])
  def partial_update_product(request, pk):
      product = Product.objects.get(id=pk)
      if "name" in request.data:
          product.name = request.data["name"]
      if "price" in request.data:
          product.price = request.data["price"]
      product.save()
      return Response({"message": "Product partially updated"})
  ```

### 5. **DELETE**
- Used to delete a resource.
- Example:
  ```python
  def delete_product(request, pk):
      product = Product.objects.get(id=pk)
      product.delete()
      return redirect("product_list")
  ```
  
## Cues Section
- What is the difference between **PUT** and **PATCH**?
  - **PUT** updates the entire resource, requiring all fields.
  - **PATCH** updates only the specified fields, keeping the rest unchanged.
- Why does **POST** require CSRF protection?
  - To prevent Cross-Site Request Forgery attacks, ensuring that only legitimate requests are processed.
- When should **DELETE** be used?
  - When a resource needs to be removed permanently from the database.
- How can you handle multiple methods in one view?
  ```python
  from django.views.decorators.http import require_http_methods

  @require_http_methods(["GET", "POST"])
  def product_view(request):
      # Handle GET and POST requests only
  ```

## Summary Section
- **GET** → Retrieve data without modifying it.
- **POST** → Create new data (forms, submissions).
- **PUT** → Update an entire resource.
- **PATCH** → Partially update a resource.
- **DELETE** → Remove a resource.
- Django views primarily use **GET** and **POST**.
- **PUT, PATCH, DELETE** are useful for APIs in Django REST Framework.
- Use `@require_http_methods` to restrict views to specific methods.


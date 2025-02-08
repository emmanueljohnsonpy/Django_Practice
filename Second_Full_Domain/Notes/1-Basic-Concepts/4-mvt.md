# MVT in Django (Cornell Method)

## What is MVT?
MVT (Model-View-Template) is Django’s software design pattern that separates concerns in web applications. It helps in maintaining clean and scalable code by organizing logic into three main components: Model, View, and Template.

## Notes Section

### 1. **Model**
- Represents the database structure and data logic.
- Defined using Django’s ORM (Object-Relational Mapping).
- Example:
  ```python
  from django.db import models
  
  class Product(models.Model):
      name = models.CharField(max_length=255)
      price = models.DecimalField(max_digits=10, decimal_places=2)
  ```

### 2. **View**
- Handles business logic and interacts with the model.
- Receives user requests and returns a response.
- Example:
  ```python
  from django.shortcuts import render
  from .models import Product
  
  def product_list(request):
      products = Product.objects.all()
      return render(request, "products.html", {"products": products})
  ```

### 3. **Template**
- Responsible for presenting data to users.
- Uses Django’s template language for dynamic content.
- Example (`products.html`):
  ```html
  <ul>
      {% for product in products %}
          <li>{{ product.name }} - ${{ product.price }}</li>
      {% endfor %}
  </ul>
  ```

## Cues Section
- What is the role of the **Model**?
  - Defines the structure of database tables and handles data operations.
- How does the **View** interact with the **Model**?
  - The View fetches data from the Model and passes it to the Template for rendering.
- What is the purpose of the **Template**?
  - Displays data dynamically using Django’s template syntax.
- Can a Django project have multiple Models and Views?
  - Yes, large applications consist of multiple Models and Views to handle different functionalities.

## Summary Section
- **Model** → Defines data structure and database operations.
- **View** → Handles business logic and interacts with the model.
- **Template** → Presents data to users in a structured format.
- The MVT pattern keeps Django applications organized and maintainable.
- Django’s built-in ORM simplifies database interactions within the Model component.


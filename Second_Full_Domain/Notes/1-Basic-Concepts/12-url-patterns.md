
# URL Patterns in Django (Cornell Method)

## Cue Column (Key Points):
- URL Patterns map HTTP requests to views in Django.
- Defined in the `urls.py` file.
- Each pattern consists of a URL path and a view function.
- Use `path()` or `re_path()` to define URLs.
- URL patterns can include parameters to capture dynamic values.

## Note-Taking Area (Details/Notes):

### What are URL Patterns?
URL patterns in Django are used to route incoming web requests to the appropriate view functions that handle those requests. Each URL pattern is tied to a specific view that processes the request and returns an HTTP response.

### Basic Syntax:
In the `urls.py` file, URL patterns are defined as a list, where each pattern maps a URL path to a view function.
```python
from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home_view, name='home'),
    path('products/<int:id>/', views.product_detail, name='product_detail'),
]
```
Here:
- `'home/'` maps to the `home_view` function.
- `<int:id>` captures the `id` as a parameter and passes it to the `product_detail` view.

### Common URL Functions:
- `path()`: Used for simple URL patterns.
    - Example: `path('about/', views.about_view)`
  
- `re_path()`: Uses regular expressions for more complex patterns.
    - Example: `re_path(r'^product/(\d+)/$', views.product_detail)`
  
### Dynamic URL Patterns:
You can use dynamic URL patterns by capturing values within the URL.
- Example: `path('category/<slug:slug>/', views.category_view)`, where `slug` is passed as an argument to the view.

### URL Parameters:
Django allows you to define URL patterns with parameters (also known as converters). These parameters can be passed into the corresponding view functions.
- Example: `path('product/<int:id>/', views.product_detail)`
- This captures an integer `id` in the URL and passes it to the `product_detail` view as an argument.

### Named URLs:
You can assign names to URL patterns using the `name` argument. This helps in reverse URL resolution, allowing you to generate URLs dynamically in templates or views.
- Example: `path('home/', views.home_view, name='home')`
- In templates: `{% url 'home' %}`.

## Summary Section (Summary):
URL patterns are essential in Django to map incoming requests to the appropriate views. They can be simple or dynamic, allowing for parameterized routes. By naming URLs, Django allows you to easily refer to routes in templates or redirect functions.
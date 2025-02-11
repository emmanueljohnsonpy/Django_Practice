
# Database Connection in Django (Cornell Method)

## Key Points
- Django uses an Object-Relational Mapping (ORM) system.
- Connects to a database using database settings in `settings.py`.
- Database connection is made via Django’s `DATABASES` setting.
- The `DATABASES` dictionary is where database configurations are stored.

## Detailed Notes

### 1. Database Setup in Django
- Django supports several databases like SQLite (default), PostgreSQL, MySQL, and Oracle.
- In `settings.py`, the `DATABASES` dictionary is used to configure the database. Here’s an example:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'mydatabase',
        'USER': 'myuser',
        'PASSWORD': 'mypassword',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

- **`ENGINE`**: Specifies the backend database (e.g., PostgreSQL, MySQL, SQLite).
- **`NAME`**: The name of the database.
- **`USER`**: The username for the database.
- **`PASSWORD`**: The password for the user.
- **`HOST`**: The database server's address, usually `localhost` for development.
- **`PORT`**: The port where the database is running (5432 for PostgreSQL).

### 2. Running Migrations
- After setting up the database, you need to run migrations to create the database schema based on your models.
- Use the following commands to apply migrations:

    ```
    python manage.py migrate
    ```

- This creates the necessary tables based on your defined models.

### 3. Database Queries in Django
- Django ORM allows querying the database with Python code, which abstracts SQL queries.
- Example of querying the database:
    ```python
    from myapp.models import Product
    products = Product.objects.all()  # Fetches all products
    ```

### 4. Using Multiple Databases
- Django can be configured to use multiple databases by modifying the `DATABASES` setting to include additional database configurations.
- This is useful in scenarios like read-write separation or database sharding.

### 5. Testing Database Connections
- It’s important to ensure that the database connection works properly. This can be done by checking logs or using the `python manage.py dbshell` command (if the database shell is configured).

## Summary
- In Django, database connection is handled via the `DATABASES` setting in `settings.py`, where you define the database engine, name, user credentials, and host information.
- After configuring the database, you run migrations to create tables based on your models.
- Django ORM simplifies database queries by allowing you to use Python code instead of raw SQL.
# Django Settings - Cornell Method

## Cue Column:
- Django settings overview
- Configuration files
- Important settings
- Static and media files
- Database settings
- Debug mode
- Security settings

---

## Note-taking Column:

### 1. Overview of Django Settings:
   - `settings.py` is the main configuration file in a Django project.
   - Stores various settings like database configurations, static file locations, security, and middleware settings.
   
### 2. Configuration of Different Settings:
   - **DEBUG:** A boolean setting that controls whether Django runs in debug mode. It should be `True` in development and `False` in production.
   - **DATABASES:** A dictionary containing database configuration. The default is SQLite, but you can configure other databases like PostgreSQL, MySQL, etc.
   - **STATIC_URL and MEDIA_URL:** Define the URL paths for static files (CSS, JS) and media files (uploads).
   - **INSTALLED_APPS:** A list of all Django apps and third-party apps used in the project.
   - **MIDDLEWARE:** A list of middleware components that process requests globally, like security, session management, etc.
   - **TEMPLATES:** Configuration for template engines that render HTML files.
   - **AUTHENTICATION_BACKENDS:** Determines how Django authenticates users.

### 3. Important Settings:
   - **ALLOWED_HOSTS:** Defines a list of valid hostnames or IP addresses that Django will allow to connect to the application.
   - **SECRET_KEY:** A randomly generated string used to provide cryptographic signing, ensuring security for various parts of Django.
   - **LANGUAGE_CODE and TIME_ZONE:** Controls the default language and timezone for the project.
   - **CSRF_COOKIE_SECURE:** Defines if CSRF tokens should only be transmitted over HTTPS.

### 4. Static and Media Files:
   - **STATICFILES_DIRS:** Allows you to specify directories for static files.
   - **MEDIA_ROOT and MEDIA_URL:** Set the root path where uploaded files will be stored and the URL used to serve them.

### 5. Security Settings:
   - **CSRF_COOKIE_SECURE:** Ensures that CSRF cookies are only sent over HTTPS.
   - **SESSION_COOKIE_SECURE:** Ensures that session cookies are only sent over HTTPS.
   - **X_FRAME_OPTIONS:** Prevents clickjacking attacks by controlling whether the site can be embedded in a frame.

---

## Summary Section:

Django settings configure various aspects of a project, including databases, static files, authentication, and security. Key settings like `DEBUG`, `DATABASES`, and `INSTALLED_APPS` ensure proper functionality during development and production. Proper configuration of security settings (like CSRF, session cookies, and secret key) is crucial to safeguard the application.

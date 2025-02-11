# Django Migrations (Cornell Method)

---

## **1. Topic: Django Migrations**  

**Definition:**  
Django migrations are a way of managing changes to the database schema over time. They allow you to modify your database structure without losing existing data.

---

## **2. Cues / Keywords**  
- What are migrations?  
- Why do we need migrations?  
- How to create and apply migrations?  
- Django migration commands  
- Common migration issues and solutions  

---

## **3. Notes**  

### **What are Migrations?**  
- Migrations are files that track changes made to Django models.  
- They help synchronize database structure with the models in your project.  
- They act as version control for database schema modifications.  

### **Why Do We Need Migrations?**  
- **Keeps database in sync** with model changes.  
- **Ensures smooth modifications** to database structure without data loss.  
- **Supports version control** for database structure, making collaboration easier.  
- **Allows rollbacks** if changes cause issues.  

### **Creating and Applying Migrations**  
Whenever you make changes to your Django models (like adding a new field or modifying an existing one), follow these steps:  

1. **Create Migration Files** (migration files in Django translate model changes into database instructions in the form of Python files)  
   ```bash
   python manage.py makemigrations
   ```
   - This creates migration files inside the **migrations/** folder of each app.  
   - Example migration file: `0001_initial.py`, `0002_add_field.py`  

2. **Apply Migrations to the Database**  
   ```bash
   python manage.py migrate
   ```
   - This applies the migration to the actual database.  

### **Django Migration Commands**  

| Command | Description |
|---------|-------------|
| `python manage.py makemigrations` | Creates migration files for model changes. |
| `python manage.py migrate` | Applies migrations to the database. |
| `python manage.py showmigrations` | Lists all migrations and their applied status. |
| `python manage.py sqlmigrate <app_name> <migration_number>` | Shows the SQL commands of a migration. |
| `python manage.py makemigrations --merge` | Merges conflicting migrations. |

### **Common Migration Issues & Fixes**  

| Issue | Cause | Solution |
|--------|--------|----------|
| **Migrations not applied** | You forgot to run `migrate`. | Run `python manage.py migrate`. |
| **Migration conflicts** | Multiple developers made conflicting changes. | Run `python manage.py makemigrations --merge`. |
| **Database changes not reflecting** | Migrations were not created properly. | Delete unnecessary migration files and recreate using `makemigrations`. |
| **Table already exists error** | Manual database modification conflicts with Django migrations. | Fake migrations: `python manage.py migrate --fake`. |
| **Unknown column error** | Schema mismatch between models and database. | Run `migrate` again or check for missing fields in the database. |

---

## **4. Summary**  

- Migrations manage database changes in Django automatically.  
- Use `makemigrations` to generate migration files and `migrate` to apply them.  
- Django provides useful commands to track, view, and resolve migration issues.  
- Proper handling of migrations ensures smooth database operations without errors.  

## Chapter 04: Message Board App - Documentation

### Summary of What I Learned

In Chapter 04 of "Django For Beginner," I learned how to create a simple blog application named Post. The process involved the following steps:

1. **Creating Models and Migrations:**
   - I created the model for the Post app and generated the necessary migration files.

2. **Creating a Superuser for Django Admin:**
   - I created a superuser to access the Django Admin interface.

3. **Displaying Post Model in Django Admin:**
   - I added the Post model to the Django Admin interface.
   - I included a `__str__` method in the Post model to make it easier to read the data entries on the admin page, instead of displaying default strings like "Post object (1)." It is recommended to always add a `__str__` method to all models.

4. **Creating Views with Generic Class-Based Views:**
   - I used the `ListView` generic class-based view to display data from the database in the `home.html` template.

### Superuser Credentials

For the superuser account I created, the credentials are as follows:
- **Username:** utrodus
- **Password:** @qwe12345

### To-Do Checklist

- [x] Learn to create models and migrations
- [x] Create a superuser for Django admin
- [x] Display Post models in Django admin
- [x] Create a view with `ListView` to show data from the database
- [x] Define a base template and extend it in other templates
- [x] Experiment with using pico.css for styling
- [x] Define static URL and root in `djangoproject/settings.py`
- [x] Generate static files for admin using the `collectstatic` command
- [x] Implement unit testing in Django using `TestCase`

### Useful Commands in This Chapter

- **Create migration for a specific app:**
  ```bash
  python manage.py makemigrations posts
  ```

- **Run migrations:**
  ```bash
  python manage.py migrate
  ```

- **Create a superuser for Django Admin:**
  ```bash
  python manage.py createsuperuser
  ```
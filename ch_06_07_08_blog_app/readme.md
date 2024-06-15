## Chapter 06: Blog App - Documentation

### Summary of What I Learned

In Chapter 06, I learned how to build a simple blog application that utilizes relational databases and static files for templates. Here are the key concepts I covered:

1. **Relational Database and Django's ORM:**
   - I learned about relational databases and how to use Django's ORM (Object-Relational Mapper).
   - I created a `Post` table and related it to Django's built-in `User` table using primary and foreign keys.

2. **get_absolute_url() Method:**
   - I learned how to use the `get_absolute_url()` method in models to generate URLs for displaying detailed data of a post.

3. **Managing Static Files:**
   - I studied how to manage and store static files (including CSS and JavaScript) in Django.

4. **Unit Testing:**
   - I learned how to perform unit testing in Django using `TestCase`.

5. **Styling with Bootstrap:**
   - I used Bootstrap for styling the blog application.
   - I structured the templates using inheritance to keep the code clean and maintainable.

### Superuser Credentials

For the superuser account I created, the credentials are as follows:
- **Username:** utrodus
- **Password:** @qwe12345

### Demo

Here is a demo video of the simple blog application I developed: [Demo Video](https://jam.dev/c/52b72119-23f6-4baf-89f9-b0cf5ef290c2)

### To-Do Checklist

- [x] Learn about relational databases and Django's ORM
- [x] Create and relate `Post` and `User` tables
- [x] Implement the `get_absolute_url()` method in models
- [x] Manage and store static files in Django
- [x] Use Bootstrap for styling
- [x] Structure templates using inheritance
- [x] Perform unit testing using `TestCase`

### Useful Commands in This Chapter

- **Create migration for the `Post` model:**
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

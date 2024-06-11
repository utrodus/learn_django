from django.db import models


class Post(models.Model):
    text = models.TextField()
    description = models.TextField(default="No description")

    # the method __str__ is used to django admin to display the text of the post
    # instead of the default 'Post object (1)'.
    # The method returns the first 50 characters of the text of the post.
    def __str__(self):
        return self.text[:50]

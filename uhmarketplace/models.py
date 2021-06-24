from django.db import models


class Uhmarketplace(models.Model):
    book_title = models.CharField(max_length=80)
    book_author = models.CharField(max_length=80)
    course = models.CharField(max_length=80)
    updated_on = models.DateTimeField(auto_now= True)
    content = models.CharField(max_length=300)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.book_title
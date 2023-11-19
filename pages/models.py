from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
# from django.conf import settings


# class Post(models.Model):
#     title = models.CharField(max_length=300, null=True)
#     category = models.CharField(max_length=300)
#     User = models.ForeignKey(User, on_delete=models.CASCADE)
#     body = models.TextField()
#     duration = models.CharField(max_length=100)
#     timestamp = models.DateField(auto_now_add=True)
#     updated = models.DateTimeField(auto_now=True)

#     image = models.ImageField(
#         upload_to="uploads",
#         null=True,
#     )

#     def __str__(self):
#         return self.title

#     def get_absolute_url(self):
#         return reverse("home")


# class Category(models.Model):
#     name = models.CharField(max_length=200, blank=True)

#     def __str__(self):
#         return self.name


# class Comment(models.Model):
#     comment = models.CharField(max_length=100, null=True)

#     def __str__(self):
#         return self.comment

#     def get_absolute_url(self):
#         return reverse("home")


# class Student(models.Model):
#     name = models.CharField(max_length=50)
#     avatar = models.ImageField(upload_to="uploads", null=True)


# def __str__(self):
#     return self.title

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)
    Is_task_complete_skip_if_no = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)
    

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.Is_task_complete_skip_if_no

    class Meta:
        ordering = ['Is_task_complete_skip_if_no']    


class Note(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    Is_note_complete_skip_if_no = models.BooleanField(default=False)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title
    
    def __str__(self):
        return self.Is_note_complete_skip_if_no

    class Meta:
        ordering = ['Is_note_complete_skip_if_no']    
        


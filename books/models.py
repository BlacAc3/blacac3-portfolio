# from typing import Any
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.

#shelf table
#---------------------------------------------------------------
class Book_shelf(models.Model):
    BOOK_STATUS=[
        ("not_started", "Not Started"),
        ("reading", "Currently Reading"),
        ("finished", "Finished Reading"),
    ]
    
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="my_books")
    book_id=models.TextField()
    title=models.TextField()
    authors=models.TextField()
    imageLink=models.TextField(blank=True)
    description=models.TextField(blank=True)
    publishedDate=models.TextField(blank=True)
    publisher=models.TextField(blank=True)
    pagesNumber=models.IntegerField(default=0)
    timestamp=models.DateTimeField(default=timezone.now)
    status=models.TextField(max_length=50, choices=BOOK_STATUS, default="not_started")
    

    def __str__(self):
        return f"Title: {self.title}"



#Collection Folder
#-------------------------------------------------------
class Collection_name(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="collection_name", default=None)
    name=models.TextField()
    def __str__(self):
        return f"Folder Name: {self.name}"




#Collection Content
# ------------------------------------------------------------------
class  Collection(models.Model):
    id=models.AutoField(primary_key=True)
    folder=models.ManyToManyField(Collection_name, related_name="content")
    books=models.ForeignKey(Book_shelf, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return f"Folder Lists: Book{self.books}"



#Notes table
#-----------------------------------------------------------------------------------------------
class Notes(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="notes", default=None)
    book=models.ForeignKey(Book_shelf, on_delete=models.CASCADE, related_name="notes")
    title=models.TextField()
    content=models.TextField()
    dateTime=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Book: {self.book.title}, Note Title: {self.title}"



#Book Reviews Table
#-----------------------------------------------------------------------------------------------------------
class Book_reviews(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="userReviews")
    bookId=models.TextField()
    title=models.TextField()
    content=models.TextField()
    dateTime=models.DateTimeField(default=timezone.now)
    def __str__(self):
        return f"Books: {self.bookId}, Review: {self.title}, review content: {self.content} by {self.user.username}"





#List of users that have their shelves public
#--------------------------------------------------------------------------------------------- 
class PublicShelf(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE, related_name="public")
    def __str__(self):
        return f"Shelf: by user:{self.user.username}"
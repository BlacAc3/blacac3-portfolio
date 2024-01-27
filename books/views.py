from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from django.db import IntegrityError
import random
import re
from . models import *
from  .get_api_data import *

from django.views.decorators.cache import cache_page


login_url = "login_render"


# Create your views here.
@login_required(login_url=login_url)
def index(request):
    user= request.user
    return render(request, "books/index.html",{
        "user":user,
    })


# register function
def register_render(request):
    if request.method!="POST":
        return render(request, "books/register.html")
    # assigning variables
    username= request.POST.get("username")
    email=request.POST.get("email")
    password=request.POST.get("password")
    confirmPassword = request.POST["confirm_password"]

    # Verify password
    if password != confirmPassword:
        return render(request, "books/register.html",{
            "mess":"Passwords do not Match!",
            "username":username,
            "email":email,
            })
    
    
    #checking if user already exists
    try:
        user=User.objects.create_user(username=username, email=email, password=password)
        user.save()
    except IntegrityError:
        return render(request, "books/register.html", {
            "mess": f"Username: {username}, Already exists.",
            "username":username,
            "email":email,
        })
    #if so login user
    login(request, user)
    return redirect("index")
        

#login te user if conditions are met
def login_render(request):
    if request.method != "POST":
        return render(request, "books/login.html")
    # assigning variables
    username= request.POST.get("username")
    password=request.POST.get("password")

    # verify if user exists
    user=authenticate(request, username=username, password=password )
    if user is not None:
        login(request, user)
        return redirect("index")
    else:
        mess="Invalid Username or Password"
        return render(request, "books/login.html", {
            "mess":mess,
        })
    

# logout function
def logout_function(request):

    logout(request)
    return HttpResponseRedirect(reverse(index))

def latest_books(request):
    #a randomizer that gets random letters and searches the latest result on the query of that letter
    alphabets="abcdefghijklmnopqrstuvwxyz"
    randomLetter=random.choice(alphabets)
    
    # maximum Number is 40 
    book_info=get_books(randomLetter, 40, "newest", "title")
    return render (request, "books/book_list.html", {
            "title":"Latest!",
            "books":book_info,
            "user":request.user,
            "total":len(book_info),
        })



# ---------------------------------------------------------------------------------
# view the book details
@cache_page(10 *60)
def view_book(request, book_id):
    user=request.user
    book_api_url=f"https://www.googleapis.com/books/v1/volumes/{book_id}"
    # calls a function that compiles the data and returns it
    book= compile_api_data(book_api_url)
    status_in_shelf=Book_shelf.objects.filter(book_id=book_id).exists()
    bookReviews=Book_reviews.objects.filter(bookId=book_id)
    return render (request, "books/book_view.html", {
        "book":book,
        "shelf_status":status_in_shelf,
        "user":request.user,
        "reviews":bookReviews,
    })


#------------------------------------------------------------------------------------------------
#render shelf page
@login_required(login_url=login_url)
def shelf_view(request):
    user=request.user
    user_shelfList=Book_shelf.objects.select_related("user").filter(user=user).order_by("-timestamp")
    not_started=Book_shelf.objects.filter(user=user, status="not_started").order_by("-timestamp")
    reading=Book_shelf.objects.filter(user=user, status="reading").order_by("-timestamp")
    finished=Book_shelf.objects.filter(user=user, status="finished").order_by("-timestamp")
    collection_list=Collection_name.objects.filter(user=user)
    public=False
    if user.public.all():
        public=True
    
    return render(request, "books/shelf.html", {
    "all":user_shelfList,
    "not_started":not_started,
    "reading":reading,
    "finished":finished,
    "total":user_shelfList.count(),
    "collections":collection_list,
    "public":public,
    })

# ------------------------------------------------------------------------------------------------------------------
#Search by book function
@login_required(login_url=login_url)
def book_search(request):
    term=request.POST.get("searchTerm")
    books=get_books(term, 40, "relevance", "title")
    return render(request, "books/book_list.html", {
        "title":"Results!",
        "books":books,
    })

# ---------------------------------------------------------------------------------------------------------------------------------
#Search by author function
@login_required(login_url=login_url)    
def author_search(request):
    term=request.POST.get("searchTerm")
    books=get_books(term, 40, "relevance", "author")
    return render(request, "books/book_list.html", {
        "title":"Results!",
        "books":books,
    })

# ----------------------------------------------------------------------------------------------------------
# Creates a new collection based on the collection name provided in the request and saves it. 
@login_required(login_url=login_url)
def createCollection(request):  # sourcery skip: use-named-expression
    user=request.user
    collectionNameRaw=request.POST.get("collectionName")
    collectionName=collectionNameRaw.lower()
    nameExists=Collection_name.objects.filter(user=user, name=collectionName).exists()
    if not collectionNameRaw :
        return redirect("shelf_view")
    if nameExists:
        return redirect("shelf_view")
    new_folder=Collection_name(user=user, name=collectionName)
    new_folder.save()
    return redirect("shelf_view")


@login_required(login_url=login_url)
#add to collection function
def addToCollection(request):  # sourcery skip: use-named-expression
    # assign variables 
    if request.method == "GET":
        collectionId= request.GET.get("collectionId")
        bookId=request.GET.get("bookId")
        user=request.user

        folderName=Collection_name.objects.get(user=user, id=collectionId)
        book=Book_shelf.objects.get(user=user, book_id=bookId)
        collectionExists=Collection.objects.filter(folder=folderName, books=book)
        if collectionExists:
            return JsonResponse({"data":"Book already exists in collection!"})
        #adding collection
        NewCollectionFolder=Collection(books=book)
        NewCollectionFolder.save()
        NewCollectionFolder.folder.add(folderName)
        NewCollectionFolder.save()
        return JsonResponse({"Yes":"Perfect"})
    

# remove from collection function
def removeFromCollection(request, id):
    user=request.user
    collection_name=Collection_name.objects.get(user=user, id=id)
    collection=Collection.objects.filter(folder=collection_name)
    if not collection_name:
        return redirect("shelf_view")
    collection_name.delete()
    collection.delete()
    return redirect("shelf_view")
    

# view collections function 
@cache_page(5)
def collection_view(request, collectionId):
    user=request.user
    collection_name=Collection_name.objects.get(user=user, id=collectionId)
    collection_books=Collection.objects.filter(folder=collection_name)
    collection_list=Collection_name.objects.filter(user=user)
    mess = "" if collection_books else "Oops! could not find any books"
    collection_title=collection_name.name
    return render(request, "books/collections.html", {
        "collection_books":collection_books,
        "collections":collection_list,
        "mess":mess,
        "collection_title":collection_title,
    })

# renders the note creation page with certain features as coded below
@login_required(login_url=login_url)
def notes_create(request):
    user=request.user
    all_books_title=Book_shelf.objects.filter(user=user).order_by("title")
    all_book_notes=Notes.objects.filter(user=user).order_by("-dateTime")
    NewCreationMode=True
    bookId=None

    #search feature to get the search result and render
    if request.method== "POST":
        searchTerm=request.POST["searchTerm"]
        all_books_title=shelfSearch(user, searchTerm)
    
    #redirects and renders edit note directly from shelf page with the appropriate book selected
    if request.method=="GET":
        bookId=request.GET.get("bookId")
        
    return render(request, "books/notes_create_edit.html",{
        "book_titles":all_books_title,
        "notes":all_book_notes,
        "selectId":bookId,
        "creationMode":NewCreationMode,
    })

# function that returns a search result of books in the  shelf
def shelfSearch(user, term):
    all_books_title=Book_shelf.objects.filter(user=user).order_by("title")
    book_searchResult=[]
    for book in all_books_title:
        if result := re.search(term, book.title, re.IGNORECASE):
            book_searchResult.append(book)
    return book_searchResult

#this function creates a new note
@login_required(login_url=login_url)
def addNote(request):
    if request.method=="POST":
        user=request.user
        title=request.POST.get("note_title")
        content=request.POST.get("note_content")
        bookId=request.POST.get("bookId")
        book=Book_shelf.objects.get(user=user, book_id=bookId)
        
        newNote=Notes(user=user, book=book, title=title, content=content)
        newNote.save()
    return redirect("viewNote", noteId=newNote.id)

#function deletes notes
def deleteNote(request, noteId):
    user=request.user
    note=Notes.objects.get(user=user, id=noteId)
    note.delete()
    return redirect("notes")

#function to edit an already created note 
def editNote(request, noteId):
    user=request.user
    note=Notes.objects.get(id=noteId)
    if request.method=="POST":
        title=request.POST.get("note_title")
        content=request.POST.get("note_content")
        note.title=title
        note.content=content
        note.save()
    return redirect("viewNote", noteId=noteId)

#renders a html page that view a note
def viewNote(request, noteId):
    user=request.user
    all_book_notes=Notes.objects.filter(user=user).order_by("-dateTime")
    note=Notes.objects.get(id=noteId)
    return render(request, "books/notes_view.html",{
        "notes":all_book_notes,
        "currentNote":note,
        "viewMode":True,
    })

#renders all notes for a particular book
def book_notes(request, bookId):
    user=request.user
    book=Book_shelf.objects.get(user=user, book_id=bookId)
    all_book_notes=Notes.objects.filter(user=user).order_by("-dateTime")
    notes=Notes.objects.filter(user=user, book=book).order_by("-dateTime")

    return render(request, "books/1_book_all_notes.html", {
        "book_notes":notes,
        "notes":all_book_notes,
        "book":book,
    })

# renders a html but with an editing setup with inputs prefilled instead of as viewing setup
def edit_note_render(request, noteId):
    user=request.user
    edit_note=Notes.objects.get(user=user, id=noteId)
    all_book_notes=Notes.objects.filter(user=user).order_by("-dateTime")
    note_edit_mode=True
    return render(request, "books/notes_create_edit.html", {
        "note_edit_mode":note_edit_mode,
        "notes":all_book_notes,
        "editedNote":edit_note,
        })


def add_review(request,bookId):
    user=request.user
    if request.method=="POST" and user.is_authenticated:
        user=request.user
        title=request.POST.get("reviewTitle")
        content=request.POST.get("reviewContent")
        review=Book_reviews(user=user, bookId=bookId, title=title, content=content)
        review.save()
    return redirect("view_book", book_id=bookId)
    


@login_required(login_url=login_url)
def publicShelf(request):
    publicShelves=PublicShelf.objects.all()
    currentUser=request.user
    return render(request, "books/publicShelf.html", {
        "shelves":publicShelves,
        "currentUser":currentUser,
    })
from django.urls import path
from . import views
from . import JS_functions

urlpatterns=[
    # index or main or original path 
    path("", views.index, name="index"),
    
    # user login and authentication paths 
    path("login", views.login_render, name="login_render"),
    path("register", views.register_render, name="register_render"),
    path("logout", views.logout_function, name="logout"),

    #rendering html files
    path("latest", views.latest_books, name="latest_page"), #latest Page rendering
    path("book/<str:book_id>", views.view_book, name="view_book"), #viewing a particular book
    path("shelf", views.shelf_view, name="shelf_view"), #rendering a shelf page
    path("my-notes/", views.notes_create, name="notes"), #render notes creation page
    path("collections/<str:collectionId>", views.collection_view, name="collections"), #view books in a particular function
    path("public/shelves", views.publicShelf, name="publicShelf"),

    #Functions called by javascript 
    path("add-to-shelf/",JS_functions.add_to_shelf, name="add_to_shelf"), #add book to shelf
    path("remove-from-shelf/",JS_functions.remove_from_shelf, name="remove_from_shelf"), #remove book from shelf
    path("shelf-check/", JS_functions.shelf_check, name="shelf"), #check if book is added to shelf or not
    path("add-to-reading/", JS_functions.add_to_reading, name="add-to-reading"), # add book to reading status
    path("add-to-finished/", JS_functions.add_to_finished, name="add-to-finished"), #add book to finished status
    path("add-to-not-started/", JS_functions.add_to_notStarted, name="add_to_not_started"),#add book to not started
    path("shelf/make-public", JS_functions.addToPublicShelf, name="makePublic"),

    #Search urls
    path("search", views.book_search, name="book_search"), #search for book by title
    path("search/author", views.author_search, name="author_search"), #search for book by Author

    #Collection-related functions
    path("cr8-col", views.createCollection, name="createCollection"), #create a collection
    path("add-to-col/", views.addToCollection, name="addToCollection"), #add a book to a collection
    path("remove/collection/<int:id>", views.removeFromCollection, name="removeFromCollection"),#remove a book from a collection

    #Note related Functions
    path("add-note", views.addNote, name="addNote"), #add a new note
    path("note/<int:noteId>", views.viewNote, name="viewNote"), #view a particular note
    path("book/<str:bookId>/notes", views.book_notes, name="book_notes"), #view all notes related to a particular book
    path("book/note/edit_view/<int:noteId>", views.edit_note_render, name="edit_note_render"),#an note creation url setup called directly from shelf with prefilled book title
    path("book/note/edit_<int:noteId>", views.editNote, name="edit_note"), #edit an already existing note
    path("book/note/<int:noteId>/delete", views.deleteNote, name="deleteNote"),#delete a note

    #Reviews
    path("book/<str:bookId>/add-review/", views.add_review, name="add_review"),#function to add a review to a book

]

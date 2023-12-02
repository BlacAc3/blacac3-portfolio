from .views import *

#add button function
@login_required
def add_to_shelf(request):
    user=request.user
    book_id=request.GET.get("id")
    book_api_url=f"https://www.googleapis.com/books/v1/volumes/{book_id}"
    book_data=compile_api_data(book_api_url)
    status_in_shelf=Book_shelf.objects.filter(user=user, book_id=book_id).exists()

    #check if book already exists in Shelf
    if not status_in_shelf:
        #add data to Shelf models
        new = Book_shelf(user=request.user,
            book_id=book_data["id"],
            title=book_data["title"],
            authors=book_data["authors"],
            imageLink=book_data["imageLinks"],
            description=book_data["description"],
            publishedDate=book_data["publishedDate"],
            publisher=book_data["publisher"],
        )
        new.save()    
    return JsonResponse({"Added to shelf":"Successful"})


#remove button function
@login_required
def remove_from_shelf(request):
    book_id=request.GET.get("id")
    book=Book_shelf.objects.filter(user=request.user ,book_id=book_id)
    #Delete 
    if book.exists():
        book.delete()
        return JsonResponse({"Removed from shelf":"Successful"})
    else:
        return JsonResponse({"Removed from shelf":"Successful", "Exists": "False"})


#ceck if book exists in shelf or not
@login_required
def shelf_check(request):
    if request.method == "GET":
        book_id=request.GET.get("id")
        if status_in_shelf := Book_shelf.objects.filter(
            user=request.user, book_id=book_id
        ).exists():
            return JsonResponse({"boolean":"True"}, safe=False)
        else:
            return JsonResponse({"boolean":"False"}, safe=False)

def add_to_reading(request):
    if request.method == "GET":
        user=request.user
        id = request.GET.get("id")
        book=Book_shelf.objects.get(user=user, book_id=id)
        book.status="reading"
        book.save()
        return JsonResponse({"Addition to reading":"Success"})
    
def add_to_finished(request):
    if request.method == "GET":
        user=request.user
        id = request.GET.get("id")
        book=Book_shelf.objects.get(user=user, book_id=id)
        book.status="finished"
        book.save()
        return JsonResponse({"Addition to finished":"Success"})
    
def add_to_notStarted(request):
    if request.method == "GET":
        user=request.user
        id = request.GET.get("id")
        book=Book_shelf.objects.get(user=user, book_id=id)
        book.status="not_started"
        book.save()
        return JsonResponse({"Addition to not Started":"Success"})
    

def addToPublicShelf(request):
    user=request.user
    userShelf=Book_shelf.objects.filter(user=user)
    if not userShelf:
        return redirect("publicShelf")
    if private := PublicShelf.objects.filter(user=user).exists():
        PublicShelf.objects.filter(user=user).delete()
        state="Private"
    else:
        public=PublicShelf.objects.create(user=user)
        public.save()
        state="Public"
    return JsonResponse({"comment":"Your Shelf is Public status Changed",
                        "state":state })
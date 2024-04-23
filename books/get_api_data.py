import requests

#function that sorts the api data into usable and needed data
def compile_api_data(book_api_url):
    response= requests.get(book_api_url)
    if response.status_code == 200:
        #convert data to json
        data = response.json()

        #getting all books information from the api
        vol=data.get("volumeInfo",{}) 
        id= data.get("id", "") ##Get Book's ID


        title=vol.get("title", "")
        authors=vol.get("authors","")
        imageLinks=vol.get("imageLinks",{}).get("smallThumbnail","")
        description=vol.get("description","")
        publishedDate=vol.get("publishedDate","")
        publisher=vol.get("publisher", "")
        pageCount=vol.get("pageCount","")
        
        book={
            "id":id,
            "title":title, 
            "authors":authors, 
            "imageLinks":imageLinks, 
            "description":description,
            "pageCount":pageCount,
            "publishedDate":publishedDate,
            "publisher":publisher,
            }
    return book



def get_books(term, max_results, orderBy, searchBy):
    #gets information from the api
    num=int(max_results)
    if searchBy == "title":
        api_url=f"https://www.googleapis.com/books/v1/volumes?q={term}&maxResults={num}&orderBy={orderBy}&key=AIzaSyCp2-aVDiBFoKQS2CpCES42vTgI7D4h_e8"
    elif searchBy == "author":
        api_url=f"https://www.googleapis.com/books/v1/volumes?q=+inauthor:{term}&maxResults={num}&orderBy={orderBy}&key=AIzaSyCp2-aVDiBFoKQS2CpCES42vTgI7D4h_e8"
    response=requests.get(api_url)


    if response.status_code == 200:
        data=response.json()
        items=data.get("items",[])
        book_info=[]

        #getting all books information from the api and adding them to my list
        for item in items:
            vol=item.get("volumeInfo",{})
            id= item.get("id", "")
            title=vol.get("title", "")
            authors=vol.get("authors","")
            imageLinks=vol.get("imageLinks",{}).get("smallThumbnail","")
            description=vol.get("description","")
            publishedDate=vol.get("publishedDate","")
            publisher=vol.get("publisher", "")
            pageCount=vol.get("pageCount","")

            #Skip iteration of books with no image links and or titles or descriptions(for better experience)
            if imageLinks is None:
                continue
            
            #Sorting information to be added to the list
            item={
                "id":id,
                "title":title, 
                "authors":authors, 
                "imageLinks":imageLinks, 
                "description":description,
                "pageCount":pageCount,
                "publishedDate":publishedDate,
                "publisher":publisher,
                }
            book_info.append(item)
        return book_info
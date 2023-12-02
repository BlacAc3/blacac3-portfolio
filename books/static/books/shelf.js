import { removeFromShelfFunction } from "./script.js";
document.addEventListener("DOMContentLoaded", ()=>{
let bookItemInnerMenu=document.querySelector(".book-menu");
const confirmationDiv=document.querySelector(".confirmation-div");
const yes=document.querySelector("#yes-confirmation");
const no =document.querySelector("#no-confirmation");


// book item menu toggle show and hide 
// -------------------------------------------------------------------------------------------------------------------------------------------
    let bookItemIcon=document.querySelectorAll(".shelf-more");
    let cancelMenu=document.querySelector(".cancel-menu");
    if (bookItemIcon && cancelMenu ){
        const bookItemMenu=document.querySelector(".book-menu-div");
        bookItemIcon.forEach(icon=>{
            icon.addEventListener("click",()=>{
                bookItemMenu.classList.toggle("menu-open")
                let iconId=icon.parentNode.id
                bookItemMenu.id=iconId
                console.log(bookItemMenu.id)
            })
        })

//Set shelf private or public toggle
//-------------------------------------------------------------------------------------------------------------------------------------------------
    let privateButton=document.querySelectorAll(".private-public-toggle")
    privateButton.forEach((button)=>{
        button.addEventListener("click", ()=>{
            let color = button.style.color;
            let background=button.style.background;
            button.style.cursor="not-allowed";
            button.innerHTML="Loading...";
            button.style.color="black";
            button.style.background="yellow";
            fetch("/shelf/make-public", {
                method:"GET",
            })
            .then(response=>response.json())
            .then(data=>{
                console.log(data);
                button.innerHTML=data.state;
                button.style.cursor="pointer";
                button.style.color=color;
                button.style.background=background;
            });
    })
    })

//buttons in book menu
// --------------------------------------------------------------------------------------------------------------------
        //cancel menu
        cancelMenu.addEventListener("click",()=>{
            bookItemMenu.classList.toggle("menu-open")
        })

        let cancelBookStatusSection= document.querySelector(".cancel-book-status-section");
        let bookStatusButton=document.querySelector("#book-status");
        let bookStatusSection=document.querySelector(".book-status-section-div");
        bookStatusButton.addEventListener("click", ()=>{
            bookStatusSection.classList.toggle("book-status-section-open")
            bookItemInnerMenu.classList.toggle("hide");
        })

        cancelBookStatusSection.addEventListener("click", ()=>{
            bookStatusSection.classList.toggle("book-status-section-open")
            bookItemInnerMenu.classList.toggle("hide");
        })

        
        
        //add to notStarted
        let addToNotStarted = document.querySelector("#menu-notStarted");
        addToNotStarted.addEventListener("click", ()=>{
            fetch(`/add-to-not-started/?id=${bookItemMenu.id}`, {
                method:"GET",
            })
            .then(response=>response.json())
            .then(data=>{
                console.log(data, "ace")
                window.location.reload()
            })
        })

        //add to reading button
        let addToReading = document.querySelector("#menu-current");
        addToReading.addEventListener("click", ()=>{
            fetch(`/add-to-reading/?id=${bookItemMenu.id}`,{
                method:"GET",
            })
            .then(response=>response.json())
            .then(data=>{
                console.log(data);
                window.location.reload()
            })
            
        })

        //add to finished button
        let addToFinished = document.querySelector("#menu-finish");
        addToFinished.addEventListener("click", ()=>{
            fetch(`/add-to-finished/?id=${bookItemMenu.id}`,{
                method:"GET",
            })
            .then(response=>response.json())
            .then(data=>{
                console.log(data)
                window.location.reload()
            })
            
        })



        //add to collection
        let collection_add_buttons = document.querySelectorAll(".collection_add_buttons")
        collection_add_buttons.forEach(button=>{
            button.addEventListener("click", ()=>{
                let collectionId=button.id
                    fetch(`/add-to-col/?bookId=${bookItemMenu.id}&collectionId=${collectionId}`,{
                    method: "GET",
                })
                .then(response =>response.json())
                .then(data=>{
                    console.log(data.Error)
                    window.location.reload()
                })
                .catch(error=>{
                    console.log(error)
                })
                
            })
        })


        // removing book from shelf button 
        let removeMenu=document.querySelector("#menu-remove");
        if (removeMenu){
            removeMenu.addEventListener("click", ()=>{
                confirmationDiv.classList.toggle("show-confirmation")
                yes.addEventListener("click", ()=>{
                    removeFromShelfFunction(bookItemMenu.id)
                    console.log("removed book with id:  " + bookItemMenu.id)
                })
            })
        }

        //Note creation
            //-------------------------------------------------------------------------------------------------------------
            let createNoteButton = document.querySelector("#create-notes")
            if (createNoteButton){
                createNoteButton.addEventListener("click",()=>{
                    let url = `/my-notes/?bookId=${bookItemMenu.id}`
                    window.location.href=url
                })
            }
        
    }

// collection adding javascript 
// --------------------------------------------------------------------------------------
let addToCollection=document.querySelector("#add-to-collection")
let addSection=document.querySelector(".add-collection-section-div")
let cancelAddCollectionSection=document.querySelector(".cancel-add-collection-section")
if (addToCollection){
    addToCollection.addEventListener("click", ()=>{
        addSection.classList.toggle("open-add-section")
        console.log("running")
        bookItemInnerMenu.classList.toggle("book-menu-hide")
    })
    cancelAddCollectionSection.addEventListener("click", ()=>{
        addSection.classList.toggle("open-add-section")
        bookItemInnerMenu.classList.toggle("book-menu-hide")
    })
}

// Collection creation
// -----------------------------------------------------------------------------------------------
let createCollection = document.querySelector(".add-collection");
let cancelCollectionButton = document.querySelector(".cancel-input-collection")
let collectionInput = document.querySelector("#collectionNameCreate")
if (createCollection){
    createCollection.addEventListener("click", ()=>{
        collectionInput.classList.toggle("open")
        console.log("Create Collection DIV opened!!")
    })
    cancelCollectionButton.addEventListener("click", ()=>{
        collectionInput.classList.toggle("open")
        console.log("Create Collection DIV closed!!")
    })
}
    

//Collection Deletion
// ---------------------------------------------------------------------------------------------------
let removeCollectionButton=document.querySelectorAll(".remove-collection") 
let removeCollectionMenu=document.querySelector(".removeCollectionMenu")
if (removeCollectionButton){
    removeCollectionButton.forEach((button)=>{
        button.addEventListener("click", ()=>{
            removeCollectionMenu.classList.toggle("removeCollectionMenuClose")
        })
    })
    
}





// sort buttons for single page js 
// --------------------------------------------------------------------------------------------------------------------------------------------------------

    let allShelfButton= document.querySelector("#all-shelf-button");
    let notStartedShelfButton=document.querySelector("#not_started-shelf-button");
    let readingShelfButton=document.querySelector("#reading-shelf-button");
    let finishedShelfButton= document.querySelector("#finished-shelf-button");

    
    // listeners
    if (allShelfButton){
        allShelfButton.addEventListener("click", ()=>{showSort(allShelfButton, "shelf-list")})
        notStartedShelfButton.addEventListener("click", ()=>{showSort(notStartedShelfButton, "not_started-shelf")})
        readingShelfButton.addEventListener("click", ()=>{showSort(readingShelfButton, "reading-shelf")})
        finishedShelfButton.addEventListener("click", ()=>{showSort(finishedShelfButton, "finished-shelf")})
    }
    // function for showing and hiding pages 
    function showSort(button, sectionId){
        let section = document.querySelector(`#${sectionId}`)
        let all= document.querySelectorAll(".all-books-shelf");
        let buttons= document.querySelectorAll(".tab-section li");

        // make all display none so the selected display alone can be visible 
        all.forEach(section=>{
            section.style.display="none";
        })
        
        //whiten other buttons anytime a button is clicked
        buttons.forEach((colorButton)=>{
            colorButton.style.background="rgb(255, 255, 144)";
            colorButton.style.color="black";
        }) 

        button.style.background="black";
        button.style.color="beige";

        section.style.display="flex";
        console.log(`Section:${sectionId} is now visible`)

    }
    
    
    
});
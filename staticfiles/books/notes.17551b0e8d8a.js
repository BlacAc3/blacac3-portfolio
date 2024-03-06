document.addEventListener("DOMContentLoaded", ()=>{

    let sideBar=document.querySelector(".notes-side-bar")
    let mainPage=document.querySelector(".notes-page")

    const confirmationDiv=document.querySelector(".confirmation-div");
    const yes=document.querySelector("#yes-confirmation");
    const no = document.querySelector("#no-confirmation");


    //notes list more section toggle code
    // ---------------------------------------------------------------------------------------------------------------------
    let sideBookItem = document.querySelectorAll(".side-book-item")
    let openMenu = "more-notes-section-open"
    sideBookItem.forEach((item)=>{
        let button=item.querySelector(".more-notes-button")
        let moreNotesSection=item.querySelector(".more-notes-section")

        button.addEventListener("click", ()=>{
            //hides the previous opened menus only in the current menu being asked for is closed
            if (!moreNotesSection.classList.contains(openMenu)){
                sideBookItem.forEach(book_item=>{
                    let sectionToCheck=book_item.querySelector(".more-notes-section")
                    //if div is open close all
                    if (sectionToCheck.classList.contains(openMenu)){
                        sectionToCheck.classList.toggle(openMenu);
                    }   
                })
            }
            //open the div
            moreNotesSection.classList.toggle(openMenu)
            
        })
    })

    // show sidebar of list of notes js code for mobile devices 
    let notesSideButton= document.querySelector(".notes-side-bar-button");
    if (notesSideButton){
        notesSideButton.addEventListener("click", ()=>{
            sideBar.classList.toggle("show")
        })
    }

    let searchShelf= document.querySelector("#search-notes-in-shelf");
    let noteSearchFunction= document.querySelector("#note-search-function");
    if (searchShelf){
        searchShelf.addEventListener("click", ()=>{
            noteSearchFunction.classList.toggle("searchNoteShow")
        })
    }
    
    // notes deletion
    let noteDeleteButton=document.querySelectorAll(".delete-note");
    if (noteDeleteButton) {
        noteDeleteButton.forEach((button)=>{
            button.addEventListener("click", function(){
                confirmationDiv.classList.toggle("show-confirmation");
                yes.addEventListener("click",()=>{
                    let noteId=button.id
                    window.location.href=`/projects/books/book/note/${noteId}/delete`;
                })
            })
            
        })
        no.addEventListener("click",()=>{
            confirmationDiv.classList.toggle("show-confirmation")
        })
        
    }
    
})

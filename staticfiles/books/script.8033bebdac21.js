// url parent setup for the main url
const url_parent = "/projects/books"


document.addEventListener("DOMContentLoaded", ()=> {
    const confirmationDiv=document.querySelector(".confirmation-div");
    const yes=document.querySelector("#yes-confirmation");
    const no = document.querySelector("#no-confirmation");
    

    // click backround to close code 
    let confirmDivContainer= document.querySelector(".confirmation-div")
    let confirmDiv= document.querySelector(".confirmation")
    confirmDivContainer.addEventListener("click", (e)=>{
        if (!confirmDiv.contains(e.target)){
            confirmDivContainer.classList.toggle("show-confirmation")
        }
    })

//Animation 
//--------------------------------------------------------------------------------------------
    const dots = document.querySelectorAll('.dot');
    const loadingDots = document.querySelector('.loading-dots');
    const mainBody = document.querySelector("#inner-body");
    let currentDotIndex = 0;
    const toggleDots= function() {
        dots[currentDotIndex].style.opacity = 0;
        currentDotIndex = (currentDotIndex + 1) % dots.length;
        dots[currentDotIndex].style.opacity = 1;
    }
    const removeLoadingAnimation=function() {
        loadingDots.style.display = 'none'; // Hide the loading animation
        mainBody.style.display="block";
    }
    // Add a listener for the 'DOMContentLoaded' event
    window.addEventListener('load', function () {
        // Stop the animation
        clearInterval(animationInterval);
        
        // Remove the loading animation
        removeLoadingAnimation();
    });
    const animationInterval = setInterval(toggleDots, Infinity);
// -------------------------------------------------------------------------------------------------------






// js code for navbar responsiveness
//---------------------------------------------------------------------------------------
    const navMenu=document.querySelector(".menu-icon");
    const mobileNav=document.querySelector(".mobile_nav");
    navMenu.addEventListener("click", ()=>{
        mobileNav.classList.toggle("show-nav");
    });

//--------------------------------------------------------------------------------------------------------------


// button handler for adding and removing books in shelf
// --------------------------------------------------------------------------------------------------------------------------
    let addToShelf= document.querySelector("#add-to-shelf");
    let removeFromShelf= document.querySelector("#remove-from-shelf");
    if (addToShelf){
        addToShelf.addEventListener("click",()=>{
            let bookContainer = document.querySelector(".book-viewing")
            let bookContainerId=bookContainer.id
            addToShelfFunction(bookContainerId)
        })};
    if (removeFromShelf){
        removeFromShelf.addEventListener("click", ()=>{
            let bookContainer = document.querySelector(".book-viewing")
            let bookContainerId=bookContainer.id
            confirmationDiv.classList.toggle("show-confirmation")
            yes.addEventListener("click", ()=>{
                removeFromShelfFunction(bookContainerId)
            })
        })};

    let bookContainer = document.querySelector(".book-viewing");
    if (bookContainer){
        shelfCheck()
        console.log("checked for book in shelf")
    }

// button handler for viewing review Section
// --------------------------------------------------------------------------------------------------------------
    let addReviewButton=document.querySelector("#add-review");
    let reviewFormSection=document.querySelector("#review-form");
    if (addReviewButton){
        addReviewButton.addEventListener("click", ()=>{
            reviewFormSection.classList.toggle("show-review-form");
        })
    }

    
// Search popup 
// ----------------------------------------------------------------------------------------------------
    let searchBar= document.querySelector(".searchbar-div")
    let searchBarInput=document.querySelector(".searchbar")
    let searchBarDiv=document.querySelector(".search-bar-div")
    let searchButton=document.querySelectorAll(".search-button")
    searchButton.forEach(button => {
        button.addEventListener("click", ()=>{
            searchBar.classList.toggle("search")
            console.log("Done: Search Bar is showing try")

            
        })
        
    });
    searchBar.addEventListener("click", (e)=>{
        console.log(e.target)
        if (!searchBarInput.contains(e.target)){
            searchBar.classList.toggle("search")
        }
    })
    
})



// --------------------------------------------------------------------------------------------------------------------------------------------------------------
// Functions
// ----------------------------------------------------------------------------------------------------------------------------------------------------------------------

// Check if an item is in shelf
function shelfCheck(){
    let addToShelf= document.querySelector("#add-to-shelf")
    let removeFromShelf= document.querySelector("#remove-from-shelf")
    let bookContainer = document.querySelector(".book-viewing")
    let bookContainerId=bookContainer.id
    

        //Fetch the url that leads to the views.py add view function 
        fetch(`${url_parent}/shelf-check/?id=${bookContainerId}`, {
            method: "GET",
        })
        .then(response=>response.json())
        .then (data=>{
            console.log(data.boolean)
            if (data.boolean === "True"){
                //Hide 
                addToShelf.style.display="none";
                removeFromShelf.style.display="block";
            }else{
                addToShelf.style.display="block";
                removeFromShelf.style.display="none";
            }
        })
        
}




//---------------------------------------------------------
//Add to Shelf Button
export function addToShelfFunction(bookContainerId) {

    let addToShelf= document.querySelector("#add-to-shelf");
    let removeFromShelf= document.querySelector("#remove-from-shelf");
    addToShelf.style.cursor="not-allowed";
    let text = addToShelf.innerHTML;
    addToShelf.innerHTML="Adding..."
    //Fetch the url that leads to the views.py add view function 
    fetch(`${url_parent}/add-to-shelf/?id=${bookContainerId}`, {
        method: "GET",
    })
    .then(response=>response.json())
    .then (data=>{
        console.log(data)
        addToShelf.style.display="none"
        addToShelf.innerHTML=text
        removeFromShelf.style.display="block"
    })
    .catch(error=>{
        console.log(error)
    })

    //Hide 
    
}

// ------------------------------------------------------------------------------------------
// Remove from shelf 
export function removeFromShelfFunction(bookContainerId) {
    let addToShelf= document.querySelector("#add-to-shelf")
    let removeFromShelf= document.querySelector("#remove-from-shelf")
    //Fetch the url that leads to the views.py add view function 
    fetch(`${url_parent}/remove-from-shelf/?id=${bookContainerId}`, {
        method: "GET",
    })
    .then(response=>response.json())
    .then (data=>{
        console.log(data)
        if (addToShelf){
            addToShelf.style.display="block"
            removeFromShelf.style.display="none"
        }
        window.location.reload()
    })
    .catch(error=>{
        console.log(error)
    })
    //Hide 
    
    
    


}


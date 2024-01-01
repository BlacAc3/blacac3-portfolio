document.addEventListener("DOMContentLoaded", ()=>{

    let navIcon = document.querySelector(".nav-menu-icon");
    let sidebar = document.querySelector("#sidebar-section");
    navIcon.addEventListener("click", ()=>{
        sidebar.classList.toggle("hide")
        console.log("hidden")
    })

    function showPopup(text) {
        const popup = document.getElementById('topPopup');
        const popupText =document.querySelector("#topPopup div")
        popupText.innerHTML = text;
        popup.style.display = 'flex';
        setTimeout(() => {
            popup.style.display = 'none';
        }, 3000); // Adjust the time the popup is displayed (in milliseconds)
    }
    
    // display popup for account number click event 
    let accountNumber = document.querySelector(".num");
    if (accountNumber){
        accountNumber.addEventListener("click", ()=>{
                let text= accountNumber.innerHTML
                showPopup(`Copied! ${text}`)
            })
    }
    

    //display popup when a user clicks receive
    let receiveButton= document.querySelector(".receive");
    receiveButton.addEventListener("click", ()=>{
        console.log("clicked")
        showPopup("Copy your account number By Clicking on it in your Profile Page")
    })

    //popup for transaction
    let sendButton = document.querySelector(".send")
    let modalContainer=document.querySelector(".modal-container-div")
    sendButton.addEventListener("click", ()=>{
        console.log("Send button Clicked")
        modalContainer.style.display="flex";
    })
    //close transaction popup
    let closeModal = document.querySelector(".modal-close-button")
    closeModal.addEventListener("click", ()=>{
        console.log("Closed transaction page")
        modalContainer.style.display="none";
    })

})

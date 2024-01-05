document.addEventListener("DOMContentLoaded", ()=>{
    let navIcon = document.querySelector(".nav-menu-icon");
    let sidebar = document.querySelector("#sidebar-section");
    if (navIcon){
        navIcon.addEventListener("click", ()=>{
            sidebar.classList.toggle("hide")
            console.log("hidden")
        })
    }
    

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
                showPopup(`Copied to Clipboard!`)
            })
    }
    

    //display popup when a user clicks receive
    let receiveButton= document.querySelector(".receive");
    if (receiveButton){
        receiveButton.addEventListener("click", ()=>{
            console.log("clicked")
            showPopup("Copy your account number By Clicking on it in your Profile Page")
        })
    }

    //popup for transaction
    let sendButton = document.querySelector(".send")
    let modalContainer=document.querySelector(".modal-container-div")
    if (sendButton){
        sendButton.addEventListener("click", ()=>{
            console.log("Send button Clicked")
            modalContainer.style.display="flex";
        })
    }

    //close transaction popup
    let closeModal = document.querySelector(".modal-close-button")
    if (closeModal){
        closeModal.addEventListener("click", ()=>{
            console.log("Closed transaction page")
            modalContainer.style.display="none";
        })
    }
        
    //show hide handler for login and registration page
    let logButton = document.querySelector("#log-section-button");
    let regButton = document.querySelector("#reg-section-button");
    let logSection = document.querySelector("#finance-log");
    let regSection = document.querySelector("#finance-reg");
    
    if (logButton){
        logButton.addEventListener("click", ()=>{
            console.log("click")
            if (logSection.classList.contains("hide") ){
                logSection.classList.remove("hide")
                regSection.classList.add("hide")
                console.log("Login section visible")
            }
        })
        regButton.addEventListener("click", ()=>{
            if (regSection.classList.contains("hide") ){
                regSection.classList.remove("hide")
                logSection.classList.add("hide")
                console.log("Registration section visible")
            }
        })
    }
})

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
    
    let accountNumber = document.querySelector(".num");
    accountNumber.addEventListener("click", ()=>{
        let text= accountNumber.innerHTML
        showPopup(`Copied! ${text}`)
    })

})

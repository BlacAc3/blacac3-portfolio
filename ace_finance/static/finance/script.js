document.addEventListener("DOMContentLoaded", ()=>{

    let navIcon = document.querySelector(".nav-menu-icon");
    let sidebar = document.querySelector("#sidebar-section");
    navIcon.addEventListener("click", ()=>{
        sidebar.classList.toggle("hide")
        console.log("hidden")
    })
    




})
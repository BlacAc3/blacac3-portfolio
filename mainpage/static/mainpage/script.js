document.addEventListener("DOMContentLoaded", ()=>{
    const mobileNavbar = document.querySelector(".mobile-nav");

    
    // click action for home navbar button
    let navHomeButtons = document.querySelectorAll(".nav-home");
    let homePage = document.querySelector(".home");
    navHomeButtons.forEach(item=>{
        item.addEventListener("click", ()=>{
            allNavClickable = document.querySelectorAll(".intro")
            allNavClickable.forEach(navItem => {
                navItem.style.display="none";
            });
            if (mobileNavbar.classList.contains("mobile-nav-show")){
                mobileNavbar.classList.remove("mobile-nav-show")
            }
            homePage.style.display="flex"
        })
        
    })

    // click action for navbar about button
    let navAboutButtons = document.querySelectorAll(".nav-about");
    let aboutPage = document.querySelector(".about");
    navAboutButtons.forEach(navAbout => {
        navAbout.addEventListener("click", ()=>{
            allNavClickable = document.querySelectorAll(".intro")
            allNavClickable.forEach(navItem => {
                navItem.style.display="none";
            });
            if (mobileNavbar.classList.contains("mobile-nav-show")){
                mobileNavbar.classList.remove("mobile-nav-show")
            }
            aboutPage.style.display="flex"
        })
    })

    // Click action button for certificate page
    let navCertButtons = document.querySelectorAll(".nav-cert");
    let certPage = document.querySelector(".cert");
    navCertButtons.forEach(navCert => {
        navCert.addEventListener("click", ()=>{
            allNavClickable = document.querySelectorAll(".intro")
            allNavClickable.forEach(navItem => {
                navItem.style.display="none";
            });
            if (mobileNavbar.classList.contains("mobile-nav-show")){
                mobileNavbar.classList.remove("mobile-nav-show")
            }
            certPage.style.display="flex"
        })
    })
    let navCert = document.querySelector(".intro button");
    let projectsPage = document.querySelector(".projects");
        navCert.addEventListener("click", ()=>{
            allNavClickable = document.querySelectorAll(".intro")
            allNavClickable.forEach(navItem => {
                navItem.style.display="none";
            });
            if (mobileNavbar.classList.contains("mobile-nav-show")){
                mobileNavbar.classList.remove("mobile-nav-show")
            }
            projectsPage.style.display="flex"
        
    })
    
    //click action for nav menu for better responsiveness
    let navMenu = document.querySelector(".nav-menu");
    navMenu.addEventListener("click", ()=>{
        mobileNavbar.classList.toggle("mobile-nav-show")
    })

    document.addEventListener('click', function(event) {

        // Check if the click is outside the div
        if (!navMenu.contains(event.target)) {
            // Hide the div or perform any other action
            mobileNavbar.classList.remove("mobile-nav-show")
        }
    });
    navMenu.addEventListener('click', function(event) {
        event.stopPropagation();
    });
    
    
})
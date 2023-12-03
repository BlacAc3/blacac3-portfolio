document.addEventListener("DOMContentLoaded", ()=>{
    
    
    // click action for home navbar button
    let navHome = document.querySelector(".nav-home");
    let homePage = document.querySelector(".home");
    navHome.addEventListener("click", ()=>{
        allNavClickable = document.querySelectorAll(".intro")
        allNavClickable.forEach(navItem => {
            navItem.style.display="none";
        });
        
        homePage.style.display="flex"
    })

    // click action for navbar about button
    let navAbout = document.querySelector(".nav-about");
    let aboutPage = document.querySelector(".about");
    navAbout.addEventListener("click", ()=>{
        allNavClickable = document.querySelectorAll(".intro")
        allNavClickable.forEach(navItem => {
            navItem.style.display="none";
        });
        
        aboutPage.style.display="flex"
    })

    // Click action button for certificate page
    let navCert = document.querySelector(".nav-cert");
    let certPage = document.querySelector(".cert");
    navCert.addEventListener("click", ()=>{
        allNavClickable = document.querySelectorAll(".intro")
        allNavClickable.forEach(navItem => {
            navItem.style.display="none";
        });
        
        certPage.style.display="flex"
    })
    
})
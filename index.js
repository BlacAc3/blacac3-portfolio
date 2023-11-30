document.addEventListener("DOMContentLoaded", ()=>{
    const tab=document.querySelector(".tab");
    const tabToggle= document.querySelector(".tab-toggle");
    if (tab){
        tabToggle.addEventListener("click",()=>{
            let disp = tab.style.display;
            if (disp="none"){
                tab.style.display="flex";
            } 
            if (disp="flex"){
                tab.style.display="none";
            }else{
                tab.style.display="none"
            }
            console.log(tab.style.display);
        });
    }
    
})
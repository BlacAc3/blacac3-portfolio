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
    let transactionModalContainer=document.querySelector(".transaction-box")
    if (sendButton){
        sendButton.addEventListener("click", ()=>{
            console.log("Send button Clicked")
            transactionModalContainer.style.display="flex";
        })
    }

    // open beneficiary popup 
    let benButton = document.querySelector("#beneficiaries-list a")
    if (benButton){
    
        benButton.addEventListener("click", ()=>{
            console.log("Opened Beneficiary page")
                beneficiaryModalContainer.style.display="flex";
        })
        


        //close transaction popup
        const closeModalTransaction = document.querySelector(".modal-close-button-transaction")
            closeModalTransaction.addEventListener("click", ()=>{
                console.log("Closed transaction page")
                transactionModalContainer.style.display="none";
                })
            

        //close beneficiary popup
        let beneficiaryModalContainer = document.querySelector(".beneficiaries-modal-container")
        const closeModalBeneficiary = document.querySelector(".modal-close-button-beneficiaries")
        if (closeModalBeneficiary){
                closeModalBeneficiary.addEventListener("click", ()=>{
                    console.log("Closed Beneficiary page")
                    beneficiaryModalContainer.style.display="none";
                })
            }
        
        let numInput = document.querySelector(".modal-form-acc-no input")
        let balanceInput = document.querySelector(".modal-form-amount input")
        let sendMoneyButton = document.querySelector(".modal-container button")
        let recipientName = document.querySelector("#beneficiaries-list p")
        let balance_element = document.querySelector(".modal-form-amount a")
        let balance = parseInt(balance_element.innerHTML)
            
        numInput.addEventListener("input", ()=>{
                let {value} = numInput
                fetch(`account-number/?q=${value}`, {
                    method: 'GET',
                    headers:{
                        "Content-Type":"application/json"
                    }
                })
                .then (response=>response.json())
                .then(data=>{
                    console.log(data.username)
                    
                    if (data.username !== undefined){
                        recipientName.innerHTML = data.username
                        if ( balance !== 0 ){
                            sendMoneyButton.style.display = "flex"
                        }
                        
                    }

                    if(data.username === undefined){
                        recipientName.innerHTML = "..."
                        sendMoneyButton.style.display="none"
                    }
                    
                    

                })
        })
        balanceInput.addEventListener("input", ()=>{
            
            if(balance >= balanceInput.value && recipientName.innerHTML !=="..." && balance !== 0){
                sendMoneyButton.style.display="flex"
                console.log(`${balance} is enough with your balance of ${balanceInput.value}`)
            }else{ 
                sendMoneyButton.style.display="none"
                console.log(`${balance} is not enough`)
            }

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

    let benCards = document.querySelectorAll(".modal-beneficiaries .card")
    if (benCards){
        benCards.forEach((card)=>{
            card.addEventListener("click", ()=>{
                let accNo = card.querySelector("p")
                let accName= card.querySelector("h3")

                beneficiaryModalContainer.style.display="none";
                let numberField = document.querySelector(".modal-form-acc-no input")
                let nameField= document.querySelector("#beneficiaries-list p")
                numberField.value=null
                numberField.value=accNo.innerHTML;
                nameField.innerHTML = accName.innerHTML;

            })
        })
    }
})

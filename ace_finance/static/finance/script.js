document.addEventListener("DOMContentLoaded", ()=>{

    
    
    let navIcon = document.querySelector(".nav-menu-icon");
    let sidebar = document.querySelector("#sidebar-section");
    if (navIcon){
        navIcon.addEventListener("click", ()=>{
            sidebar.classList.toggle("hide")
            console.log("hidden")
        })
    }
    showPopup()

    // copies text to clipboard 
    function copyToClipboard(text){
        navigator.clipboard.writeText(text)
            .then(() => {
            console.log('Text copied to clipboard');
            showPopup(`Copied to Clipboard!`)
            })
            .catch((err) => {
            console.error('Error copying text: ', err);
            });
            
        };

    //text that can be copied onclick
    let profAccNo = document.querySelectorAll(".copy-text")
    if (profAccNo){
        profAccNo.forEach((profAccNo)=>{
            profAccNo.addEventListener("click", ()=>{
                copyToClipboard(profAccNo.textContent)
            })
        })
    }
    

    // Shows popup text 
    function showPopup(text) {
        const popup = document.getElementById('topPopup');
        const popupText =document.querySelector("#topPopup div")
        if(text){
            popupText.innerHTML = text;
        }
        if (popupText.textContent){
            popup.style.display = 'flex';
            setTimeout(() => {
                popup.style.display = 'none';
            }, 3000); // Adjust the time the popup is displayed (in milliseconds)
        }
    }
    
    // does transaction verifications 
    let numInput = document.querySelector(".modal-form-acc-no input")
    let balanceInput = document.querySelector(".modal-form-amount input")
    let sendMoneyButton = document.querySelector(".modal-container button")
    let recipientName = document.querySelector("#beneficiaries-list p")
    let balance_element = document.querySelector(".modal-form-amount a")
    let balance = parseInt(balance_element.innerHTML)
    function verifiedTransactionDetails(){
        recipientName.innerHTML = "..."
        let {value} = numInput
        if (value){
            fetch(`/projects/finance-app/account-number/?q=${value}`, {
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
                    if ( balance !== 0 && balanceInput.value ){
                        sendMoneyButton.style.display = "flex"
                        sendMoneyButton.setAttribute("type", "submit")
                    }
                    
                }

                if(data.username === undefined){
                    recipientName.innerHTML = "..."
                    sendMoneyButton.style.display="none"
                    sendMoneyButton.setAttribute("type", "button")
                }
            })
        }
    }
    

    //display popup when a user clicks receive
    let receiveButton= document.querySelectorAll(".receive");
    if (receiveButton){
        receiveButton.forEach((receiveButton=>{
            receiveButton.addEventListener("click", ()=>{
                console.log("clicked")
                showPopup("Copy your account number By Clicking on it in your Profile Page")
            })
        }))
        
    }

    //popup for transaction
    //has a feature that checks if the modal box was activated from the beneficiaries page
    //if so the beneficiaries account number is automatically inputted
    let sendButton = document.querySelectorAll(".send")
    let transactionModalContainer=document.querySelector(".transaction-box")
    let accountInput = document.querySelector(".modal-form-acc-no input")
    
    if (sendButton){
        sendButton.forEach(sendButton=>{
            let beneficiaryParent=sendButton.parentNode.parentNode
            let recipientNumber = beneficiaryParent.querySelector(".each-beneficiary-info-pin p").textContent
            sendButton.addEventListener("click", ()=>{
                console.log("Send button Clicked")
                transactionModalContainer.style.display="flex";
                if (beneficiaryParent.className == "each-beneficiary"){
                    console.log(recipientNumber)
                    accountInput.value = recipientNumber
                    verifiedTransactionDetails()
                }
            })
        })
        
    }

    // open beneficiary popup 
    const closeModalTransaction = document.querySelector(".modal-close-button-transaction")
    if (closeModalTransaction){
        //close transaction popup
        closeModalTransaction.addEventListener("click", ()=>{
            console.log("Closed transaction page")
            transactionModalContainer.style.display="none";
            })
            


        numInput.addEventListener("input", verifiedTransactionDetails())
        balanceInput.addEventListener("input", ()=>{
            
            //The Below condition checks the following:
            //--The user main balance is more than or equal to the transaction amount inputed
            //--The recipient must be available in the system
            //--The users account balance must not equal 0
            //--The transaction amount inputed must not be empty
            if(balance >= balanceInput.value && recipientName.innerHTML !=="..." && balance !== 0 && balanceInput.value){
                sendMoneyButton.style.display="flex"
                sendMoneyButton.setAttribute("type", "submit")
                console.log(`${balance} is enough with your balance of ${balanceInput.value}`)
            }else{ 
                sendMoneyButton.style.display="none"
                sendMoneyButton.setAttribute("type", "button")
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

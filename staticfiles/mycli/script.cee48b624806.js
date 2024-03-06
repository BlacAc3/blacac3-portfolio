document.addEventListener('DOMContentLoaded', function () {
    const output = document.getElementById('output');
    const input = document.getElementById('input');

    input.addEventListener('keydown', function (event) {
        if (event.key === 'Enter') {
            if (input.value.toLowerCase() === "clear"){
                input.value = '';
                location.reload()
            }
            event.preventDefault();
            const command = input.value.trim();
            executeCommand(command);
        }
    });

    function executeCommand(command) {
        // Here, you can implement the logic to execute the command.
        fetch(`get-result/?query=${command}`, {
            method:"GET",
        })
        .then(response=>response.json())
        .then(response=>{
            console.log(response)
            input.value = '';
            appendOutput("\n")
            appendOutput('$ ' + command + '\n');
            appendOutput('$ ' + response.result + '\n');
        })
        
    }

    function appendOutput(text) {
        output.textContent += text;
        output.scrollTop = output.scrollHeight; // Auto-scroll to the bottom
    }
});

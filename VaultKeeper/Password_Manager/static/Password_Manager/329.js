// Changes the trashcan image from closed trash can image to the open trash can image 
function hover(img) {
    img.src = "/static/images/open-trash-can.png";
}


// Changes the trashcan image from open trash can image to the closed trashcan image
function hoverOut(img) {
    img.src = "/static/images/closed-trash-can.png"
    }


// Button that copys to clipboard
// Used to copy the username/password in gallery.html
function copy(counter) {
    var copyText = document.getElementById("copyText" + counter);
    
    // Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices
    
    // Copy the text inside the text field
    copyToClipboard(copyText.value)
    // navigator.clipboard.writeText(copyText.value);
    
    // Alert the copied text
    alert("COPIED 1");
}

function copyUser(counter) {
    var copyText = document.getElementById("copyUser" + counter);
    
    // Select the text field
    copyText.select();
    copyText.setSelectionRange(0, 99999); // For mobile devices
    
    // Copy the text inside the text field
    copyToClipboard(copyText.value)
    
    // Alert the copied text
    alert("COPIED 2");
}

async function copyToClipboard(textToCopy) {
    // Navigator clipboard api needs a secure context (https)
    if (navigator.clipboard && window.isSecureContext) {
        await navigator.clipboard.writeText(textToCopy);
    } else {
        // Use the 'out of viewport hidden text area' trick
        const textArea = document.createElement("textarea");
        textArea.value = textToCopy;
            
        // Move textarea out of the viewport so it's not visible
        textArea.style.position = "absolute";
        textArea.style.left = "-999999px";
            
        document.body.prepend(textArea);
        textArea.select();

        try {
            document.execCommand('copy');
        } catch (error) {
            console.error(error);
        } finally {
            textArea.remove();
        }
    };
}




function deletePassword(id) {
    var cardId = event.target.closest('.modal').getAttribute('data-card-id');
        console.log("Deleting card #" + cardId);
    // ... rest of the delete logic here
  }

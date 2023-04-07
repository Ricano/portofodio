// Get a reference to the background image element
let bgImg = document.getElementById("graffiti-wall");

// Get the modal
let modal = document.getElementById("myModal");

let mouseDownTime;
let timeoutId;


let closeToEdgeWarning = document.getElementById("edge-warning");


// Listen for a 1 second mousedown or touchstart on the entire document to gather the location and open the modal
document.addEventListener("mousedown", handleMouseDownOrTouchStart);
document.addEventListener("touchstart", handleMouseDownOrTouchStart);

function handleMouseDownOrTouchStart(e) {
    // Record the time when the left mouse button was pressed or a touch started

    if (e.target === bgImg) {

        // Only consider left mouse button or single touch
        if ((e.button === 0 && e.type === "mousedown") || (e.touches.length === 1 && e.type === "touchstart")) {
            // Rest of the code...

            mouseDownTime = new Date().getTime();
            // Set a timeout to check if the button has been held down for at least 2 seconds
            timeoutId = setTimeout(function () {
                // Check if the left mouse button is still held down or a touch is still active
                if ((e.buttons === 1 && e.type === "mousedown") || (e.touches.length === 1 && e.type === "touchstart")) {
                    // Get the location of the mouse or touch on the long press
                    let mouseX = e.clientX || e.touches[0].clientX;
                    let mouseY = e.clientY || e.touches[0].clientY;

                    // Get the position of the background image relative to the viewport
                    let bgImgRect = bgImg.getBoundingClientRect();
                    let bgImgX = bgImgRect.left;
                    let bgImgY = bgImgRect.top;

                    // Get the position of the mouse or touch relative to the background image
                    let mouseBgX = mouseX - bgImgX;
                    let mouseBgY = mouseY - bgImgY;


                    let marginX = 360;
                    let marginY = 500;
                    let backgroundWidthInPixels = getComputedStyle(bgImg).width
                    let backgroundHeightInPixels = getComputedStyle(bgImg).height
                    // remove 'px' trailing from string
                    let backgroundWidth = backgroundWidthInPixels.substring(0, backgroundWidthInPixels.length - 2)
                    let backgroundHeight = backgroundHeightInPixels.substring(0, backgroundHeightInPixels.length - 2)
                    if (backgroundWidth - mouseBgX < marginX || backgroundHeight - mouseBgY < marginY ) {
                        closeToEdgeWarning.style.display = "flex"
                        return
                    }

                    // Open the modal
                    modal.style.display = "block";
                    // Set the values of the form fields
                    document.getElementById("id_location_x").value = mouseBgX;
                    document.getElementById("id_location_y").value = mouseBgY;

                    // Prevent the default context menu from appearing
                    e.preventDefault();
                }
            }, 1000);
        }
    }
}

// Listen for a mouseup or touchend on the entire document (just to cancel the mouse down/touch start timer)
document.addEventListener("mouseup", handleMouseUpOrTouchEnd);
document.addEventListener("touchend", handleMouseUpOrTouchEnd);

function handleMouseUpOrTouchEnd(e) {
    // Cancel the timeout if the left mouse button is released before the 2 seconds are up or a touch ends
    if ((e.button === 0 && e.type === "mouseup") || e.type === "touchend") {
        clearTimeout(timeoutId);
    }
}

// Close the Egde warning on click
closeToEdgeWarning.addEventListener("click", function (e) {
    closeToEdgeWarning.style.display = "none";
});


// When the user clicks anywhere outside the modal, close it
window.onclick = function (event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}

document.querySelector("#graffiti-form").addEventListener("submit", function (event) {
    event.preventDefault();
    let formData = new FormData(event.target);
    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/graffiti");
    xhr.setRequestHeader("X-CSRFToken", document.querySelector("[name=csrfmiddlewaretoken]").value);
    xhr.onload = function () {
        try {
            let responseJSON = JSON.parse(xhr.responseText);
            let errorDiv = document.getElementById("error-message");
            errorDiv.innerHTML = ""

            for (const [key, value] of Object.entries(JSON.parse(responseJSON.errors))) {
                errorDiv.innerHTML += "<li>" + key.toUpperCase() + ": " + value[0].message + "</li>";
            }
        } catch (error) {
            modal.style.display = "none";
            window.location.href = "/graffiti";
        }
    };
    xhr.send(formData);
});


// Get the text input field and the text-counter div
const textInput = document.getElementById("id_text");
const textCounter = document.getElementById("text-counter");

// Add an event listener to the text input field that listens for the "input" event
textInput.addEventListener("input", () => {
    textCounter.style.visibility = "visible"
    // Get the remaining characters
    const remainingChars = textInput.maxLength - textInput.value.length;

    // Update the text of the text-counter div
    textCounter.textContent = remainingChars.toString() + "/" + textInput.maxLength;
});


//Rotate form text on slider slide :)

const rotationSlider = document.getElementById("rotation");
const textDiv = document.getElementById("id_text");

rotationSlider.addEventListener("input", function () {
    const rotationValue = rotationSlider.value;
    textDiv.style.transform = "rotate(" + rotationValue + "deg)";
});




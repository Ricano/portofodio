
// get "yt-form-go" element

const ytFormGo = document.getElementById("yt-form-go");
const loader = document.getElementById("loader");
const form = document.getElementById("yt-form");
const form2 = document.getElementById("download-form");

form.addEventListener("submit", function(event) {
  loader.style.display = "block"; // Show the loader when the form is submitted
  // You can also disable the form fields or the submit button here if desired
});

form.addEventListener("load", function(event) {
  loader.style.display = "none"; // Hide the loader when the form response is received
  // You can re-enable the form fields or the submit button here if they were disabled
});

form.addEventListener("error", function(event) {
  console.error("Form submission failed");
  loader.style.display = "none"; // Hide the loader when the form submission fails
  // You can re-enable the form fields or the submit button here if they were disabled
});

form.addEventListener("load", function(event) {
  console.log(event.target.responseText); // Handle the form response here
});

form2.addEventListener("submit", function(event) {
  loader.style.display = "block"; // Show the loader when the form is submitted
  // You can also disable the form fields or the submit button here if desired
});

form2.addEventListener("load", function(event) {
  loader.style.display = "none"; // Hide the loader when the form response is received
  // You can re-enable the form fields or the submit button here if they were disabled
});

form2.addEventListener("error", function(event) {
  console.error("Form submission failed");
  loader.style.display = "none"; // Hide the loader when the form submission fails
  // You can re-enable the form fields or the submit button here if they were disabled
});

form2.addEventListener("load", function(event) {
  console.log(event.target.responseText); // Handle the form response here
});

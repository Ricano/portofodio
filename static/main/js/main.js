let menuIcon = document.querySelector("#menu-icon");
let navBar = document.querySelector(".navbar");

menuIcon.onclick = () => {
    menuIcon.classList.toggle("bx-x");
    navBar.classList.toggle("active");
}


let sections = document.querySelectorAll("section");
let navLinks = document.querySelectorAll("header nav a");

window.onscroll = () => {
    sections.forEach(section => {
        let top = window.scrollY;
        let offset = section.offsetTop - 150;
        let height = section.offsetHeight;
        let id = section.getAttribute("id");

        if (top >= offset && top < offset + height) {
            navLinks.forEach((links => {
                links.classList.remove("active");
                document.querySelector("header nav a[href*=" + id + "]").classList.add("active");
            }))
        }
    });


    let header = document.querySelector("header");
    header.classList.toggle("sticky", window.scrollY > 100);


    menuIcon.classList.remove("bx-x");
    navBar.classList.remove("active");
};


ScrollReveal({
    // reset: true,
    distance: "80px",
    duration: 2000,
    delay: 200
});

ScrollReveal().reveal(".home-content, .heading", {
    origin: "top"
});
ScrollReveal().reveal(".photo, .services-container, portfolio-box, .contact form", {
    origin: "bottom"
});
ScrollReveal().reveal(".home-content h1, .about", {
    origin: "left"
});
ScrollReveal().reveal(".home-content p, .about-content", {
    origin: "right"
});


const typed = new Typed(".multiple-text", {
    strings: ["stuff", "poop", "nothing"],
    typeSpeed: 100,
    backSpeed: 100,
    backDelay: 1000,
    loop: true,
    showCursor: false
})
const typed2 = new Typed(".multiple-tech", {
        strings: ["stuff", "poop", "nothing"],
        typeSpeed: 100,
        backSpeed: 100,
        backDelay: 1000,
        loop: true,
        showCursor: false
    })


// Kaboom
function create() {
    location.reload()
}

function kaboom() {
// Get all-ish elements on the page

    const elements = document.querySelectorAll('footer, p, section, img, h3, h2, h1, a, i, span, #kitt');

// Loop through each element and set its position to absolute
    for (let i = 0; i < elements.length; i++) {
        const element = elements[i];
        element.style.position = 'absolute';
    }

// Function to animate an element offscreen
    function animateElementOffscreen(element) {
        // Get random values for the x and y positions and rotation
        const x = Math.random() * window.innerWidth * 2 - window.innerWidth / 2;
        const y = Math.random() * window.innerHeight * 2 - window.innerHeight / 2;
        const rotation = Math.random() * 720 - 360;

        // Calculate the distance to the edge of the screen
        const distanceX = Math.abs((window.innerWidth / 2) - x);
        const distanceY = Math.abs((window.innerHeight / 2) - y);

        // Calculate the easing function to use based on the distance to the edge of the screen
        const easingX = distanceX / (window.innerWidth / 2);
        const easingY = distanceY / (window.innerHeight / 2);

        // Animate the element to fly offscreen with a random position and rotation
        element.style.transition = 'transform 2s cubic-bezier(' + easingX + ', ' + easingY + ', 1, 1)';
        element.style.transform = `translate(${x}px, ${y}px) rotate(${rotation}deg)`;

        // Hide the element after the animation is complete

    }


// Loop through each element and animate it offscreen
    for (let i = 0; i < elements.length; i++) {
        const element = elements[i];
        animateElementOffscreen(element);
    }

    setTimeout(() => {
        for (let i = 0; i < elements.length; i++) {
            const element = elements[i];
            element.style.display = 'none';
        }
        document.querySelector("html").style.height = "100vh"
        document.getElementById("create-btn").style.display = "inline"
    }, 2300)

}
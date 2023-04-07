    // Change the profile photo every PHOTO_CHANGE_TIME seconds
    // Define an array of image sources
        const PHOTO_CHANGE_TIME = 5

    const photoSources = [
        "https://i0.wp.com/digital-photography-school.com/wp-content/uploads/2011/11/square-format-01.jpg?resize=600%2C600&ssl=1",
        "https://play-lh.googleusercontent.com/IeNJWoKYx1waOhfWF6TiuSiWBLfqLb18lmZYXSgsH1fvb8v1IYiZr5aYWe0Gxu-pVZX3",
        "https://media.istockphoto.com/id/1339008615/photo/thick-ornamental-gold-frame-isolated-on-white-background.jpg?b=1&s=170667a&w=0&k=20&c=NQ-sFeIOh9EV9XbJPw63xm8AbnqW4lO5QZ9ZieiVgrY="
    ];


    const myPhoto = document.getElementById("my-photo");
   // const myPhoto = document.querySelector(".photo img")
    let index = 0;

    function fadeOut() {
        myPhoto.style.opacity = 1;
        const fadeOutInterval = setInterval(() => {
            if (myPhoto.style.opacity > 0) {
                myPhoto.style.opacity -= 0.1;
            } else {
                clearInterval(fadeOutInterval);
                fadeIn();
            }
        }, 50);
    }

    function fadeIn() {
        index = (index + 1) % photoSources.length;
        myPhoto.src = photoSources[index];
        const fadeInInterval = setInterval(() => {
            if (myPhoto.style.opacity < 1) {
                myPhoto.style.opacity = parseFloat(myPhoto.style.opacity) + 0.1;
            } else {
                clearInterval(fadeInInterval);

                setTimeout(fadeOut, PHOTO_CHANGE_TIME * 1000);
            }
        }, 50);
    }

    setTimeout(fadeOut, PHOTO_CHANGE_TIME * 1000);

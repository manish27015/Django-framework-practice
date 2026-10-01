const slides = document.querySelector(".slides");
const dots = document.querySelectorAll(".dot");

const nextBtn = document.getElementById("nextBtn");
const prevBtn = document.getElementById("prevBtn");

const features = document.getElementById("features");

let currentSlide = 0;


function showSlide(index) {

    if (!slides) return;

    currentSlide = index;

    slides.style.transform =
        "translateX(-" + (currentSlide * 33.333333) + "%)";


    // DOTS

    dots.forEach(function (dot) {
        dot.classList.remove("active");
    });

    if (dots[currentSlide]) {
        dots[currentSlide].classList.add("active");
    }


    // FEATURES ONLY ON FIRST SLIDE

    if (features) {

        if (currentSlide === 0) {
            features.classList.remove("hide");
        } else {
            features.classList.add("hide");
        }

    }
}


/* NEXT */

if (nextBtn) {

    nextBtn.addEventListener("click", function () {

        currentSlide++;

        if (currentSlide >= 3) {
            currentSlide = 0;
        }

        showSlide(currentSlide);

    });

}


/* PREVIOUS */

if (prevBtn) {

    prevBtn.addEventListener("click", function () {

        currentSlide--;

        if (currentSlide < 0) {
            currentSlide = 2;
        }

        showSlide(currentSlide);

    });

}


/* DOTS */

dots.forEach(function (dot, index) {

    dot.addEventListener("click", function () {

        showSlide(index);

    });

});


/* AUTO SLIDER */

// setInterval(function () {

//     currentSlide++;

//     if (currentSlide >= 3) {
//         currentSlide = 0;
//     }

//     showSlide(currentSlide);

// }, 4000);


/* FIRST SLIDE */

showSlide(0);
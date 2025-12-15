const burger = document.querySelector(".burger");
const nav = document.querySelector(".menu");
const navLinks = document.querySelectorAll(".menu li")


burger.addEventListener("click", () => {
    nav.classList.toggle("nav-active");

    navLinks.forEach((link, index) => {
        if (link.style.animation) {
            link.style.animation = "";
        } else {
            // console.log(index);
            link.style.animation = `navLinksFade 0.5s ease forwards ${index / 11 + 0.4
                }s`;
        }
    });
    //burger animataion
    burger.classList.toggle("toggle");

});
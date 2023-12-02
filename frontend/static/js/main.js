
/* Menu */

const menu = document.getElementById("menu");
const menuBtn = document.getElementById("menuBtn");
const menuProfile_1 = document.getElementById("menuProfile_1");
const menuProfile_2 = document.getElementById("menuProfile_2");
const menuProfile_3 = document.getElementById("menuProfile_3");
const menuProfile_4 = document.getElementById("menuProfile_4");
const menuProfileBtn_1 = document.getElementById("menuProfileBtn_1");
const menuProfileBtn_2 = document.getElementById("menuProfileBtn_2");
const menuProfileBtn_3 = document.getElementById("menuProfileBtn_3");
const menuProfileBtn_4 = document.getElementById("menuProfileBtn_4");


menuBtn.addEventListener("click", () => {
    menu.classList.toggle("hidden-menu");
});

menuProfileBtn_1.addEventListener("click", () => {
    menuProfile_1.classList.remove("hidden");
    menuProfile_2.classList.add("hidden");
    menuProfile_3.classList.add("hidden");
    menuProfile_4.classList.add("hidden");
});

menuProfileBtn_2.addEventListener("click", () => {
    menuProfile_1.classList.add("hidden");
    menuProfile_2.classList.remove("hidden");
    menuProfile_3.classList.add("hidden");
    menuProfile_4.classList.add("hidden");
});

menuProfileBtn_3.addEventListener("click", () => {
    menuProfile_1.classList.add("hidden");
    menuProfile_2.classList.add("hidden");
    menuProfile_3.classList.remove("hidden");
    menuProfile_4.classList.add("hidden");
});

menuProfileBtn_4.addEventListener("click", () => {
    menuProfile_1.classList.add("hidden");
    menuProfile_2.classList.add("hidden");
    menuProfile_3.classList.add("hidden");
    menuProfile_4.classList.remove("hidden");
});

/* Scroll */

function scrollToLeft(containerId) {
    var container = document.getElementById(containerId);
    scrollToSmooth(container, container.scrollLeft - 275);
}

function scrollToRight(containerId) {
    var container = document.getElementById(containerId);
    scrollToSmooth(container, container.scrollLeft + 275);
}

function scrollToSmooth(container, position) {
    var start = container.scrollLeft;
    var startTime = performance.now();

    function animate(currentTime) {
        var elapsedTime = currentTime - startTime;

        container.scrollLeft = easeInOut(elapsedTime, start, position - start, 500);

        if (elapsedTime < 500) {
            requestAnimationFrame(animate);
        }
    }

    requestAnimationFrame(animate);
}

function easeInOut(t, b, c, d) {
    t /= d / 2;
    if (t < 1) return c / 2 * t * t + b;
    t--;
    return -c / 2 * (t * (t - 2) - 1) + b;
};

/* Chatbot Silvo Santos */

(function (d, t) {
    var BASE_URL = "https://plataforma2.innovchat.com.br";
    var g = d.createElement(t), s = d.getElementsByTagName(t)[0];
    g.src = BASE_URL + "/packs/js/sdk.js";
    g.defer = true;
    g.async = true;
    s.parentNode.insertBefore(g, s);
    g.onload = function () {
        window.chatwootSDK.run({
            websiteToken: 'TcHZS1iJiHH6hRsk3xAYUn8E',
            baseUrl: BASE_URL
        });
    };
})(document, "script");
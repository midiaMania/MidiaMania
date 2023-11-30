
/* Menu */

const menu = document.getElementById("menu");
const menuBtn = document.getElementById("menuBtn");

addEventListener("load", (event) => {
    const menu = document.getElementById("menu");
    menu.classList.toggle("hidden")
});

menuBtn.addEventListener("click", () => {
    menu.classList.toggle("hidden");
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
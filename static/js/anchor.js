// If browser if Firefox, go to the top of the page. This should fix the bug with anchor link in Firefox.
function anchor() {
    if (navigator.userAgent.indexOf("Firefox") != -1) {
        console.log("Mozilla Firefox detected")
        document.getElementById("navigation").scrollIntoView();
    }
}
document.addEventListener("DOMContentLoaded", function () {
    const goBackButton = document.querySelector(".go_back");

    if (goBackButton) {
        goBackButton.addEventListener("click", function (event) {
            event.preventDefault();
            window.history.back();
        });
    }
});

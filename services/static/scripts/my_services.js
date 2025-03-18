function enterService() {
    document.querySelectorAll(".service_container").forEach(div => {
        div.addEventListener("click", function() {
            window.location.href = this.getAttribute("data-url");
        });
    });
}
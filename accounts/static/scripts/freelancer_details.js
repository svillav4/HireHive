document.addEventListener("DOMContentLoaded", function () {
    var form = document.querySelector("form");
    var save_button = document.getElementById("save_button");
    var modal = document.getElementById("modal_success");
    var close_button = document.getElementById("close_button");

    save_button.addEventListener("click", function (event) {
        event.preventDefault(); // Prevent default form submission

        var formData = new FormData(form);

        fetch(form.action, {
            method: "POST",
            body: formData
        })
        .then(response => {
            if (response.ok) {
                modal.showModal();
            } else {
                alert("Error saving details.");
            }
        })
        .catch(error => console.error("Error:", error));
    });

    close_button.addEventListener("click", function () {
        modal.close();
    });

    window.onclick = function (event) {
        if (event.target == modal) {
            modal.close();
        }
    };
});
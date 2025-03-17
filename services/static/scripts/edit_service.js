document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const title = document.getElementById("title");
    const description = document.getElementById("description");
    const price = document.getElementById("price");
    const category = document.getElementById("category");
    const deliveryTime = document.getElementById("delivery_time");
    const fileInput = document.getElementById("file");
    const fileLabel = document.querySelector(".custom_file_upload");

    // ✅ Mantener la selección de archivo resaltada si ya hay una imagen cargada
    if (fileInput.files.length > 0) {
        fileLabel.classList.add("file-selected");
    }

    fileInput.addEventListener("change", function () {
        if (fileInput.files.length > 0) {
            fileLabel.classList.add("file-selected");
        } else {
            fileLabel.classList.remove("file-selected");
        }
    });

    const errorContainer = document.createElement("div");
    errorContainer.classList.add("alert", "alert-danger");
    errorContainer.style.display = "none";
    form.insertBefore(errorContainer, form.firstChild);

    form.addEventListener("submit", function (event) {
        let errors = [];

        if (title.value.trim() === "") {
            errors.push("Title is required.");
        }
        if (description.value.trim() === "") {
            errors.push("Description is required.");
        }
        if (price.value <= 0 || isNaN(price.value)) {
            errors.push("Price must be a positive number.");
        }
        if (deliveryTime.value <= 0 || isNaN(deliveryTime.value)) {
            errors.push("Delivery time must be at least 1 day.");
        }
        if (category.value === "") {
            errors.push("Category must be selected.");
        }

        if (fileInput.files.length > 0) {
            const file = fileInput.files[0];
            const validExtensions = ["image/jpeg", "image/png", "image/jpg"];
            if (!validExtensions.includes(file.type)) {
                errors.push("Image must be in JPG or PNG format.");
            }
        }

        if (errors.length > 0) {
            event.preventDefault();
            errorContainer.innerHTML = errors.map(error => `<strong>Error:</strong> ${error} <br>`).join("");
            errorContainer.style.display = "block";
        } else {
            errorContainer.style.display = "none";
        }
    });
});

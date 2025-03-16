document.addEventListener("DOMContentLoaded", function () {
    const form = document.querySelector("form");
    const title = document.getElementById("title");
    const description = document.getElementById("description");
    const price = document.getElementById("price");
    const category = document.getElementById("category");
    const deliveryTime = document.getElementById("delivery_time");
    const fileInput = document.getElementById("file");
    const fileLabel = document.querySelector('.custom-file-upload');
    const originalText = fileLabel.querySelector('.text span').textContent;
    
    const previewImage = document.createElement("img");
    previewImage.style.maxWidth = "100px";
    previewImage.style.marginTop = "10px";
    previewImage.style.display = "none";
    
    if (fileInput) {
        fileLabel.appendChild(previewImage);
        
        fileInput.addEventListener("change", function () {
            const file = this.files[0];
            if (file) {
                fileLabel.querySelector('.text span').textContent = file.name;
                
                fileLabel.classList.add('file-selected');
                
                const reader = new FileReader();
                reader.onload = function (e) {
                    previewImage.src = e.target.result;
                    previewImage.style.display = "block";
                };
                reader.readAsDataURL(file);
            } else {
                fileLabel.querySelector('.text span').textContent = originalText;
                fileLabel.classList.remove('file-selected');
                previewImage.style.display = "none";
            }
        });
    }

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
            alert(errors.join("\n"));
        }
    });
});

function toggleFilter() {
    document.querySelector(".filter_dropdown").classList.toggle("active");
}

function clearFilters() {
    document.querySelectorAll(".form-check-input").forEach(input => input.checked = false);
    
    
    // Remove 'filter' parameter from the URL
    const url = new URL(window.location.href);
    url.searchParams.delete("price_filter");
    url.searchParams.delete("category_filter");

    // Reload the page without the filter
    window.location.href = url.toString();
}

// Close dropdown when clicking outside
document.addEventListener("click", function(event) {
    const dropdown = document.querySelector(".filter_dropdown");
    if (!dropdown.contains(event.target)) {
        dropdown.classList.remove("active");    
    }
});

function enterService() {
    document.querySelectorAll(".service_container").forEach(div => {
        div.addEventListener("click", function() {
            window.location.href = this.getAttribute("data-url");
        });
    });
}
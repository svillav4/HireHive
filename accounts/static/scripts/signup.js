function toggleIsFreelancer() {
    var radiobutton = document.getElementById("btnradio2").checked;
    var is_freelancer = document.getElementById("is_freelancer");

    if (radiobutton) {
        is_freelancer.value = true;
    } else {
        is_freelancer.value = false;
    }
}

window.onload = function() {
    var is_freelancer = document.getElementById('is_freelancer');
    
    // Set the correct radio button on page load
    var isFreelancer = is_freelancer.value === 'true';
    document.getElementById('btnradio2').checked = isFreelancer;
    document.getElementById('btnradio1').checked = !isFreelancer;

    toggleIsFreelancer();  // Ensure the correct value is set on page load
};

document.getElementById("btnradio1").addEventListener("click", toggleIsFreelancer);
document.getElementById("btnradio2").addEventListener("click", toggleIsFreelancer);
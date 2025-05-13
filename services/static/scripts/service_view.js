document.addEventListener("DOMContentLoaded", function () {
    const goBackButton = document.querySelector(".go_back");

    if (goBackButton) {
        goBackButton.addEventListener("click", function (event) {
            event.preventDefault();
            window.history.back();
        });
    }
});

const btnOrder = document.getElementById("btn_order");
const modalOrder = document.getElementById("modal_order");
const btnReview = document.getElementById("btn_leave_review");
const modalReview = document.getElementById("modal_review");

btnOrder.addEventListener("click",() => {
    modalOrder.showModal();

    window.addEventListener("click", (event) => {
        if (event.target === modalOrder) {
            modalOrder.close();
        }
    });
});

btnReview.addEventListener("click",() => {
    modalReview.showModal();

    window.addEventListener("click", (event) => {
        if (event.target === modalReview) {
            modalReview.close();
        }
    });
});


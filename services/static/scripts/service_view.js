document.addEventListener("DOMContentLoaded", function () {
    const goBackButton = document.querySelector(".go_back");

    if (goBackButton) {
        goBackButton.addEventListener("click", function (event) {
            event.preventDefault();
            window.history.back();
        });
    }
});

const btnOpenModal = document.getElementById("btn_open_modal");
const modal = document.getElementById("modal");
const btn_close_modal = document.getElementById("btn_close_modal");

btnOpenModal.addEventListener("click",() => {
    modal.showModal();
});

btn_close_modal.addEventListener("click",() => {
    modal.close();
});

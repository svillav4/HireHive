const btnOpenModal = document.getElementById("btn_open_modal");
const modal = document.getElementById("modal");
const btnCloseModal = document.getElementById("btn_close_modal");

btnOpenModal.addEventListener("click",() => {
    modal.showModal();
});

btnCloseModal.addEventListener("click",() => {
    modal.close();
});

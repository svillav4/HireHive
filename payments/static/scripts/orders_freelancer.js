window.onload = function() {
    enableButtons();
}

const buttonsOpen = []
const buttonsClose = []
const modals = []

function enableButtons() {
    const var1 = document.getElementsByClassName("information")
    for (let i = 0; i < var1.length; i++) {
        buttonsOpen.push(var1[i].getElementsByClassName("btn_open_modal")[0]);
        buttonsClose.push(var1[i].getElementsByClassName("btn_close_modal")[0]);
        modals.push(var1[i].getElementsByClassName("modall")[0]);


        
        buttonsOpen[i].addEventListener("click",() => {
            modals[i].showModal();
            console.log("Abrir:", modals[i]);
        });
        buttonsClose[i].addEventListener("click",() => {
            modals[i].close();
            console.log("Cerrar:", modals[i]);
        });
        
    }

}
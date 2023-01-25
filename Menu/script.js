function esconder(){
    // OPERADOR TERNARIO
    menu.style.display = (menu.style.display == "block"? "none":"block");
}
function mudouTamanho(){
    menu.style.display = (window.innerWidth >= 768 ? "block":"none");
}
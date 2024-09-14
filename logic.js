let nav = document.querySelector("header>nav");

function alterar(){
    nav.style.display = nav.style.display == "none" ? "flex" : "none";
}

document.body.onload = function(){
    document.querySelector("header>nav").style.display = "none";
}
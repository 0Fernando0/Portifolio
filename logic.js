let menu = document.querySelector("header>nav");

function setDisplayMenu(){
    if(window.innerWidth >= 952){
        menu.style.display = "flex";
    }else{
        menu.style.display = "none";
    }
}


function setMenu(){
    menu.style.display = menu.style.display == "none" ? "flex" : "none";
}

// let nav = document.querySelector("header>nav");

// function alterar(){
//     nav.style.display = nav.style.display == "none" ? "flex" : "none";
// }

// document.body.onload = function(){
//     if(window.innerWidth < 668){
//         nav.style.display = "none";
//     }
// }

// document.body.onresize = function(){
//     if(window.innerWidth > 668){
//         nav.style.display = "flex";
//     }
// }
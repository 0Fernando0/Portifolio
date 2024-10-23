let menu = document.querySelector("header>nav");
let links_navegacao = document.querySelectorAll("nav>a");
let sections = document.querySelectorAll("section");

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

function animationObserver(){
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if(entry.isIntersecting){
                let section_id = entry.target.getAttribute("id");
                for (const link of links_navegacao) {
                    let link_id = link.getAttribute("href").slice(1)
                    if(link_id == section_id){
                        link.classList.add("visible")
                        break
                    }
                }
            }
            else{
                let section_id = entry.target.getAttribute("id");
                for (const link of links_navegacao) {
                    let link_id = link.getAttribute("href").slice(1)
                    if(link_id == section_id){
                        link.classList.remove("visible")
                        break
                    }
                }
            }
        })
    })
    sections.forEach(sec => {
        observer.observe(sec)
    })
}

animationObserver()


function switchTheme(){
    const img_theme = document.getElementById("theme");
    const img_menu = document.querySelector("header img")
    const theme = document.querySelector("html");
    
    if(theme.getAttribute("data-theme") == "dark"){
        theme.setAttribute("data-theme","light")
        img_theme.setAttribute("src","imagens/moon.png")
    }
    else{
        theme.setAttribute("data-theme","dark")
        img_theme.setAttribute("src","imagens/sun.png")
    }
}
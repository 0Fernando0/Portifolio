document.getElementById("burguer").onclick = function(){
    let condição = (document.getElementById("menu").style.display == "none") ? "block":"none"
    document.getElementById("menu").style.display = condição;
}

document.getElementById("body").onresize = function(){
    let cond = (window.innerWidth  > 600) ? "block":"none"; 
    document.getElementById("menu").style.display = cond;
        
}
let btn = document.querySelector("#btn");
let sidebar = document.querySelector(".siderbar");
let search = document.querySelector(".bx-search");

btn.onclick = function(){
    sidebar.classList.toggle("active");
}

search.onclick = function(){
    sidebar.classList.toggle("active");
}


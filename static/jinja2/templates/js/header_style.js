console.log('header_style connected');

let header = document.getElementById('header');
let drop_menu_button = document.getElementById('drop_menu_button');
let nav_list = document.getElementById('nav_list');


function drop_menu(){
    console.log('dropping the menu');
    nav_list.classList.toggle('thin-screen');
}

drop_menu_button.addEventListener('click', drop_menu);

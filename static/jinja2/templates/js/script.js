console.log('script.js connected')


let players_form = document.getElementById('players_form');
let player1_label = document.getElementById('player_1_label');
let player2_label = document.getElementById('player_2_label');
let player1_input = document.getElementById('player_1');
let player2_input = document.getElementById('player_2');
let js_validation_msg_field = document.getElementById('js_validation_error');
let validate_players_inputs_button = document.getElementById('validate_players_inputs')

function verifyPlayersInputs(){
    validate_players_inputs_button.addEventListener("click", checkValuesInInputs);
    console.log('verifyPlayersInputs');
}

function checkValuesInInputs(){
    players_form = document.getElementById('players_form');
    player1_input = document.getElementById('player_1');
    player2_input = document.getElementById('player_2');
    if (player1_input.value == "" || player2_input.value == ""){
        js_validation_msg_field.textContent = "Заполните все поля";
    } else {
        players_form.submit();
    }
}

verifyPlayersInputs();
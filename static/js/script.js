home_content();
function search_user(){
	//

	//
	var send_message=false;
	const xhttp = new XMLHttpRequest();
	input=document.getElementById("user_input").value;
	if(input.length>2){
		fetch('/post-data', {method: 'POST', headers: {'Content-Type': 'application/json'}, body: JSON.stringify({ data: "cherche "+input.replaceAll(" ","_") })})
		.then(response => {
			console.log(response);
			return response.text(); // Change to response.text() instead of response.json()
		})
		.then(data => document.getElementById("result").innerHTML = data) // Set the innerHTML to the response text
		.catch(error => {
			console.error(error);
		});
	}
}

function add_user(){
	/*
		a besoin de 6 inputs username_input,lastname_input,email_input,address_input,description_input,phone_input dans le code html
		s'occupe d'envoyer la commande en charge de l'ajout d'un utilisateur et des infformations d'une information d'un utilisateur
	*/
	var send_message=false;
	username=document.getElementById("username_input").value;
	lastname=document.getElementById("lastname_input").value;
	email=document.getElementById("email_input").value;
	address=document.getElementById("address_input").value;
	description=document.getElementById("description_input").value;
	phone=document.getElementById("phone_input").value;
	fetch('/post-data', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ data: "ajoute "+phone.replaceAll(" ","_")+" "+username.replaceAll(" ","_")+" "+lastname.replaceAll(" ","_")+" "+email.replaceAll(" ","_")+" "+address.replaceAll(" ","_")+" "+description.replaceAll(" ","_") })
	})
	.then(response => {
		console.log(response);
		return response.text(); // Change to response.text() instead of response.json()
	})
	.then(data => document.getElementById("result").innerHTML = data) // Set the innerHTML to the response text
	.catch(error => {
		console.error(error);
	});
	

}

function delete_user(){
	/*
		a besoin de 1 input user_input dans le code html
		s'occupe d'envoyer la commande pour effacer un utilisateur
	*/
	data=document.getElementById("delete_input").value;
	fetch('/post-data', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ data: "supprime "+data })
	})
	.then(response => {
		console.log(response);
		return response.text(); // Change to response.text() instead of response.json()
	})
	.then(data => document.getElementById("result").innerHTML = data) // Set the innerHTML to the response text
	.catch(error => {
		console.error(error);
	});
	


}
function home_content(){
	fetch('/post-data', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ data: "8" })
	})
	.then(response => {
		console.log(response);
		return response.text(); // Change to response.text() instead of response.json()
	})
	.then(data => document.getElementById("result").innerHTML = data) // Set the innerHTML to the response text
	.catch(error => {
		console.error(error);
	});
}

function change_implement(){
	/*
		a besoin de 3 inputs change_input,argument_selector,user_input dans le code html
		s'occupe d'envoyer la commande en charge du changement d'une information d'un utilisateur
	*/
	var send_message=false;
	new_information=document.getElementById("change_input").value;
	argument=document.getElementById("argument_selector").value;
	user=document.getElementById("modify_input").value;   
	fetch('/post-data', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ data: "2 "+user+" "+argument+" "+new_information.replaceAll(" ","%20") })
	})
	.then(response => {
		console.log(response);
		return response.text(); // Change to response.text() instead of response.json()
	})
	.then(data => document.getElementById("result").innerHTML = data) // Set the innerHTML to the response text
	.catch(error => {
		console.error(error);
	});

}
function all_none(){
	document.getElementById("add_option").style.display="none";
	document.getElementById("change_option").style.display="none";
	document.getElementById("suppr_option").style.display="none";
	//document.getElementById("user_input").style.display="inline";
	//document.getElementById("user_button").style.display="inline";
	document.getElementById("result").innerHTML='';
	document.getElementById("titletext").innerHTML="Répertoire Téléphonique".bold();
	let inputs = document.getElementsByTagName("input");
	for (input of inputs){
		input.value = "";
	}
}
function suppr_input_values(){
	let inputs = document.getElementsByTagName("input");
	for (input of inputs){
		input.value = "";
	}
}

function suppr_option_show(){
	if(document.getElementById("suppr_option").style.display=="none"){
		all_none();
		document.getElementById("suppr_option").style.display="block";
		document.getElementById("titletext").innerHTML="Répertoire Téléphonique - Supprimer Contact".bold();
	}
	else{
		document.getElementById("suppr_option").style.display="none";
	}
}

function add_option_show(){
	
	
	if(document.getElementById("add_option").style.display=="none"){
		all_none()
		document.getElementById("add_option").style.display="block";
		document.getElementById("titletext").innerHTML="Répertoire Téléphonique - Ajouter Contact".bold();
	}else{
		document.getElementById("add_option").style.display="none";
	}
}

function change_option_show(){
	
	if(document.getElementById("change_option").style.display=="none"){
		all_none()  
		document.getElementById("change_option").style.display="block";
		document.getElementById("user_input").style.display="inline"
		document.getElementById("user_button").style.display="inline"
		document.getElementById("titletext").innerHTML="Répertoire Téléphonique - Modifier Contact".bold();
	}else{
		document.getElementById("change_option").style.display="none";
		document.getElementById("user_input").placeholder="search";
	}
}
function actualisation_change_placeholder(){
	text=document.getElementById("argument_selector").value;
	document.getElementById("change_input").placeholder=text;

}
function connect_user(){
	email=document.getElementById("username_login_input").value;
	password=document.getElementById("password_login_input").value;
	fetch('/post-data', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ data: "6 "+email+" "+password})
	})
	.then(response => {
		console.log(response);
		return response.text();
	})
	.then(data => give_token(data)) // Set the innerHTML to the response text
	.catch(error => {
		console.error(error);
	}); 
}

function create_user(){
	email=document.getElementById("username_signin_input").value;
	password=document.getElementById("password_signin_input").value;
	fetch('/post-data', {
		method: 'POST',
		headers: {
			'Content-Type': 'application/json'
		},
		body: JSON.stringify({ data: "7 "+email+" "+password})
	})
	.then(response => {
		console.log(response);
		return response.text();
	})
	.then(data => give_token(data)) // Set the innerHTML to the response text
	.catch(error => {
		console.error(error);
	}); 

}

function give_token(data){
	alert(data);
	const json_data =JSON.parse(data);
	localStorage.token=json_data.token;
	if (String(localStorage.token).length > 1){
		location.hash = "#";
	}
	alert(data);
}

function popup_on_first_time(){
	if(String(localStorage.token)=="undefined" || String(localStorage.token)==""){
		location.hash = 'centered_login';
	}

}
window.addEventListener('popstate', function (event) {
	if(!(location.href.indexOf("#centered_signin") > -1)){
		location.reload();
	}
});


window.onload=function(){
	var input = document.getElementById("user_input");
	popup_on_first_time();
	input.addEventListener("keypress", function(event) {
	  
	  if (event.key === "Enter") {
		
		event.preventDefault();
		
		document.getElementById("user_button").click();
	  }
	});

}

function openNav() {
	document.getElementById("mySidenav").style.width = "250px";
  
}

function closeLeftMenu() {
	document.getElementById("mySidenav").style.width = "0";
	document.getElementById("main").style.marginLeft= "0";
	document.body.style.backgroundColor = "white";
}

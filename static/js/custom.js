
document.getElementById("loading").style.visibility ="hidden";

function clickBtn(){
  const message = document.getElementById("message");
	const loading = document.getElementById("loading");

	if(loading.style.visibility=="visible"){
		// hiddenで非表示
		loading.style.visibility ="hidden";
    message.style.visibility ="visible";
	}else{
		// visibleで表示
		loading.style.visibility ="visible";
    message.style.visibility ="hidden";
	}
}

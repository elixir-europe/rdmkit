let systemInitiatedDark = window.matchMedia("(prefers-color-scheme: dark)"); 
let theme = sessionStorage.getItem('theme');

if (systemInitiatedDark.matches) {
	document.getElementById("theme-toggle").innerHTML = '<i class="fa fa-adjust"></i>  <i id="tg-sb-icon" class="fa fa-toggle-on"></i>';
} else {
	document.getElementById("theme-toggle").innerHTML = '<i class="fa fa-adjust"></i>  <i id="tg-sb-icon" class="fa fa-toggle-off"></i>';
}

function prefersColorTest(systemInitiatedDark) {
  if (systemInitiatedDark.matches) {
  	document.documentElement.setAttribute('data-theme', 'dark');		
   	document.getElementById("theme-toggle").innerHTML = '<i class="fa fa-adjust"></i>  <i id="tg-sb-icon" class="fa fa-toggle-on"></i>';
   	sessionStorage.setItem('theme', '');
  } else {
  	document.documentElement.setAttribute('data-theme', 'light');
    document.getElementById("theme-toggle").innerHTML = '<i class="fa fa-adjust"></i>  <i id="tg-sb-icon" class="fa fa-toggle-off"></i>';
    sessionStorage.setItem('theme', '');
  }
}
systemInitiatedDark.addListener(prefersColorTest);


function modeSwitcher() {
	let theme = sessionStorage.getItem('theme');
	if (theme === "dark") {
		document.documentElement.setAttribute('data-theme', 'light');
		sessionStorage.setItem('theme', 'light');
		document.getElementById("theme-toggle").innerHTML = '<i class="fa fa-adjust"></i>  <i id="tg-sb-icon" class="fa fa-toggle-off"></i>';
	}	else if (theme === "light") {
		document.documentElement.setAttribute('data-theme', 'dark');
		sessionStorage.setItem('theme', 'dark');
		document.getElementById("theme-toggle").innerHTML = '<i class="fa fa-adjust"></i>  <i id="tg-sb-icon" class="fa fa-toggle-on"></i>';
	} else if (systemInitiatedDark.matches) {	
		document.documentElement.setAttribute('data-theme', 'light');
		sessionStorage.setItem('theme', 'light');
		document.getElementById("theme-toggle").innerHTML = '<i class="fa fa-adjust"></i>  <i id="tg-sb-icon" class="fa fa-toggle-off"></i>';
	} else {
		document.documentElement.setAttribute('data-theme', 'dark');
		sessionStorage.setItem('theme', 'dark');
		document.getElementById("theme-toggle").innerHTML = '<i class="fa fa-adjust"></i>  <i id="tg-sb-icon" class="fa fa-toggle-on"></i>';
	}
}

if (theme === "dark") {
	document.documentElement.setAttribute('data-theme', 'dark');
	sessionStorage.setItem('theme', 'dark');
	document.getElementById("theme-toggle").innerHTML = '<i class="fa fa-adjust"></i>  <i id="tg-sb-icon" class="fa fa-toggle-on"></i>';
} else if (theme === "light") {
	document.documentElement.setAttribute('data-theme', 'light');
	sessionStorage.setItem('theme', 'light');
	document.getElementById("theme-toggle").innerHTML = '<i class="fa fa-adjust"></i>  <i id="tg-sb-icon" class="fa fa-toggle-off"></i>';
}
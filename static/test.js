
const navBar = document.querySelector('.navbar');
const openMenuToggle = document.querySelector('.bx-menu');
const closeMenuToggle = document.querySelector('.bx-x');

// --- OPEN MENU

openMenuToggle.addEventListener('click', () => {
    if(navBar.classList.contains('show_navbar')){
        navBar.classList.remove('show_navbar');
    }else {
        navBar.classList.add('show_navbar');
        openMenuToggle.classList.add("hide");
        closeMenuToggle.classList.add("show");
    }
})

// --- CLOSE MENU

closeMenuToggle.addEventListener('click', () => {
    if(navBar.classList.contains('show_navbar')){
        navBar.classList.remove('show_navbar');
        openMenuToggle.classList.remove("hide");
        closeMenuToggle.classList.remove("show");
    }
})


// --------- DARK MODE ACTIVATION ----------
let darkMode = localStorage.getItem('darkmode');
const darkModeToggle = document.querySelector('.themecolor');
const sunIcon = document.querySelector('.bxs-sun');
const moonIcon = document.querySelector('.bxs-moon');

const enableDarkMode = () => {
    // 1. Add the class dark mode to the body
    document.body.classList.add('darkmode');
    // 2. Update dark mode in the local storage
    localStorage.setItem('darkmode', 'enabled');
}

if (darkMode === "enabled"){
    enableDarkMode();
    sunIcon.classList.add("show");
    moonIcon.classList.add("hide");
}

const disableDarkMode = () => {
    // 1. Remove class dark mode to the body
    document.body.classList.remove('darkmode');
    localStorage.setItem('darkmode', null)
}

darkModeToggle.addEventListener('click', () => {
    darkMode = localStorage.getItem('darkmode');
    if (darkMode !== "enabled"){
        enableDarkMode();
        sunIcon.classList.add("show");
        moonIcon.classList.add("hide");
    }else {
        disableDarkMode();
        sunIcon.classList.remove("show");
        moonIcon.classList.remove("hide");
    }
})

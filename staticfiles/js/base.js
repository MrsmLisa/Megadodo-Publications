
// close the navbar when clicking outside of it
document.addEventListener('click', function(event) {
    const navbar = document.getElementById('navbarSupportedContent');
    const toggler = document.querySelector('.navbar-toggler');

    if (navbar.classList.contains('show') && 
        !navbar.contains(event.target) && 
        !toggler.contains(event.target)) {
        toggler.click();
    }
});
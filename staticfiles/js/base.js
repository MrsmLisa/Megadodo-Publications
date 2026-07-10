
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

// show all toasts
document.addEventListener('DOMContentLoaded', function() {
    console.log('DOM fully loaded and parsed');
    const toastElements = document.querySelectorAll('.toast');
    toastElements.forEach(function(toastElement) {
        const toast = new bootstrap.Toast(toastElement, {
            autohide: true, delay: 5000
        });
        toast.show();
    });
});
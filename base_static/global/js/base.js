// menu animation

const headerMenu = document.querySelector('[data-header="menu"]')

function AnimateMenuScroll() {
    const windowTop = window.pageYOffset;
    if (windowTop > 0) {
        headerMenu.classList.add('menu-shadow')
    }
    else {
        headerMenu.classList.remove('menu-shadow')
    }
}

window.addEventListener('scroll', function() {
    AnimateMenuScroll();
})

// ============================================================================


function submitForm(id) {
    let form = document.getElementById(id);
    form.submit();
}

function deletSearch() {
    let search = document.getElementById('search');
    search.value = ''
    submitForm('form_filter')
}

function sendSearch() {
    submitForm('form_filter')
}


const hamburger = document.querySelector(".hamburger");
const menu = document.querySelector(".menu");

hamburger.addEventListener("click", () =>
menu.classList.toggle("active"));

hamburger.addEventListener("click", () =>
hamburger.classList.toggle("active"));
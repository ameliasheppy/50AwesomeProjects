// want an eventlistener!
const toggle = document.getElementById('toggle')
const nav = document.getElementById('nav')

//with classList, we can add, remove or toggle. we want toggle!
toggle.addEventListener('click', ()=>{
    nav.classList.toggle('active')
})
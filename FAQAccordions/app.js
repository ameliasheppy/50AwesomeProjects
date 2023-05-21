// bring in toggle buttons
//loop through node list (forEach)
//add click event with eventListener
//toggle the active classes

const toggles = document.querySelectorAll('.faq-toggle')

toggles.forEach(toggle =>{
    toggle.addEventListener('click', () =>{
        toggle.parentNode.classList.toggle('active')
    })
})
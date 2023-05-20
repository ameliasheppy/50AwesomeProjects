const labels = document.querySelectorAll('.form-control label')

//turn them into a node list!
//split them, use map to turn them into a span of letters with a transition on it, use join to turn our array back into a str
//to verify that they are in a span, go to elements in the dev tools and check it out!
//we need to set an addl transition here on each individual index so that each letter has it's own transition
//play with the *50 to see if we like it's current transition speed
labels.forEach(label =>{
    label.innerHTML = label.innerText.split('').map((letter, idx) => `<span style="transition-delay:${idx*50}ms">${letter}</span>`).join('')
})
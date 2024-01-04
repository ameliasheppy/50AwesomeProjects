//be able to grab the panels, want to grab them all. This will put all of the panels into a node list, which is like an array!
const panels = document.querySelectorAll('.panel')

console.log(panels)
//you can loop through the Node list like it is an array. 
panels.forEach(panel => {
    //set the eventListener to do something on each click
    //run the func everytime we click
    panel.addEventListener('click', () => {
        console.log("switched the panels!")
        //need to remove the active class from the other panels that are not selected
        removeActiveClasses()
        //when we click the active, it switches the flex to flex 5.
        panel.classList.add('active')
    })
})

//since the arrow funcs in the forEach only take one arg, don't need extra () after panel
function removeActiveClasses() {
    panels.forEach(panel => {
        panel.classList.remove('active')
    })
}
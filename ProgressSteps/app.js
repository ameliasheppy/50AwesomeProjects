const progress = document.getElementById('progress')
const previous = document.getElementById('previous')
const next = document.getElementById('next')
//bring in all of the circles as a node list
const circles = document.querySelectorAll('.circle')

let currentActive = 1

next.addEventListener('click', () => {
    currentActive++

    if(currentActive > circles.length) {
        currentActive = circles.length
    }

    update()
})

previous.addEventListener('click', () =>{
    currentActive--
    console.log(currentActive)
    //keep it in it's boundaries!
    //the circles are a node list/array so they have a length
    if(currentActive < 1){
        currentActive = 1
    }
    update()
})

function update(){
    circles.forEach((circle, index) =>{
        if(index < currentActive){
            circle.classList.add('active')
        }else{
            circle.classList.remove('active')
        }
    })
    const actives = document.querySelectorAll('.active')
    //we want the circles AND the lines to light up blue
    //need to get a %'age so we can fill up our bar

    //the percentage needs to cover it by thirds, not quarters, so subtract one
    progress.style.width = (actives.length-1)/(circles.length-1)*100+'%'
    //check the current active
    if(currentActive === 1) {
        previous.disabled = true
        //check to see if it's at the end
    } else if(currentActive === circles.length) {
        next.disabled = true
        //otherwise, we can access both buttons if we are in the middle
    } else {
        previous.disabled = false
        next.disabled = false
    }
}
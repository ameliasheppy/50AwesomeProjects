const loadText = document.querySelector('.loading-text')
const bg = document.querySelector('.bg')

let load = 0;
// the below would blur forever and ever without stopping, so we need to add a way for it to stop at 1000%
let int = setInterval(blurring, 30)

function blurring(){
    // we want this to run in an interval, q 30 ms
    load++

    if(load>99){
        clearInterval(int)
    }
    // this is what we are doing in the DOM
    //we want it start blurry and then clear
    loadText.innerText = `${load}%`
    //opacity goes from 0-1, not 100, so we will need some JS math!
    //we want to map from 0-100 in the time that 1-0
    //use the Stack Overflow JS map a range to another range map 0-100 to 1-0
    // want to take in a num, an input min and max and then an output min and max
    //if we wanted to start clear and go blurry, it would be 0-->1
    loadText.style.opacity = scale(load, 0, 100, 1, 0)
    //do the same thing for the blur, 30px will be the max blur
    //map 0-100 as 30-0 when load is done
    bg.style.filter = `blur(${scale(load, 0, 100, 30, 0)}px)`
}

const scale = (num, in_min, in_max, out_min, out_max)=>{
    return (num - in_min) * (out_max - out_min) /(in_max - int) + out_min
}
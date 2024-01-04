const sounds = ["applause", "gasp", "tada", "victory", "wrong"]

sounds.forEach(sound =>{
    const btn = document.createElement('button')
    btn.classList.add('btn')

    btn.innerText = sound
    btn.addEventListener('click', () =>{
        //we can use the API to do play with JS if it is an audio element
        stopSongs()
        document.getElementById(sound).play()
    })

    document.getElementById('buttons').appendChild(btn)
})

function stopSongs(){
    sounds.forEach(sound => {
        const song = document.getElementById(sound)

        song.pause()
        song.currentTime = 0;
    })
}
const insert = document.getElementById('insert')

window.addEventListener('keydown', (e) =>{
    console.log(e)
    //look through the returned obj in the console and we can see code, keyCode, etc, of what we're looking for
    //be sure to check and see if the key is equal to an " "

    insert.innerHTML = `
    <div class="key"> ${e.key === " " ? 'space':e.key}
    <small>event.key</small>
</div>
<div class="key"> 
    ${e.keyCode}
    <small>event.keyCode</small>
</div>
<div class="key">
    ${e.code}
    <small>event.code</small>
</div>`
})
let context = document.getElementById("canvas")
let canvas = context.getContext("2d")
canvas.moveTo(0, 0)
canvas.lineTo(100, 100)
canvas.stroke()
let running = true
function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
async function draw() {
    imported = document.getElementById("python").innerText
    while (imported.length < 1){
        imported = document.getElementById("python").innerText

        await sleep(1000)
        console.log("awaiting imports from python")
    }
    console.log(imported.length)
    console.log(imported)
    imported = imported.replaceAll("'",'"')
    imported = JSON.parse(imported)
    imported = [imported]
    console.log(imported)
    console.log(imported[0][0].name)
}
draw()
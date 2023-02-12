function draw() {
    var theCanvas = document.getElementById('smiley');
    if (theCanvas.getContext) {
        var theContext = theCanvas.getContext('2d');
        theContext.beginPath();
        theContext.lineWidth = 3;
        theContext.fillStyle = 'yellow';
        theContext.arc(75,75,50,0,Math.PI * 2,true); // Outer circle
        theContext.fill();
        theContext.moveTo(110,75);
        theContext.arc(75,75,35,0,Math.PI,false); // Mouth
        theContext.stroke()
        theContext.moveTo(65,65);
        theContext.arc(60,65,5,0,Math.PI * 2); // Left Eye
        theContext.moveTo(95,65);
        theContext.arc(90,65,5,0,Math.PI * 2); // Right Eye
        theContext.stroke();
    } else {
        document.write('Your browser does not support the Canvas API. Please install a modern browser!!!');
    }
}
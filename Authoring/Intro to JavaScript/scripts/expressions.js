var notDefined;
var yourName = prompt('What is your name?','Sammy');
var temperature = prompt('What is the temperature in Celsius?');
if (isNaN(temperature) == true) {
    var message = 'Invalid temperature entered!!!';
} else if (temperature == null) {
    var message = 'You did not enter a temperature';
} else {
    var fahrenheit = temperature * 9 / 5 + 32;
    // Setup message to be output to the user as a variable to reduce code
    var message = 'Hello ' + yourName + '! You entered ' + temperature + ' as` the Celsius temperature which converts to ' + fahrenheit + ' in fahrenheit.';
}

/* 
notDefined = (temperature > 10) ? 'greater than 10' : 'less than equal to 10'

if (temperature > 10) {
    notDefined = 'greater than 10';
} else {
    notDefined = 'less than equal to 10';
}
*/
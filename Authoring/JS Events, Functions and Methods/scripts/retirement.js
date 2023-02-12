function calculateRetirement(currentAge) {
    const RETIRE_AGE = 67;
    var theMessage = '';
    if (isNaN(currentAge)) {
        theMessage = 'Age is not a number!!!';
    } else {
        var years = RETIRE_AGE - currentAge;
        if (years <= 0) {
            theMessage = 'Congratulations, you have reached the retirement age!!!';
        } else {
            theMessage = 'You can retire in ' + years + ' years.';
        }
    }
    return theMessage;
}
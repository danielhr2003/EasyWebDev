function validateForm(theForm) {
    var isValid = true;
    var errorMessage = '';

    if (theForm.clientname.value == '') {
        isValid = false;
        errorMessage = errorMessage + 'Client name is required';
        theForm.clientname.focus();
    }

    if (theForm.email.value == '') {
        if (isValid == true) {
            isValid = false;
            theForm.email.focus();
        }
        errorMessage = errorMessage + '\nClient email is required'
    } else {
        if (theForm.email.value.length < 3) {
            if (isValid == true) {
                isValid = false;
                theForm.email.focus();
            }
            errorMessage = errorMessage + '\nEmail must be at least 3 characters';
        }
    }

    if (theForm.county.value == '') {
        if (isValid == true) {
            isValid = false;
            theForm.county.focus();
        }
        errorMessage = errorMessage + '\nCounty is required'
    }



    if (isValid == false) {
        alert(errorMessage);
    }

    return isValid;
}

$(document).ready(function() {
   $('#btnValidate').click(function() {
        var sEmail = $('#txtEmail').val();
        if ($.trim(sEmail).length == 0) {
            alert('Please enter valid email address');
            e.preventDefault();
        }
        if (validateEmail(sEmail)) {
           
        }
        else {
            alert('Invalid Email Address');
            e.preventDefault();
        }
    });
});
$(document).ready(function() {
    $('#txtPhone').blur(function(e) {
        if (validatePhone('txtPhone')) {
            $('#spnPhoneStatus').html('Valid');
            $('#spnPhoneStatus').css('color', 'green');
        }
        else {
            $('#spnPhoneStatus').html('Invalid');
            $('#spnPhoneStatus').css('color', 'red');
        }
    });
});

function validatePhone(txtPhone) {
    var a = document.getElementById(txtPhone).value;
    var filter = /^[0-9-+]+$/;
    if (filter.test(a)) {
        return true;
    }
    else {
        return false;
    }
}
$(document).ready(function() {
$('#submit').click(function(e) {
	 var name = $('#name').val();
	 var name_regex = /^[a-zA-Z]+$/;
	 if (firstname.length == 0) {
$("#name").focus();
return false;
}
// Validating Name Field.
else if (!name.match(name_regex) || name.length == 0) {
$("#name").focus();
return false;
}
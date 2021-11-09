let rules = {
    username: {
        required: true,
    },
    password: {
        required: true
    },
};

$.validator.setDefaults({
        errorClass: 'help-block with-errors',
        errorElement: 'div',
        onkeyup: function (element) {
            $(element).valid();
        },
        onfocusout: function (element) {
            $(element).valid();
        },
        highlight: function (element, errorClass, validClass) {
            $(element).closest('.form-group').addClass('has-error');
        },
        unhighlight: function (element, errorClass, validClass) {
            $(element).closest('.form-group').find('.help-block.has-error').html('');
            $(element).closest('.form-group').removeClass('has-error');
        },
        errorPlacement: function (error, element) {
            $(element).closest('.form-group').append(error);
        },
        rules: rules
    });


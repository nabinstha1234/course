(function ($) {
    var methods = {
        isValid: false,
        valid: function () {
            return methods.isValid;
        },
        init: function (options) {
            var passInput = $(this);
            var form = passInput.closest('form');
            var messageWrapperId = passInput.attr('id') + "-message-wrapper";
            methods.renderMessage(messageWrapperId, passInput);
            passInput.on('keyup', function () {
                methods.validateInput($(this).val(), messageWrapperId);
            }).on('focusin', function () {
                $('#' + messageWrapperId).removeClass('d-none');
                methods.validateInput($(this).val(), messageWrapperId);
            });
            return {'el': this, 'isValid': methods.isValid};
        },
        renderMessage: function (messageWrapperId, passInput) {
            var checkTemplate = "<div id='" + messageWrapperId + "' class='d-none'>" +
                "<div>Your password needs to:</div>" +
                "<ul>" +
                "<li data-check='numeric'>include at least one number.</li>" +
                "<li data-check='specialChar'>include at least one special character.</li>" +
                "<li data-check='capitalChar'>include at least one capital character.</li>" +
                "<li data-check='lowerChar'>include at least one lower character.</li>" +
                "<li data-check='minlength'>require password length to be 8 characters or longer.</li>" +
                "</ul></div>";
            passInput.after(checkTemplate);
            return;
        },
        validateInput: function (input, messageWrapperId) {
            if (input.length >= 8) {
                $('#' + messageWrapperId).find('li[data-check="minlength"]').css('color', 'green');
                methods.isValid = true;
            }
            else {
                $('#' + messageWrapperId).find('li[data-check="minlength"]').css('color', 'red');
                methods.isValid = false;
            }
            if (/[A-Z]/.test(input)) {
                $('#' + messageWrapperId).find('li[data-check="capitalChar"]').css('color', 'green');
                methods.isValid = true;
            } else {
                $('#' + messageWrapperId).find('li[data-check="capitalChar"]').css('color', 'red');
                methods.isValid = false;
            }
            if (/[a-z]/.test(input)) {
                $('#' + messageWrapperId).find('li[data-check="lowerChar"]').css('color', 'green');
                methods.isValid = true;
            } else {
                $('#' + messageWrapperId).find('li[data-check="lowerChar"]').css('color', 'red');
                methods.isValid = false;
            }
            if (/[0-9]/.test(input)) {
                $('#' + messageWrapperId).find('li[data-check="numeric"]').css('color', 'green');
                methods.isValid = true;
            } else {
                $('#' + messageWrapperId).find('li[data-check="numeric"]').css('color', 'red');
                methods.isValid = false;
            }
            if (/[$-/@#:-?{-~!"^_`\[\]]/.test(input)) {
                $('#' + messageWrapperId).find('li[data-check="specialChar"]').css('color', 'green');
                methods.isValid = true;
            } else {
                $('#' + messageWrapperId).find('li[data-check="specialChar"]').css('color', 'red');
                methods.isValid = false;
            }
showPass
            return methods.isValid;
        }
    };

    $.fn.strongifyPassword = function (methodOrOptions) {
        if (methods[methodOrOptions]) {
            return methods[methodOrOptions].apply(this, Array.prototype.slice.call(arguments, 1));
        } else if (typeof methodOrOptions === 'object' || !methodOrOptions) {
            return methods.init.apply(this, arguments); // Default to "init"
        } else {
            $.error('Method ' + methodOrOptions + ' does not exist on Strongify Password');
        }
    };
}(jQuery));

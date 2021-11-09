$(function () {
    $("#sale_date_from").datepicker({
        dateFormat: "yy-mm-dd",
        numberofMonths:1,
        changeYear:true,
        changeMonth:true,
        onSelect: function (selectdate) {
            let dt = new Date(selectdate);
            dt.setDate(dt.getDate() + 0)
            $('#sale_date_upto').datepicker('option', 'minDate', dt);
        },
    });
    $("#sale_date_upto").datepicker({
        dateFormat: "yy-mm-dd",
        numberofMonths:1,
        changeYear:true,
        changeMonth:true,
        onSelect: function (selectdate) {
            let dt = new Date(selectdate);
            dt.setDate(dt.getDate() - 1)
            $('#sale_date_from').datepicker('option', 'maxDate', dt);
        },
    });

});
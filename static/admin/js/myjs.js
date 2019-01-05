$("#logout_button").click(function () {
    $.ajax({
        url: "/logout/",
        type: "POST",
        data: {
        },
        success: function (vv) {
            alert(vv);
        }
    })
    document.location.href="/";
});
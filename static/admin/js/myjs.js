$("#searching").click(function () {
    var profession = $("#profession").val();
    var location = $("#location").val();


    $.ajax({
        url: "/searching/",
        type: "POST",
        data: {
            "profession": profession,
            "location": location,
        },
        /*success: function (vv) {

        }*/
    })

    location.replace("www.google.com");
});
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

/*$("#apply").click(function () {
    alert("現在還不能應徵喔 因為這個功能還沒做 先加薪再說");
    document.location.href="/";
});*/
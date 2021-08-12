
$(function () {
    $("#mysearch").on("keyup", function () {

        if ($("#mysearch").length > 0) {
            $("#results_section").css("display", "block")
        }
        else if ($("#mysearch").length == 0) {
            $("#results_section").css("display", "none")
        }
        var formData = $("#search-form").serialize()
        var myUrl = $("#search-form").attr('data-url') || window.location.href
        $.ajax({
            method: 'GET',
            url: myUrl,
            data: formData,
            success: function (response) {
                $("#results_section").html(response['search_results'])
            },
            error: function (rs, e) {
                console.log(rs.responseText);
            }
        })
    })
})
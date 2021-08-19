$(function(){
    $(".show-nav-menu").on("click", ()=>{
        $(".navbar-menu-container").css("display", "flex").css("transition","all 0.3s ease")
        // $("#mysidenav").hide(1);
        $(".show-nav-menu").hide()
        $(".cancel-btn").show()
    })
    $(".cancel-btn").on("click", ()=>{
        $(".navbar-menu-container").css("display", "none").css("transition", "all 0.3s ease")
        $(".show-nav-menu").show()
        $(".cancel-btn").hide()
    })

    // hover action for rents
    $("#rents").on("mouseover",()=>{
        $(".for-rents").css("display","block")
    }).on("mouseout",()=>{
        $(".for-rents").css("display", "none")
    })
})
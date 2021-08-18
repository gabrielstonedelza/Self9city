$(function(){
    $(".show-nav-menu").on("click", ()=>{
        $("#navlinks-container").css("display","block")
        $("#mysidenav").hide(1500);
    })
    $(".cancel-btn").on("click", ()=>{
        $("#navlinks-container").css("display", "none")
        $("#mysidenav").show(1500);
    })
})
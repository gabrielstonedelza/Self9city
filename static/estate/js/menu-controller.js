$(function(){
    $(".open-menu").on("click", ()=>{
        $(".items").addClass('active')
        $(".open-menu").hide();
    })
    $(".cancel-btn").on("click", ()=>{
        $(".items").removeClass('active')
        $(".open-menu").show();
    })
})
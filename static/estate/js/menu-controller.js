$(function(){
    $(".open-menu").on("click", ()=>{
        $(".items").addClass('active')
    })
    $(".cancel-btn").on("click", ()=>{
        $(".items").removeClass('active')
    })
})
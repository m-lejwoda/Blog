

$(".navbar__mobile-icon").click(function () {
    $('.navbar__mobile__panel').addClass("text-warning-anim");
    if ($('.navbar__mobile__panel').is(":visible")) {
        
        $('.navbar__mobile__panel').removeClass("text-warning-anim2")
        $('.navbar__mobile__panel').removeClass("text-warning-anim")
        $('.navbar__mobile__panel').addClass("text-warning-anim").delay(1000).hide(1);

    } else {

        $('.navbar__mobile__panel').show(1).addClass("text-warning-anim2");

    }
});
$(".news__bonusinformation__journalists__user").on({
    mouseenter: function (event) {
        $(".news__bonusinformation__journalists__user__name").css('color','red')
        $( this ).find('a').css('color','#F94C4C');
    },
    mouseleave: function (event) {
        $(".news__bonusinformation__journalists__user__name").css('color','red')
        $( this ).find('a').css('color','white');
    }
});
$(".dashboard__news__firstcolumn").on({
    mouseenter: function (event) {
        $(".dashboard__news__firstcolumn__meta-title").css('color','#F94C4C')
        
    },
    mouseleave: function (event) {
        $(".dashboard__news__firstcolumn__meta-title").css('color','white')
        
    }
});
$(".dashboard__news__secondcolumn__first").on({
    mouseenter: function (event) {
        $(".dashboard__news__secondcolumn__first__meta-title").css('color','#F94C4C')
        
    },
    mouseleave: function (event) {
        $(".dashboard__news__secondcolumn__first__meta-title").css('color','white')
        
    }
});
$(".dashboard__news__secondcolumn__second").on({
    mouseenter: function (event) {
        $(".dashboard__news__secondcolumn__second__meta-title").css('color','#F94C4C')
        
    },
    mouseleave: function (event) {
        $(".dashboard__news__secondcolumn__second__meta-title").css('color','white')
        
    }
});


$("#news").click(function() {
    $('html,body').animate({
        scrollTop: $(".news__posts").offset().top},
        'slow');
});
function onClick(page) {
    window.location.href = page
}
function onClickRecommendation(e){
    document.getElementsByClassName(e)[0].attributes.value.value = "checked"
    if(e !== "post__recommendation-popular"){
        document.getElementsByClassName("post__recommendation-popular")[0].attributes.value.value = ""
    }

    if(e !== "post__recommendation-author"){
        document.getElementsByClassName("post__recommendation-author")[0].attributes.value.value = ""
    }
    if(e !== "post__recommendation-last"){
        document.getElementsByClassName("post__recommendation-last")[0].attributes.value.value = ""
    }
} 
function onSubmit(event){
    event.preventDefault()
    let radio1 = document.getElementById("radio-one")
    let radio2 = document.getElementById("radio-two")
    let radio3 = document.getElementById("radio-three")
    if(radio1.checked){
        radio1.value = true
        radio2.value = false
        radio3.value = false
    }
    if(radio2.checked){
        radio2.value = true
        radio1.value = false
        radio3.value = false
    }
    if(radio3.checked){
        radio3.value = true
        radio1.value = false
        radio2.value = false
    }
    let form = document.getElementById("form")
    form.submit(function(e){
        e.preventDefault()
    })
    
}


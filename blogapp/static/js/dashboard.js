
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
$(".navbar__mobile-icon").click(function() {
    console.log("Wyświetl ikone")
    
    // $('html,body').animate({
    //     scrollTop: $(".news__posts").offset().top},
    //     'slow');
});






$("#news").click(function() {
    console.log($(".news__posts"))
    console.log($(".search"))
    $('html,body').animate({
        scrollTop: $(".news__posts").offset().top},
        'slow');
});
// $(document).ready(function (){
//     $.ajax({
//         url: "/radio/",
//         type: 'POST',
//         data:{
//             radio: "radio",
//             input: "radio-one",
//             author: author
//         },
//         success: function(response){
//             console.log(response)
//             $('#radio2').html(response);
//         }
        
//     })
//     $(".radio-btn").click(function(){
//         var url = "{% url 'radio2' %}";
//         console.log(url)
//         $.ajax({
//             url: "/radio/",
//             type: 'POST',
//             data:{
//                 radio: "radio",
//                 input: $(this)[0].id,
//                 author: author
//             },
//             success: function(response){
//                 console.log(response)
//                 $('#radio2').html(response);
//             }
            
//         })
//     })
// })
function onClick(page) {
    window.location.href = page
}
function onClickRecommendation(e){
    console.log(e)
    document.getElementsByClassName(e)[0].attributes.value.value = "checked"
    console.log(document.getElementsByClassName(e)[0])
    if(e !== "post__recommendation-popular"){
        document.getElementsByClassName("post__recommendation-popular")[0].attributes.value.value = ""
    }

    if(e !== "post__recommendation-author"){
        document.getElementsByClassName("post__recommendation-author")[0].attributes.value.value = ""
        console.log(document.getElementsByClassName("post__recommendation-author")[0])
    }
    if(e !== "post__recommendation-last"){
        document.getElementsByClassName("post__recommendation-last")[0].attributes.value.value = ""
        console.log(document.getElementsByClassName("post__recommendation-last")[0])
    }
} 
function onSubmit(event){
    event.preventDefault()
    let radio1 = document.getElementById("radio-one")
    let radio2 = document.getElementById("radio-two")
    let radio3 = document.getElementById("radio-three")
    if(radio1.checked){
        console.log("radio1")
        radio1.value = true
        radio2.value = false
        radio3.value = false
    }
    if(radio2.checked){
        console.log("radio2")
        radio2.value = true
        radio1.value = false
        radio3.value = false
    }
    if(radio3.checked){
        console.log("radio3")
        radio3.value = true
        radio1.value = false
        radio2.value = false
    }
    let form = document.getElementById("form")
    form.submit(function(e){
        e.preventDefault()
    })
    
}


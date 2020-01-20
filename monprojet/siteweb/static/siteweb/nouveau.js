$(function() {
    $(".portfolio nav li").click(function(t) {
		if ( e(this).hasClass( "active" ) ){
			console.log("deja actif")}
		else{
			$(".portfolio section figure").slideUp("slow");
			modal = e(this).attr("id");
			$(".portfolio nav li").removeClass("active");
			$(this).addClass("active");
			if (modal=="all"){
				$(".portfolio section figure").slideDown("slow");
			}
			else $(".portfolio section figure." + modal).slideDown("slow");
		}
    });
})

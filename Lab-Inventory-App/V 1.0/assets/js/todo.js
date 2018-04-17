$("ul").on("click", "li", function(){
	$(this).toggleClass("completed");
	//choosing this selects the specific clicked element! Awesome.

});

// click x to delete Todo

$("ul").on("click", "span", function(event){
	$(this).parent().fadeOut(500, function(){
		$(this).remove();

	});
	event.stopPropogation();

});
$("Input[type='text']").keypress(function(event){
	if(event.which === 13){
		var identity = $(this).attr('class');
		//alert($("." +identity));
		var todoText = $(this).val();
		$(this).val("");
		//grabbing new todo text
		//alert(text);
		//create new li and add to ul
		$("#"+identity).append("<li><span><i class = 'fa fa-trash'></i></span> " + todoText + "</li>");
	}
})

$(".fa-plus").click(function(){
	$("Input[type='text']").fadeToggle();

});
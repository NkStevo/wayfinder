var selectedDiv = $("#main").children()[0];

  $("#wrapper").on("swiperight",function nextRight(){
    $(this).animate({
       opacity: 0, // animate slideUp
       marginLeft: '+300px'
     }, 'fast', 'linear', function() {
       $.when($(this).fadeOut("fast", function(){
         opacity: 0
         $("#holderDiv").append(selectedDiv)
         next(selectedDiv);
         selectedDiv = $("#main").children()[0];


       })).done($(this).fadeIn("fast", function(){
         $(this).css({"opacity": "", "margin-left": "", "display": "", "transition":".25s ease-in"})
       }));
     });
   });





   $("#wrapper").on("swipeleft",function nextLeft(){
     $(this).animate({
        opacity: 0, // animate slideUp
        marginLeft: '-300px'
      }, 'fast', 'linear', function() {
        $.when($(this).fadeOut("fast", function(){
          opacity: 0
          $("#holderDiv").append(selectedDiv)
          next(selectedDiv);
          selectedDiv = $("#main").children()[0];


        })).done($(this).fadeIn("fast", function(){
          $(this).css({"opacity": "", "margin-left": "", "display": "", "transition":".25s ease-in"})
        }));
      });
    });


  function next(currentDiv){
    switch(currentDiv.id){
      case "evan":
        $("#main").append($("#ale"))
        break;
      case "ale":
        $("#main").append($("#steve"))
        break;
      case "steve":
        $("#main").append($("#evan"))
        break;

    }
  }

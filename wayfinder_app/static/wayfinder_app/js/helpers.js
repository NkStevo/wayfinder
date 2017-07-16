var selectedDiv = $("#main").children()[0];

  $("#wrapper").on("swiperight",function nextRight(){
    $(this).animate({
       opacity: 0, // animate slideUp
       marginLeft: '+300px'
     }, 'fast', 'linear', function() {
       $.when($(this).fadeOut("fast", function(){
         opacity: 0
         $("#holderDiv").append(selectedDiv)
         $("#main").append($("#holderDiv").children()[0])
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
          $("#main").append($("#holderDiv").children()[0])
          selectedDiv = $("#main").children()[0];

        })).done($(this).fadeIn("fast", function(){
          $(this).css({"opacity": "", "margin-left": "", "display": "", "transition":".25s ease-in"})
        }));
      });
    });

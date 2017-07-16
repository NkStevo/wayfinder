  $("#main").on("swiperight",function nextRight(){
  //  $(this).css({'background-color': 'blue'})
    $(this).animate({ height: 0, opacity: 0 }, 'slow');
    //$("#holderDiv").append($(this))

  });



  $("#main").on("swipeleft",function nextLeft(){
    $(this).css({'background-color': 'red'})
  });

  function next(currentDiv){

  }

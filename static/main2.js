
//To toggle the button status 

$(document).ready(function () {
    var isListening = false;

    $("#toggle-listen").click(function () {
      if (!isListening) {
        // Start listening
        $("#mic-display").hide(); // Hide the microphone icon
        $("#sound").show(); // Show the wave animation container 
        $(".sound-wave").css("margin-left", "-125px");
        $(".loader").css("margin-left", "-3px"); 
        $.ajax({
          url: "/listen/",
          type: "GET",
          data: { action: "start" },
          success: function (response) {
            $("#recognized-text").text(response.text);
          },
          error: function (xhr, status, error) {
            console.error("Error:", error);
          },
        });
       } else {
        // Stop listening
        $("#mic-display").show(); // Show the microphone icon
        $("#sound").hide(); // Hide the wave animation container
        $(".sound-wave").css("margin-left", "0px");
        $(".loader").css("margin-left", "-97px");

        $.ajax({
          url: "/listen/",
          type: "GET",
          data: { action: "stop" },
          success: function (response) {
            $("#recognized-text").text(""); // Clear text
          },
          error: function (xhr, status, error) {
            console.error("Error:", error);
          },
        });
      }
      isListening = !isListening; // Toggle listening state
      // $(this).text(isListening ? "Start Listening" : "Stop Listening");
    });


  });
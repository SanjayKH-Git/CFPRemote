$(document).ready(function($){
    $(".dropdown").on('click', function() {
    $(".section-dropdown").show();
    });

    $("#PhNo").on('click', function() {
        $(".section-dropdown").hide();
        $("#target").val("");
        $("#target").attr({"type":"tel","name":"PhoneNo","pattern":"^\\d{10}$", "placeholder":"Enter Target PhoneNo (10 Digit)"},);
    });
    $("#email").on('click', function() {
        $(".section-dropdown").hide();
        $("#target").val("");
        $("#target").attr({"type":"email","name":"Email","pattern":"[^@\\s]+@[^@\\s]+\\.[^@\\s]+", "placeholder":"Enter Target Email"},);
    });
    $("#website").on('click', function() {
        $(".section-dropdown").hide();
        $("#target").val("");
        $("#target").attr({"type":"url","name":"webLink","pattern":"https://.*|http://.*", "placeholder":"Enter Target URL"},);
    });

    $('#Punish').submit(function(e) {
        $("#atk").disabled=true;
        alert("💣 Attacking on "+ $('#target').val() +"\n🧨 Please don't Refresh the Page \n⏰ Wait for few seconds to complete ");
        $('.Bomb').css('display','block')
    });

});
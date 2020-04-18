var isValid = true;
 $('input,textarea,select').filter('[required]:visible').each(function() {
  if ( $(this).val() === '' )
     isValid = false;
});

function onClickedEstimatePrice() {
    console.log("Estimate price button clicked");
    var area = document.getElementById("area");
    var bhk = document.getElementById("bhk");
    var bathrooms = document.getElementById("bath");
    var parking = document.getElementById("parking");
    var TYPE = document.getElementById("type");
    var status1 = document.getElementById("status");
    var transaction = document.getElementById("transaction");
    var furnishing = document.getElementById("furnishing");
    var Locality = document.getElementById("Locality");
    var warning = document.getElementById("warning");

    if(area.value > 0 && bhk.value!="" && bathrooms.value!="" && parking.value!="" && TYPE.value !="" && status1.value!="" && transaction.value!="" && furnishing.value!="" && Locality.value!=""){
        warning.innerHTML = "";
        //var estPrice = document.getElementById("uiEstimatedPrice");
        var url = "http://127.0.0.1:5000/predict_home_price"; 
        //var url = "/api/predict_home_price"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
        $.post(url, {
            area: parseFloat(area.value),
            bhk: bhk.value,
            bathroom: bathrooms.value,
            furnishing: furnishing.value,
            parking : parking.value,
            status1 : status1.value,
            transaction: transaction.value,
            TYPE : TYPE.value,
            locality: Locality.value
            },function(data, status) {
                console.log(data.calc_price);
                //estPrice.innerHTML = "<h3>Rs. "+data.calc_price.toString() +"</h3>";
                console.log(status);
                Swal.fire({
                    title: "Estate Price", 
                    html: "<h3>Rs. "+data.calc_price.toString() +"</h3>",  
                    confirmButtonText: "Ok", 
                    showClass: {
                        popup: 'animated rubberBand slow'
                    },
                    hideClass: {
                        popup: 'animated fadeOutUp faster'
                    }
                });
                document.getElementById("myForm").reset();
        });
    }else{
        warning.innerHTML = "<p>Please fill all the information!<p>";
    }

    
    //document.getElementById("myForm").reset();
}
  
  function onPageLoad() {
    console.log( "document loaded" );
    var url = "http://127.0.0.1:5000/get_location_names"; // Use this if you are NOT using nginx which is first 7 tutorials
    //var url = "/api/get_location_names"; // Use this if  you are using nginx. i.e tutorial 8 and onwards
    $.get(url,function(data, status) {
        console.log("got response for get_location_names request");
        if(data) {
            var locations = data.locations;
            var Locality = document.getElementById("Locality");
            //$('#Locality').empty();
            for(var i in locations) {
                var opt = new Option(locations[i]);
                $('#Locality').append(opt);
            }
        }
    });
  }
  
  window.onload = onPageLoad;
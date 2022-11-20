function weatherBalloon( cityID ) {
    var key = '{yourkey}';
    fetch('https://api.openweathermap.org/data/2.5/weather?id=' + cityID+ '&appid=' + key)  
    .then(function(resp) { return resp.json() }) // Convert data to json
    .then(function(data) {
    console.log(data);
    })
    .catch(function() {
      // catch any errors
    });
}

window.onload = function() {
    weatherBalloon( 6167865 );
}
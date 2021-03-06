/**
 * Created by ggarrido on 5/01/15.
 */

function initialize() {
    var mapOptions = {
        center: { lat: 39.577279, lng: 2.639604},
        zoom: 18,
        panControl: true,
        zoomControl: true,
        scrollwheel: false,
        mapTypeControl: true,
        scaleControl: false,
        streetViewControl: false,
        overviewMapControl: false,
        disableDefaultUI: true
    };

    var myLatlng = new google.maps.LatLng(39.577293, 2.639612);
    var map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);
    var contentString = '<div id="content">'+
      '<div id="siteNotice">'+
      '</div>'+
      '<h1 id="firstHeading" class="firstHeading">Centro Psicogym</h1>'+
      '<div id="bodyContent">'+
      '<p>Estamos en el <b>Centro Psicogym</b>, todos los Martes de' +
      ' <b>15.00 a 18.30</b>, para cualquer consulta.'
      '</div>';

    var infowindow = new google.maps.InfoWindow({
      content: contentString
    });

    var marker = new google.maps.Marker({
          position: myLatlng,
          map: map,
          title: 'PsicoGym'
    });

//    google.maps.event.addListener(marker, 'click', function() {
//      infowindow.open(map,marker);
//    });
}

$(function () {
  google.maps.event.addDomListener(window, 'load', initialize);
});

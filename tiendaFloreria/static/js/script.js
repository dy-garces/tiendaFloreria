function iniciarMap() {
    var coord = { lat: -36.7909433, lng: -73.0564579 };
    var map = new google.maps.Map(document.getElementById('map'), {
        zoom: 17,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}
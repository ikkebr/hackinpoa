$(function(){

    var points = [];
    var map;
    var map_tag = "map_canvas";
    var body = $("body");
    var directionService = new google.maps.DirectionsService();
    var directionsDisplay = new google.maps.DirectionsRenderer({
        draggable: true
    });

    function setCurrentLocation(map) {
        if (navigator.geolocation) {
            navigator.geolocation.getCurrentPosition(function(location){
                map.setCenter(new google.maps.LatLng(location.coords.latitude,
                    location.coords.longitude));
                // new google.maps.Marker({
                //     position: map.getCenter(),
                //     map: map,
                //     title: 'Click to zoom'
                // });
            });
        }
    }

    function initializeMap() {
        var mapOptions = {
            center: new google.maps.LatLng(-34.397, 150.644),
            zoom: 13,
            mapTypeId: google.maps.MapTypeId.ROADMAP
        };
        var map = new google.maps.Map(document.getElementById(map_tag),
            mapOptions);

        setCurrentLocation(map);
        return map;
    }

    function setInitialRoute(origin, destination){
        body.attr("data-origin", origin);
        body.attr("data-destination", destination);
    }

    function getInitialRoute(){
        var ret = [];

        ret.push(body.attr("data-origin"));
        ret.push(body.attr("data-destination"));

        return ret;
    }

    function addWayPoint(location){
        var routePoints = getInitialRoute();

        directionService.route({
            origin: routePoints[0],
            destination: routePoints[1],
            travelMode: google.maps.TravelMode.DRIVING,
            waypoints: points
        }, function(data, status){
            directionsDisplay.setMap(map);
            directionsDisplay.setDirections(data);
            setInitialRoute(routePoints[0].value, routePoints[1].value);
        });
    }

    function addInitialRoute(routePoints){
        var response;

        directionService.route({
            origin: routePoints[0].value,
            destination: routePoints[1].value,
            travelMode: google.maps.TravelMode.DRIVING
        }, function(data, status){
            directionsDisplay.setMap(map);
            directionsDisplay.setDirections(data);
            setInitialRoute(routePoints[0].value, routePoints[1].value);
        });
    }

    map = initializeMap();

    $("#init-route").submit(function(event){
        event.preventDefault();
        var form = $(this);
        var data = form.serializeArray();

        addInitialRoute(data, map);
    });

    google.maps.event.addListener(map, 'click', function(data){
        points.push({location: new google.maps.LatLng(
            data.latLng.k, data.latLng.D
        )});
        addWayPoint();
    });

    google.maps.event.addListener(directionsDisplay, 'directions_changed', function(){
        debugger;
    });

});
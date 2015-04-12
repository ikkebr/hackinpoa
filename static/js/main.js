if (window.Mototrip === undefined) window.Mototrip = {};

Mototrip.Create = {

    create: function(){
        var priv = {};
        var pub = {};

        priv.points = [];
        priv.map;
        priv.map_tag = "map_canvas";
        priv.body = $("body");
        priv.directionService = new google.maps.DirectionsService();
        priv.directionsDisplay = new google.maps.DirectionsRenderer({
            draggable: true
        });

        priv.setCurrentLocation = function () {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function(location){
                    priv.map.setCenter(new google.maps.LatLng(location.coords.latitude,
                        location.coords.longitude));
                    // new google.maps.Marker({
                    //     position: map.getCenter(),
                    //     map: map,
                    //     title: 'Click to zoom'
                    // });
                });
            }
        }

        priv.initializeMap = function() {
            var mapOptions = {
                center: new google.maps.LatLng(-34.397, 150.644),
                zoom: 13,
                mapTypeId: google.maps.MapTypeId.ROADMAP
            };
            map = new google.maps.Map(document.getElementById(priv.map_tag),
                mapOptions);

            return map;
        }

        priv.setInitialRoute = function(origin, destination){
            priv.body.attr("data-origin", origin);
            priv.body.attr("data-destination", destination);
        }

        priv.addPointOnTable = function(data, current_point){
            var legs = data.routes[0].legs;
            var latitude = current_point.k.toPrecision(5);
            var longitude = current_point.D.toPrecision(5);
            var table = $("#points");

            for(i=0; i<=legs.length - 1; i++){
                var leg = legs[i];
                var start_latitude = leg.start_location.k.toPrecision(5);
                var start_longitude = leg.start_location.D.toPrecision(5);

                if(latitude == start_latitude && longitude == start_longitude){
                    table.find("tbody").append("<tr><td>" + leg.start_address + "</td><td>" + leg.distance.text + "</td></tr>");
                }
            }
        }

        priv.setFormData = function(data){
            var legs = data.routes[0].legs;
            var distance;
            var duration;

            for(i=0; i<=legs.length - 1; i++){

            }
        }

        priv.setPoint = function(origin, destination, initial, waypoints, current_point){
            priv.directionService.route({
                origin: origin,
                destination: destination,
                travelMode: google.maps.TravelMode.DRIVING,
                waypoints: waypoints
            }, function(data, status){
                if(initial == false){
                    priv.addPointOnTable(data, current_point);
                }
                priv.directionsDisplay.setMap(priv.map);
                priv.directionsDisplay.setDirections(data);
                priv.setFormData(data);
            });
        }

        priv.getInitialRoute = function(){
            var ret = [];

            ret.push(priv.body.attr("data-origin"));
            ret.push(priv.body.attr("data-destination"));

            return ret;
        }

        priv.addWayPoint = function(current_point){
            var location = priv.getInitialRoute();
            var origin = location[0];
            var destination = location[1];
            var waypoints = priv.points;

            priv.setPoint(origin, destination, false, waypoints, current_point)
        }

        priv.addInitialRoute = function(routePoints){
            var origin = routePoints[0].value;
            var destination = routePoints[1].value

            priv.setInitialRoute(origin, destination, true);
            priv.setPoint(origin, destination)
        }

        pub.init = function(){
            priv.map = priv.initializeMap();
            priv.setCurrentLocation();

            $("#init-route").submit(function(event){
                event.preventDefault();
                var form = $(this);
                var data = form.serializeArray();

                priv.addInitialRoute(data);
            });

            google.maps.event.addListener(priv.map, 'click', function(data){
                var current_point = new google.maps.LatLng(
                    data.latLng.k, data.latLng.D
                )
                priv.points.push({location: current_point});
                priv.addWayPoint(current_point);
            });

            // google.maps.event.addListener(priv.directionsDisplay, 'directions_changed', function(){

            // });
        }

        return pub;
    }()

}

Mototrip.Create.create.init()

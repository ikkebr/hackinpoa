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
                    priv.addWayPointOnRoute(leg);
                    table.find("tbody").append("<tr><td>" + leg.start_address + "</td><td>" + leg.distance.text + "</td></tr>");
                }
            }
        }

        priv.setFormData = function(data){
            var legs = data.routes[0].legs;
            var trip = $("#trip").attr("value");
            var distance = 0.0;
            var duration = 0.0;

            for(i=0; i<=legs.length - 1; i++){
                var leg = legs[i];
                distance += leg.distance.value;
                duration += leg.duration.value;
            }

            distance = (distance / 1000).toPrecision(2);
            duration = "00:" + (duration / 60).toPrecision(2);

            $.ajax({
                url: window.location.pathname,
                type: "POST",
                data: {
                    trip: trip,
                    distance: distance,
                    duration: duration,
                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken").val(),
                    start_point: priv.getInitialRoute()[0],
                    end_point: priv.getInitialRoute()[1],
                },
                success: function(data){
                    $("#route").val(data.id);
                }
            });
        }

        priv.addWayPointOnRoute = function(point){
            $.ajax({
                url: "/trips/waypoints/create",
                type: "POST",
                data: {
                    route: $("#route").val(),
                    latitude: point.start_location.k,
                    longitude: point.start_location.D,
                    description: point.start_address,
                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken").val(),
                },
                success: function(data){
                    console.log(data);
                }
            });
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
                }else{
                    priv.setFormData(data);
                }

                priv.directionsDisplay.setMap(priv.map);
                priv.directionsDisplay.setDirections(data);
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
            if($("#map_canvas").length > 0){
                priv.map = priv.initializeMap();
                priv.setCurrentLocation();

                if(window.location.pathname.indexOf("show") < 0){
                    google.maps.event.addListener(priv.map, 'click', function(data){
                        var current_point = new google.maps.LatLng(
                            data.latLng.k, data.latLng.D
                        )
                        priv.points.push({location: current_point});
                        priv.addWayPoint(current_point);
                    });
                }
            }


            $("#init-route").submit(function(event){
                event.preventDefault();
                var form = $(this);
                var data = form.serializeArray();

                priv.addInitialRoute(data);
            });

            // google.maps.event.addListener(priv.directionsDisplay, 'directions_changed', function(){

            // });
        }

        return pub;
    }()

}

Mototrip.Create.create.init()

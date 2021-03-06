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
            draggable: false
        });

        priv.setCurrentLocation = function () {
            if (navigator.geolocation) {
                navigator.geolocation.getCurrentPosition(function(location){
                    priv.map.setCenter(new google.maps.LatLng(location.coords.latitude,
                        location.coords.longitude));
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
            var latitude = current_point.k.toPrecision(4);
            var longitude = current_point.D.toPrecision(4);
            var table = $("#points");

            for(i=0; i<=legs.length - 1; i++){
                var leg = legs[i];
                var start_latitude = leg.start_location.k.toPrecision(4);
                var start_longitude = leg.start_location.D.toPrecision(4);

                if(latitude == start_latitude && longitude == start_longitude){
                    priv.addWayPointOnRoute(leg);
                    table.find("tbody").append("<tr><td>" + leg.start_address + "</td><td>" + leg.distance.text + "</td></tr>");
                }
            }
        }

        priv.secondsToTime = function(secs){
            var hours = Math.floor(secs / (60 * 60));

            var divisor_for_minutes = secs % (60 * 60);
            var minutes = Math.floor(divisor_for_minutes / 60);

            var divisor_for_seconds = divisor_for_minutes % 60;
            var seconds = Math.ceil(divisor_for_seconds);

            return hours + ":" + minutes;
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

            distance = distance / 1000;
            duration = priv.secondsToTime(duration);

            $(".distance_label").html(String(distance).split(".")[0]);
            $(".hour_label").html(duration);

            $.ajax({
                url: window.location.pathname,
                type: "POST",
                data: {
                    trip: trip,
                    distance: distance,
                    duration: duration,
                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
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
                    csrfmiddlewaretoken: $("input[name='csrfmiddlewaretoken']").val(),
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
                    try{
                        priv.addPointOnTable(data, current_point);
                    }catch(e){
                        console.log(e);
                    }
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

        priv.addInitialRoute = function(origin, destination){
            priv.setInitialRoute(origin, destination, true);
            priv.setPoint(origin, destination)
        }

        pub.init = function(){
            if($("#map_canvas").length > 0){
                priv.map = priv.initializeMap();

                if(window.location.pathname.indexOf("show") < 0){
                    priv.setCurrentLocation();
                    google.maps.event.addListener(priv.map, 'click', function(data){
                        var current_point = new google.maps.LatLng(
                            data.latLng.k, data.latLng.D
                        )
                        priv.points.push({location: current_point});
                        priv.addWayPoint(current_point);
                    });
                }else{
                    for(i=0; i <= Directions.waypoints.length - 1; i++){
                        var point = Directions.waypoints[i];
                        var latitude = point.latitude.replace(",", ".");
                        var longitude = point.longitude.replace(",", ".");

                        priv.points.push({
                            location: new google.maps.LatLng(parseFloat(latitude), parseFloat(longitude))
                        });
                    }

                    priv.setPoint(Directions.start_point, Directions.end_point, false,
                        priv.points);
                }
            }


            $("#init-route").submit(function(event){
                event.preventDefault();
                var form = $(this);
                var origin = form.find("input[name='origin']").val();
                var destination = form.find("input[name='destination']").val();

                form.find("button").prop("disabled", true);
                priv.addInitialRoute(origin, destination);
            });

            $("#init-route").submit();

            // google.maps.event.addListener(priv.directionsDisplay, 'directions_changed', function(){

            // });
        }

        return pub;
    }()

}

Mototrip.Create.create.init()

/**
 * Created with PyCharm.
 * User: ggarri
 * Date: 11/2/14
 * Time: 10:45 PM
 * Copyright 2013 (c) trivago GmbH, Palma
 * To change this template use File | Settings | File Templates.
 */

(function(){
    var myApp = angular.module('myApp', []);

    myApp.controller('ContactController', ['$scope', '$http', function($scope, $http) {
        $http.defaults.headers.post['Content-Type']  = 'application/json'
        $http.defaults.headers.common['Accept'] = 'application/json';
        $scope.master = {};

        this.sendForm = function(formRequest) {
            $http.post('management/client/contactform', formRequest).success(function(){
                alert('Email ha sido enviado correctamente.');
                $scope.form = angular.copy($scope.master);
                $scope.contactForm.$setPristine();
            }).fail(function(){
                alert('Error: Asegure que su cuenta de email está escrita correctamente.');
            });
        }
    }]);

//myApp.config(['$routeProvider', function($routeProvider) {
//        $routeProvider
//            .when('/', {
//                controller: 'homeCtrl',
//                templateUrl: 'profile/cv.html'
//            })
//            .otherwise({
//                redirectTo: '/error404'
//            })
//}]);

})();
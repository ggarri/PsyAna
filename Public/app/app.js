/**
 * Created with PyCharm.
 * User: ggarri
 * Date: 11/2/14
 * Time: 10:45 PM
 * Copyright 2013 (c) trivago GmbH, Palma
 * To change this template use File | Settings | File Templates.
 */

(function(){
    var myApp = angular.module('myApp', ['ngUnderscore']);

    myApp.controller('ContactController', ['$http', function($http) {
        $http.defaults.headers.post['Content-Type']  = 'application/json'
        $http.defaults.headers.common['Accept'] = 'application/json';

        this.sendForm = function(formRequest) {
            $http.post('management/client/contactform', formRequest);
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
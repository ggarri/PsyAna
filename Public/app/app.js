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

    myApp.controller('HomeCtrl', ['$scope', function($scope) {
        this.test = 'Angular';
        $scope.test = 'Angular2';
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
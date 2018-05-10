

/* App Module */

var restApp = angular.module("restApp", [
 /*
  'ngRoute',*/
]);

restApp.config(['$locationProvider', function($locationProvider) {
        $locationProvider.html5Mode(true);
    }]);

restApp.controller("ProductTypeCtrl", 
  function($scope,$http) {
    $http.get('http://127.0.0.1:8000/api/products') .then(function(response) {
      $scope.products = response.data;

       
   });
    $scope.val='Likki';
     });
 restApp.controller("ProductModelCtrl", 
   function($scope,$location,$http) {
   
    $http.get('http://127.0.0.1:8000/api/products') .then(function(response) {
      $scope.products = response.data;
       
   });
    if ( $location.search().hasOwnProperty( 'pType' ) ){
       $scope.pType=$location.search()['pType'];

     }
     }); 
  restApp.controller("ProductSCCtrl", 
   function($scope,$location,$http) {
    $scope.pID=0;
    if ( $location.search().hasOwnProperty( 'pID' ) ){
        $scope.pID=$location.search()['pID'];
        $http.get('http://127.0.0.1:8000/api/sl/'+$scope.pID).then(function(response) {
        $scope.serviceCenters = response.data;

       
   });
      
     }
     }); 

  restApp.controller("SCDetailCtrl", 

     
   function($scope,$location,$http) {
    $scope.sID=0;
    if ( $location.search().hasOwnProperty( 'sID' )){
        $scope.sID=$location.search()['sID'];
        $http.get('http://127.0.0.1:8000/api/sc').then(function(response){
          $scope.scList = response.data;
          });
     }
     });   

    
 
    


restApp.filter('unique', function() {

   // and a keyname
   return function(collection, keyname) {
      // we define our output and keys array;
      var output = [], 
          keys = [];
      
      // we utilize angular's foreach function
      // this takes in our original collection and an iterator function
      angular.forEach(collection, function(item) {
          // we check to see whether our object exists
          var key = item[keyname];
          // if it's not already part of our keys array
          if(keys.indexOf(key) === -1) {
              // add it to our keys array
              keys.push(key); 
              // push this item to our final output array
              output.push(item);
          }
      });
      // return our array which should be devoid of
      // any duplicates
      return output;
   };
});

/*restApp.config(
  function ($routeProvider, $locationProvider) {
        // configure the routing rules here
        $routeProvider.when('/:productType', {
            controller: 'ProductModelCtrl'
        });

        // enable HTML5mode to disable hashbang urls
        $locationProvider.html5Mode(true);
    });*/

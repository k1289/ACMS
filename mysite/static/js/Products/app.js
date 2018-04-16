

/* App Module */

var restApp = angular.module("restApp", [
 
  /*'ngRoute',*/
]);



restApp.controller("ProductTypeCtrl", 
  function($scope,$http) {
    $http.get('http://127.0.0.1:8000/api/products') .then(function(response) {
      $scope.products = response.data;
      $scope.productByType = function(myProductType,product){
         
          if(product.ProductType == myProductType) {
              // add it to our keys array
              // push this item to our final output array
              return true;
          }
          return false;
       
   };  
    
  });
    
  });

restApp.filter('unique', function() {
   // we will return a function which will take in a collection
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

/*restApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider.
      when('', {
        templateUrl: 'mysite/home.html',
        controller: 'ProductTypeCtrl'
      }).
      when('/products/', {
        templateUrl: 'product-detail.html',
        controller: 'CategoryDetailCtrl'
  
      });
  }]);*/




/* Controllers */


restApp.controller('ProductTypeCtrl', ['$scope', '$http',
  function($scope, $http) {
    $http.get('http://127.0.0.1:8000/api/products?format=json').success(function(data) {
      $scope.products = data;
      
    });

    
   /* $scope.orderProp = 'id';*/
    
  }]);

/*restAppController.controller('CategoryDetailCtrl', ['$scope','$http','$routeParams',
  function($scope,$http, $routeParams) {
	
	$http.get('/products/'+ $routeParams.categorySlug +'.json').success(function(data) {
	$scope.category = data;
	});
}]);*/
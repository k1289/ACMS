/* App Module */
var restApp = angular.module("ordersApp", ['ngCookies',
 /*
  'ngRoute',*/
]);

restApp.config(['$locationProvider', function($locationProvider) {
        $locationProvider.html5Mode(true);
    }]);

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

restApp.controller("DBrequestsCtrl", 
  function($scope,$http) {
    $http.get('http://127.0.0.1:8000/api/orders/list').then(function(response){
          $scope.orders = response.data;
          });
        $scope.val="";
        $scope.bool=false
        $scope.requests = false;
        $scope.details = false;

        $scope.ShowRequests = function(){
            $scope.requests = true;
            $scope.details = false;
        }
        $scope.ShowDetails = function(){
          $scope.requests = false;
            $scope.details = true;
        }
        $scope.CheckUser= function(user){

         if($scope.val == user)
         {
            $scope.bool=true;
            return $scope.bool;
          }
        }
        
        });
  restApp.controller("PlaceRequestCtrl", 
   function($scope,$http,$cookies) {
    $scope.user = '';
    $scope.problem = ''; 
    $scope.date = new Date()
    var dataObj = {
        product: 2,
        user : $scope.user,
        Problem : $scope.problem,
       Dateofrequest : $scope.date ,
       NumOfrepairdays : "5"
    };  
     $scope.submit = function () {

                var onSuccess = function (data, status, headers, config) {
                    alert('Order placed successfully.');
                };

                var onError = function (data, status, headers, config) {
                    alert('Error occured.');
                }
                $http.defaults.headers.post['X-CSRFToken'] = $cookies['csrftoken'];
                $http.post('/api/orders/create/',dataObj )
                    .success(onSuccess)
                    .error(onError);

            };
  
     }); 

  
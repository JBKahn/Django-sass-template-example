angular.module('todo.service.todo', [])
.factory('TodoService', ['$q', '$http', '$window', function($q, $http, $window) {
    debugger;
    return {
        getTodos: function(){
            var url = $window.jsBootstrap.todoListUrl;
            var params = {};

            var defer = $q.defer();

            $http({method: 'GET', url: url, data: params})
            .success(function(result){
                defer.resolve(result);
            })
            .error(function(error){
                defer.reject(error);
            });

            return defer.promise;
        },
        addTodo: function(todoText){
            var url = $window.jsBootstrap.todoListUrl;
            var params = {
                item: todoText,
                is_done: false
            };

            var defer = $q.defer();

            $http({method: 'POST', url: url, data: params})
            .success(function(result){
                defer.resolve(result);
            })
            .error(function(error){
                defer.reject(error);
            });

            return defer.promise;
        },
        updateTodo: function(id, todoText, status){
            var url = $window.jsBootstrap.todoUpdateUrl;
            var params = {
                id: id,
                item: todoText,
                is_done: status
            };

            var defer = $q.defer();

            $http({method: 'PUT', url: url, data: params})
            .success(function(result){
                defer.resolve(result);
            })
            .error(function(error){
                defer.reject(error);
            });

            return defer.promise;
        },
        removeTodo: function(id){
            var url = $window.jsBootstrap.todoUpdateUrl.replace(/\/0\//, "/" + id + "/");
            var params = {
                id: id
            };

            var defer = $q.defer();

            $http({method: 'DELETE', url: url, data: params})
            .success(function(result){
                defer.resolve(result);
            })
            .error(function(error){
                defer.reject(error);
            });

            return defer.promise;
        },
    };
}]);
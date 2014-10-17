var NgTodoController =  function(TodoService) {
    var self = this;
    self.todoData = {
        newTask: ""
    }
    TodoService.getTodos()
        .then(function (data) {
            self.todoData.todos = data;
        })

    this.addNewTask = function() {
        if (self.todoData.newTask !== "") {
            TodoService.addTodo(self.todoData.newTask)
                .then(function(data) {
                    self.todoData.todos.unshift(data);
                    self.todoData.newTask = "";
                })
        }
    };

    this.clearCompleted = function() {
        var i, uncompleted = [];

        for (i = 0; i < self.todoData.todos.length; i++) {
            if (self.todoData.todos[i].is_done) {
                TodoService.removeTodo(self.todoData.todos[i].id)
                    .then(function(data) {})
            } else {
                uncompleted.push(self.todoData.todos[i])
            }
        }
        self.todoData.todos = uncompleted;
    };

    this.removeTodo = function(index, id) {
        TodoService.removeTodo(id)
            .then(function(data) {
                self.todoData.todos.splice(index, 1);
            })
    };

    this.updateTodoItem = function(todo) {
        TodoService.updateTodo(todo.id, todo.item, todo.is_done);
    };
};
angular.module("todo.controllers.todo", [])
.controller("NgTodoController", ["TodoService", NgTodoController]);

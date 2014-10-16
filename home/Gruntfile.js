// Path Helpers
var appPath = "static_src/";
var bowerPath =  "bower_components/";
var buildPath = "build/";
var staticPath = "static/";

var appConfig = {
    appName: "exampleApp",
    path: {
        appPath: appPath,
        bowerPath:  bowerPath,
        buildPath: buildPath,
        staticPath: staticPath
    }
};

module.exports = function(grunt) {
    require('load-grunt-tasks')(grunt);
    grunt.initConfig({
        appConfig: appConfig,
        concat: {
            js: {
                src: [
                    appConfig.path.bowerPath + 'angular/angular.js',
                    appConfig.path.bowerPath + 'angular-route/angular-route.js',
                    bowerPath + "jquery/dist/jquery.min.js",
                    bowerPath + "bootstrap/dist/js/bootstrap.min.js"
                ],
                dest: buildPath + "js/requirements.dist.js"
            },
            css: {
                src: [
                    bowerPath + "bootstrap/dist/css/bootstrap.min.css",
                    bowerPath + "font-awesome/css/font-awesome.min.css",
                ],
                dest: buildPath + "css/deps.style.dist.css"
            },
            angularApp: {
                src: [
                    appConfig.path.appPath + "js/app.js",
                    appConfig.path.appPath + "js/services/*.js",
                    appConfig.path.appPath + "js/controllers/*.js",
                    appConfig.path.appPath + "js/directives/*.js",
                    appConfig.path.appPath + "js/filters.js"
                ],
                dest: appConfig.path.buildPath + "js/" + appConfig.appName + ".app.js"
            },
            jsDist: {
                src: [
                    appConfig.path.buildPath + "js/requirements.dist.js",
                    appConfig.path.buildPath + "js/" + appConfig.appName + '.templates.js',
                    appConfig.path.buildPath + "js/" +  appConfig.appName + ".app.js"
                ],
                dest: staticPath + '<%= appConfig.appName %>/js/<%= appConfig.appName %>.dist.js'
            },
            cssDist: {
                src: [
                  appConfig.path.buildPath + "css/deps.style.dist.css",
                  appConfig.path.buildPath + "css/app.css"
                ],
                dest: staticPath + '<%= appConfig.appName %>/css/<%= appConfig.appName %>.dist.css'
            }
        },

        copy: {
            main: {
                files: [
                    // includes files within path
                    {expand: true, flatten: true, src: [buildPath + "css/app.css.map"], dest: staticPath + '<%= appConfig.appName %>/css/', filter: "isFile"},
                    {expand: true, flatten: true, src: [bowerPath + "font-awesome/fonts/*"], dest: staticPath + '<%= appConfig.appName %>/fonts/', filter: "isFile"},
                    {expand: true, flatten: true, src: [bowerPath + "bootstrap/fonts/*"], dest: staticPath + '<%= appConfig.appName %>/fonts/', filter: "isFile"},
                    {expand: true, flatten: true, src: [bowerPath + "jquery/dist/jquery.min.map"], dest: staticPath + '<%= appConfig.appName %>/js/lib/', filter: "isFile"},
                    {expand: true, flatten: true, src: [bowerPath + "jquery/dist/jquery.min.js"], dest: staticPath + '<%= appConfig.appName %>/js/lib/', filter: "isFile"},
                ]
            }
        },

        watch: {
            dev: {
                files: [
                    appPath + "sass/*",
                    appPath + "js/*",
                    appPath + "html/*",
                ],
                tasks: ['default']
            }
        },

        sass: {
            dist: {
                files: {
                    "build/css/app.css": appPath + "sass/style.scss",
                },
                options: {
                    sourcemap: "inline",
                }
            }
        },

        ngtemplates: {
            templates: {
                cwd: appConfig.path.appPath,
                options: {
                    module: "templates",
                    standalone: true
                },
                src: "templates/**.html",
                dest: appConfig.path.buildPath + "js/" + appConfig.appName + ".templates.js"
            }
        }
    });

    grunt.registerTask('default', ['sass', 'ngtemplates', 'concat', 'copy']);
    grunt.registerTask('dev', ['default', 'watch']);

};

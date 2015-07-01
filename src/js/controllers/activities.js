'use strict';

var $ = require('jquery');
var _ = require('underscore');
var views = require('views');
var router = require('../router');

router.route('', 'activities', function () {
	showLogin();
	showActivities();
});

function showMain(data) {
	var activitiesTemplate = views['activities'];
    var templateFn = _.template(activitiesTemplate, { variable: 'm' });
    var activitiesHTML = templateFn({ activities: data });
	$('.main-content').html(activitiesHTML);
}

function showActivities() {
	$.ajax({
			method: 'GET', 
			url: '/api/activities/'
  		})
		  .done(function (data){
		  console.log(data);
		  showMain(data);
		  });
}

function showLogin() {
	$.ajax({
			method: 'GET', 
			url: '/api/users/'
  		})
		  	.done(function (data){
			console.log(data);
    		var template = _.template(views['logged-in'], { variable: 'm' });
			console.log()
    		var loginHTML = template(data);
			console.log(loginHTML);
    		$('.nav-content').html(loginHTML);
		});
	
}
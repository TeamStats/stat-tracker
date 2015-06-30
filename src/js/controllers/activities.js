'use strict';

var $ = require('jquery');
var _ = require('underscore');
var views = require('views');
var router = require('../router');

router.route('', 'activities', function () {
	
	$.ajax({
			method: 'GET', 
			url: '/api/users/'
  		})
		  	.done(function (data){
			showLogin(data);
		});
	showMain();
});

function showMain() {
	var mainTemplate = views['activities'];
	$('.main-content').html(mainTemplate);
}

function showLogin(data) {
	console.log(data);
    var template = _.template(views['logged-in'], { variable: 'm' });
	console.log()
    var loginHTML = template(data);
	console.log(loginHTML);
    $('.nav-content').html(loginHTML);
}
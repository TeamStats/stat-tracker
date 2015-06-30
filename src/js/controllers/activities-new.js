'use strict';

var $ = require('jquery');
var _ = require('underscore');
var views = require('views');
var router = require('../router');

router.route('activities/new', function () {
	
	showMain();
	getCookie('csrftoken');  
	$('.newactivity-form').on('submit', function(e){
		e.preventDefault();
		var data = $('#newAct').val();
		console.log(data);
		$.ajax({
			method: 'POST', 
			url: '/api/activities/',
			data: data
  		}).done(function (data){
			  alert('saved');
			console.log(data);
		});
	});
});

function showMain() {
	var mainTemplate = views['activities-new'];
	$('.main-content').html(mainTemplate);
}


function getCookie(name) {
   var cookieValue = null;
   if (document.cookie && document.cookie != '') {
       var cookies = document.cookie.split(';');
       for (var i = 0; i < cookies.length; i++) {
           var cookie = $.trim(cookies[i]);
           // Does this cookie string begin with the name we want?
           if (cookie.substring(0, name.length + 1) == (name + '=')) {
               cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
               break;
           }
       }
   }
   console.log(cookieValue);
   return cookieValue;
}
   


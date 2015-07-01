'use strict';

var $ = require('jquery');
var _ = require('underscore');
var views = require('views');
var router = require('../router');
var datepicker = require('../../../node_modules/jquery-ui/datepicker.js')


router.route('activities/:id', function (Id) {
$.ajax({
	method: 'GET', 
	url: '/api/activities/'+Id+'/stat/'	
	})
	.done(function(data){
		console.log(data);
	});
$.ajax({
			method: 'GET', 
			url: '/api/activities/'+Id
  		})
		.then(renderDetails)
		.then(addStat);
		
   		
});

	
		  
		  


 function renderDetails(data) {
	console.log(data);
    var activityTemplate = views['activity-details'];
    var templateFn = _.template(activityTemplate, { variable: 'm' });
    var activityHTML = templateFn(data);
    $('.main-content').html(activityHTML);
	return data;
 }
 
 function addStat(data) {
	 $('.date').datepicker({
		 dateFormat: "yy-mm-dd"
		 });
	 var Id = data.id;
	 $('.new-stat').on('submit', function(e){
			e.preventDefault();
			var date = $('.date').val();
			console.log(date);
			var stat = $('.stat').val();
			console.log(stat);
			var csrftoken = getCookie('csrftoken'); 
			console.log(Id);
			$.ajax({
				beforeSend: function (request){
				console.log(csrftoken)
	            request.setRequestHeader('X-CSRFToken', csrftoken);
	           	},
				method: 'POST', 
				url: '/api/activities/'+Id+'/stat/',
				data: {'stat': stat, 'timestamp': date}
  			}).done(function (data){
			  alert('saved');
			console.log(data);
		});
		});
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
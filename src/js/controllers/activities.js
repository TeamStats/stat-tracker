'use strict';

var $ = require('jquery');
var _ = require('underscore');
var views = require('views');
var router = require('../router');

router.route('', 'activities', function () {
	showMain();
});

function showMain() {
	var mainTemplate = views['activities'];
	$('.main-content').html(mainTemplate);
}
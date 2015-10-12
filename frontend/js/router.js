/*global define */

define(function (require) {
	'use strict';

	var Marionette = require('marionette');


	return Marionette.AppRouter.extend({
		appRoutes: {
			'': 'showPage',
			'page/:pageName': 'showPage',
            'hi': 'hello'
		}
	});
});

require.config({
	paths: {
		underscore: '../bower_components/underscore/underscore',
		backbone: '../bower_components/backbone/backbone',
		marionette: '../bower_components/backbone.marionette/lib/backbone.marionette',
		jquery: '../bower_components/jquery/dist/jquery',
		localStorage: '../bower_components/backbone.localStorage/backbone.localStorage',
        'backbone.radio': '../bower_components/backbone.radio/build/backbone.radio',
		tpl: 'lib/tpl',
        bootstrap: 'lib/bootstrap.min'
	},

    map: {
        '*': {
            'backbone.wreqr': 'backbone.radio'
        }
    },

	shim: {
		underscore: {
			exports: '_'
		},

		backbone: {
			exports: 'Backbone',
			deps: ['jquery', 'underscore']
		},

		marionette: {
			exports: 'Backbone.Marionette',
			deps: ['backbone']
		},

        bootstrap: {
            deps: ['jquery']
        }

	},
    waitSeconds: 60
});

require([
	'app',
    'jquery',
	'bootstrap',
    'backbone.radio'
], function (app, $) {
	'use strict';

	app.start();
});

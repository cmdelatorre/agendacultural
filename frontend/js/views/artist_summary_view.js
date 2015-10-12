/*global define */

define(function (require) {
	'use strict';

    var Marionette = require('marionette'),
        templates = require('templates'),
        Artist = require('models/artist'),
        PageView = require('views/PageView');


	return Marionette.ItemView.extend({
		template: templates.artistSummary,
        className: 'col-sm-1 col-md-3',
        model: Artist,

		ui: {
			edit: '[data-js-edit]',
            remove: '[data-js-remove]'
		},

		events: {
            "click @ui.edit": "handleEvent",
            "click @ui.remove": "handleEvent"
        },
        modelEvents: {
            "change": function() {
                this.render();
            }
        },
        handleEvent: function (evt) {
            console.log(evt);
        }
	});
});

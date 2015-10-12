/*global define */

define(function (require) {
	'use strict';

    var Marionette = require('marionette'),
        templates = require('templates'),
        Page = require('models/Page'),
        PageView = require('views/PageView');


	return Marionette.ItemView.extend({
		template: templates.menuItem,
        tagName: 'li',
        model: Page,

		ui: {
			link: 'a'
		},

		events: {
			'click a': 'activateMenu'
		},
        modelEvents: {
            "change:active": function() {
                this.render();
            }
        },

        activateMenu: function (event) {
            window.app.vent.trigger('menu:activate', this.model);
            window.app.main.show(new PageView({model: this.model}));
		},

        onRender: function() {
            if(this.model.get('active')) this.$el.addClass('active');
        }

	});
});

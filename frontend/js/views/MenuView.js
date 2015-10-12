/*global define */

define(function (require) {
	'use strict';

	var Marionette = require('marionette'),
		MenuItemView = require('views/MenuItemView');

	return Marionette.CollectionView.extend({
        childView: MenuItemView,
        tagName: 'ul',
        className: 'nav nav-pills pull-right'
	});

});

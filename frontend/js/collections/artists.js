/*global define */

define(function (require) {
	'use strict';

    var Backbone = require('backbone'),
        Artist = require('models/artist');

	return Backbone.Collection.extend({
		model: Artist
	});
});

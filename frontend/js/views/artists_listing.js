/*global define */

define(function (require) {
	'use strict';

	var Marionette = require('marionette'),
		ArtistSummaryView = require('views/artist_summary_view');

	return Marionette.CollectionView.extend({
        childView: ArtistSummaryView,
        className: 'row'
	});

});

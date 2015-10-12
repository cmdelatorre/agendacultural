/*global define */

define(function (require) {
	'use strict';

	return {
        pages : {
            about: require('tpl!templates/pages/about.html'),
            artists: require('tpl!templates/pages/artists.html'),
            contact: require('tpl!templates/pages/contact.html'),
            home: require('tpl!templates/pages/home.html'),
            event: require('tpl!templates/pages/event.html')
        },
        artistSummary: require('tpl!templates/artist_summary.html'),

        // Boilerplate
        page: require('tpl!templates/page.html'),
        menuItem: require('tpl!templates/menuItem.html'),
		footer: require('tpl!templates/footer.html')
	};
});


/*global define */

define(function (require) {
	'use strict';

	return {
        pages : {
          home: require('tpl!templates/pages/home.html'),
          about: require('tpl!templates/pages/about.html'),
          contact: require('tpl!templates/pages/contact.html'),
          newAgendaEvent: require('tpl!templates/pages/new_event.html')
        },
        page: require('tpl!templates/page.html'),
        menuItem: require('tpl!templates/menuItem.html'),
		footer: require('tpl!templates/footer.html')
	};
});


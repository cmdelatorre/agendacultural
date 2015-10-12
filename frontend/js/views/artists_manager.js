/*global define */

define(function (require) {
	'use strict';

	var Artists = require('collections/artists'),
        ArtistsView = require('views/artists_listing'),
        Marionette = require('marionette'),
        templates = require('templates');

    var data = new Artists([
        {name: "Carlos Gimenez", photo: 'http://lorempixel.com/200/300/'},
        {name: "Andres Calamaro", photo: 'http://lorempixel.com/300/200/'},
        {name: "Tupac Gomez", photo: 'http://lorempixel.com/200/150/'},
        {name: "Tito Andrónico", photo: 'http://lorempixel.com/150/200/'},
        {name: "Lolo Marquizano", photo: 'http://lorempixel.com/250/200/'},
        {name: "Aoki Itikizamura", photo: 'http://lorempixel.com/200/250/'},
        {name: "Ae Ae y Arriba Arriba", photo: 'http://lorempixel.com/190/200/'},
        {name: "Andres Calamaro", photo: 'http://lorempixel.com/200/190/'},
        {name: "Carlos Gimenez", photo: 'http://lorempixel.com/210/200/'},
        {name: "Andres Calamaro", photo: 'http://lorempixel.com/200/210/'},
        {name: "Carlos Gimenez", photo: 'http://lorempixel.com/220/200/'},
        {name: "Andres Calamaro", photo: 'http://lorempixel.com/200/220/'}
    ]);

    return Marionette.LayoutView.extend({
        template: templates.pages.artists,

        regions: {
            artists: "[data-js-artists]"
        },

        onBeforeShow: function() {
            this.showChildView('artists', new ArtistsView({collection: data}));
        }
    });

});

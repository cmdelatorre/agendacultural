/*global define */

define(function (require) {
	'use strict';

    var AppRouter = require('router'),
        ArtistsManager = require('views/artists_manager'),
        Backbone = require('backbone'),
        DialogRegion = require('regions/dialog'),
        Footer = require('views/Footer'),
        HomeView = require('views/HomeView'),
        Marionette = require('marionette'),
        MenuView = require('views/MenuView'),
        Nav = require('collections/nav'),
        NotifyRegion = require('regions/notification'),
        PageView = require('views/PageView');


	var app = new Marionette.Application();

    app.pages = new Nav([
        {title: 'Home', name: 'home', active: true},
        {title: 'New event', name: 'event'},
        {title: 'About', name: 'about'},
        {title: 'Contact', name: 'contact'}
    ]);
    var menu = new MenuView({collection: app.pages});

	app.addRegions({
		menu: '#main-nav',
		main: '#main',
		footer: '#footer',
        notification: {
            selector: "#notification",
            regionType: NotifyRegion
        },
        dialog: {
            selector: "#dialog",
            regionType: DialogRegion
        }
	});

    app.router = new AppRouter({
        controller: {
            showPage: function (pageName) {
                if(pageName == null) pageName = 'home';

                console.log('Router => Showing page: ' + pageName);
                var pageModel = app.pages.findWhere({name: pageName});

                //app.vent.trigger('menu:activate', pageModel);
                if(pageName == 'home') {
                    app.main.show(new HomeView({model: pageModel}));
                } else if(pageName == 'artists') {
                    app.main.show(new ArtistsManager());
                } else {
                    app.main.show(new PageView({model: pageModel}));
                }
            },
            hello: function() {
                console.log('In route /hi');
            }
        }
    });

    app.on("start", function(options){
        app.menu.show(menu);
		app.footer.show(new Footer());

        if (Backbone.history){
            Backbone.history.start();
        }
    });

	app.vent.on('menu:activate', function (activePageModel) {
        menu.collection.findWhere({active: true})
            .set('active', false);
        activePageModel.set('active', true);
        menu.render();
	});

    /**
     * Sample JSON Data
     * app.commands.execute("app:notify", {
     *           type: 'warning'    // Optional. Can be info(default)|danger|success|warning
     *           title: 'Success!', // Optional
     *           description: 'We are going to remove Team state!'
     *       });
     */
    app.commands.setHandler("app:notify", function(jsonData) {
        require(['views/NotificationView'], function(NotifyView) {
            app.notification.show(new NotifyView({
                model: new Backbone.Model(jsonData)
            }));
        });
    });

    /**
     * @example
     * app.commands.execute("app:dialog:simple", {
     *           icon: 'info-sign'    // Optional. default is (glyphicon-)bell
     *           title: 'Dialog title!', // Optional
     *           message: 'The important message for user!'
     *       });
     */
    app.commands.setHandler("app:dialog:simple", function(data) {
        require(['views/DialogView', 'models/Dialog', 'tpl!templates/simpleModal.html'],
            function(DialogView, DialogModel, ModalTpl) {

                app.dialog.show(new DialogView({
                    template: ModalTpl,
                    model: new DialogModel(data)
                }));
            });
    });

    /**
     * @example
     * app.commands.execute("app:dialog:confirm", {
     *           icon: 'info-sign'    // Optional. default is (glyphicon-)bell
     *           title: 'Dialog title!', // Optional
     *           message: 'The important message for user!'
     *           'confirmYes': callbackForYes, // Function to execute of Yes clicked
     *           'confirmNo': callbackForNo, // Function to execute of No clicked
     *       });
     */
    app.commands.setHandler("app:dialog:confirm", function(data) {
        require(['views/DialogView', 'models/Dialog', 'tpl!templates/confirmModal.html'],
            function(DialogView, DialogModel, ModalTpl) {

                app.dialog.show(new DialogView({
                    template: ModalTpl,
                    model: new DialogModel(data),
                    events: {
                        'click .dismiss': 'dismiss',
                        'click .confirm_yes': data.confirmYes,
                        'click .confirm_no': data.confirmNo
                    }
                }));
            });
    });

	return window.app = app;
});

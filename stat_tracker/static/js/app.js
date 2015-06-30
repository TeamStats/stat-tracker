(function e(t, n, r) {
    function s(o, u) {
        if (!n[o]) {
            if (!t[o]) {
                var a = typeof require == "function" && require;
                if (!u && a)return a(o, !0);
                if (i)return i(o, !0);
                var f = new Error("Cannot find module '" + o + "'");
                throw f.code = "MODULE_NOT_FOUND", f
            }
            var l = n[o] = {exports: {}};
            t[o][0].call(l.exports, function (e) {
                var n = t[o][1][e];
                return s(n ? n : e)
            }, l, l.exports, e, t, n, r)
        }
        return n[o].exports
    }

    var i = typeof require == "function" && require;
    for (var o = 0; o < r.length; o++)s(r[o]);
    return s
})({
    1: [function (require, module, exports) {
        "use strict";
        function showMain() {
            var e = views["activities-new"];
            $(".main-content").html(e)
        }

        var $ = require("jquery"), _ = require("underscore"), views = require("views"), router = require("../router");
        router.route("activities/new", function () {
            showMain(), $(".newactivity-form").on("submit", function (e) {
                e.preventDefault();
                var i = $("#newAct").val();
                console.log(i), $.ajax({method: "POST", url: "/api/activities/", data: i}).done(function (e) {
                    alert("saved"), console.log(e)
                })
            })
        });

    }, {"../router": 4, "jquery": "jquery", "underscore": "underscore", "views": "views"}],
    2: [function (require, module, exports) {
        "use strict";
        function showMain() {
            var e = views.activities;
            $(".main-content").html(e)
        }

        var $ = require("jquery"), _ = require("underscore"), views = require("views"), router = require("../router");
        router.route("", "activities", function () {
            showMain()
        });

    }, {"../router": 4, "jquery": "jquery", "underscore": "underscore", "views": "views"}],
    3: [function (require, module, exports) {
        "use strict";
        var router = require("./router");
        ({
            controllers: {
                "activities-new": require("./controllers/activities-new.js"),
                activities: require("./controllers/activities.js")
            }
        }), router.init();

    }, {"./controllers/activities-new.js": 1, "./controllers/activities.js": 2, "./router": 4}],
    4: [function (require, module, exports) {
        "use strict";
        var SortedRouter = require("./sorted-router");
        module.exports = new SortedRouter;

    }, {"./sorted-router": 5}],
    5: [function (require, module, exports) {
        "use strict";
        var Backbone = require("backbone"), _ = require("underscore"), SortedRouter = Backbone.Router.extend({
            sortedRoutes: {},
            route: function () {
                for (var e = arguments.length - 1, t = arguments[arguments.length - 1], r = 0; e > r; ++r)this.sortedRoutes[arguments[r]] = t
            },
            init: function () {
                var e = -1e6, t = this;
                _.chain(_.pairs(this.sortedRoutes)).sortBy(function (t) {
                    var r = t[0];
                    return r.indexOf("*") >= 0 ? e : -r.split(":").length
                }).each(function (e) {
                    Backbone.Router.prototype.route.apply(t, e)
                }), Backbone.history.start()
            }
        });
        module.exports = SortedRouter;

    }, {"backbone": "backbone", "underscore": "underscore"}]
}, {}, [3])


//# sourceMappingURL=app.js.map
require = (function e(t, n, r) {
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
    "views": [function (require, module, exports) {
        var views = {
            "activities-new": "<h1> New Activity </h1>\n<form class=\"newactivity-form\">\n\t<input id=\"newAct\" placeholder=\"Activity Title\">\n\t<button class=\"create-activity\">Create</button>\n</form>",
            "activities": "<h1>Activities</h1>\n<a href=\"activities/login/\">Login</a>\n<a href=\"activities/register/\">Register</a>\n<a class=\"new-activity\" href=\"#/activities/new\">Create New Activity</a>\n\n<% m.activities.forEach(function (activity) { %>\n\t<li class=\"activity\">\n      <a href=\"#activities/<%- activity.id %>\">\n        <%- activity.title %>\n      </a>\n    </li>\n<% }) %>",
            "activity-details": "<h1><%- m.title %></h1>\n\t\n<form class=\"new-stat\">\n<input class=\"date\" name=\"date\" placeholder=\"Date\">\n<input class=\"stat\" name=\"reps\" placeholder=\"Stat\">\n<button class=\"submit-form\">Submit</button>\n</form>\n\n",
            "logged-in": "<a href=\"activities/logout/\">Logout</a>\n<p class=\"userLogin\"><%- m[0].username %></p>\n",
            "not-loggedin": "<a href=\"activities/login/\">Login</a>\n<a href=\"activities/register/\">Register</a>"
        };
        if (typeof module !== "undefined" && module.exports) {
            module.exports = views;
        }
    }, {}]
}, {}, []);

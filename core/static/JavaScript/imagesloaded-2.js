/*! * imagesLoaded PACKAGED v3.1.4 * JavaScript is all like "You images are done yet or what?" * MIT License */
document.addEventListener("DOMContentLoaded", function() {
    (function () {
        function e() {
        }

        function t(e, t) {
            for (var n = e.length; n--;)
                if (e[n].listener === t) return n;
            return -1
        }

        function n(e) {
            return function () {
                return this[e].apply(this, arguments)
            }
        }

        var i = e.prototype,
            r = this,
            o = r.EventEmitter;
        i.getListeners = function (e) {
            var t, n, i = this._getEvents();
            if ("object" == typeof e) {
                t = {};
                for (n in i) i.hasOwnProperty(n) && e.test(n) && (t[n] = i[n])
            } else t = i[e] || (i[e] = []);
            return t
        }, i.flattenListeners = function (e) {
            var t, n = [];
            for (t = 0; t < e.length; t += 1) n.push(e[t].listener);
            return n
        }, i.getListenersAsObject = function (e) {
            var t, n = this.getListeners(e);
            return n instanceof Array && (t = {}, t[e] = n), t || n
        }, i.addListener = function (e, n) {
            var i, r = this.getListenersAsObject(e),
                o = "object" == typeof n;
            for (i in r) r.hasOwnProperty(i) && -1 === t(r[i], n) && r[i].push(o ? n : {
                listener: n,
                once: !1
            });
            return this
        }, i.on = n("addListener"), i.addOnceListener = function (e, t) {
            return this.addListener(e, {
                listener: t,
                once: !0
            })
        }, i.once = n("addOnceListener"), i.defineEvent = function (e) {
            return this.getListeners(e), this
        }, i.defineEvents = function (e) {
            for (var t = 0; t < e.length; t += 1) this.defineEvent(e[t]);
            return this
        }, i.removeListener = function (e, n) {
            var i, r, o = this.getListenersAsObject(e);
            for (r in o) o.hasOwnProperty(r) && (i = t(o[r], n), -1 !== i && o[r].splice(i, 1));
            return this
        }, i.off = n("removeListener"), i.addListeners = function (e, t) {
            return this.manipulateListeners(!1, e, t)
        }, i.removeListeners = function (e, t) {
            return this.manipulateListeners(!0, e, t)
        }, i.manipulateListeners = function (e, t, n) {
            var i, r, o = e ? this.removeListener : this.addListener,
                s = e ? this.removeListeners : this.addListeners;
            if ("object" != typeof t || t instanceof RegExp)
                for (i = n.length; i--;) o.call(this, t, n[i]);
            else
                for (i in t) t.hasOwnProperty(i) && (r = t[i]) && ("function" == typeof r ? o.call(this, i, r) : s.call(this, i, r));
            return this
        }, i.removeEvent = function (e) {
            var t, n = typeof e,
                i = this._getEvents();
            if ("string" === n) delete i[e];
            else if ("object" === n)
                for (t in i) i.hasOwnProperty(t) && e.test(t) && delete i[t];
            else delete this._events;
            return this
        }, i.removeAllListeners = n("removeEvent"), i.emitEvent = function (e, t) {
            var n, i, r, o, s = this.getListenersAsObject(e);
            for (r in s)
                if (s.hasOwnProperty(r))
                    for (i = s[r].length; i--;) n = s[r][i], n.once === !0 && this.removeListener(e, n.listener), o = n.listener.apply(this, t || []), o === this._getOnceReturnValue() && this.removeListener(e, n.listener);
            return this
        }, i.trigger = n("emitEvent"), i.emit = function (e) {
            var t = Array.prototype.slice.call(arguments, 1);
            return this.emitEvent(e, t)
        }, i.setOnceReturnValue = function (e) {
            return this._onceReturnValue = e, this
        }, i._getOnceReturnValue = function () {
            return this.hasOwnProperty("_onceReturnValue") ? this._onceReturnValue : !0
        }, i._getEvents = function () {
            return this._events || (this._events = {})
        }, e.noConflict = function () {
            return r.EventEmitter = o, e
        }, "function" == typeof define && define.amd ? define("eventEmitter/EventEmitter", [], function () {
            return e
        }) : "object" == typeof module && module.exports ? module.exports = e : this.EventEmitter = e
    }).call(this),
        function (e) {
            function t(t) {
                var n = e.event;
                return n.target = n.target || n.srcElement || t, n
            }

            var n = document.documentElement,
                i = function () {
                };
            n.addEventListener ? i = function (e, t, n) {
                e.addEventListener(t, n, !1)
            } : n.attachEvent && (i = function (e, n, i) {
                e[n + i] = i.handleEvent ? function () {
                    var n = t(e);
                    i.handleEvent.call(i, n)
                } : function () {
                    var n = t(e);
                    i.call(e, n)
                }, e.attachEvent("on" + n, e[n + i])
            });
            var r = function () {
            };
            n.removeEventListener ? r = function (e, t, n) {
                e.removeEventListener(t, n, !1)
            } : n.detachEvent && (r = function (e, t, n) {
                e.detachEvent("on" + t, e[t + n]);
                try {
                    delete e[t + n]
                } catch (i) {
                    e[t + n] = void 0
                }
            });
            var o = {
                bind: i,
                unbind: r
            };
            "function" == typeof define && define.amd ? define("eventie/eventie", o) : e.eventie = o
        }(this),
        function (e, t) {
            "function" == typeof define && define.amd ? define(["eventEmitter/EventEmitter", "eventie/eventie"], function (n, i) {
                return t(e, n, i)
            }) : "object" == typeof exports ? module.exports = t(e, require("eventEmitter"), require("eventie")) : e.imagesLoaded = t(e, e.EventEmitter, e.eventie)
        }(this, function (e, t, n) {
            function i(e, t) {
                for (var n in t) e[n] = t[n];
                return e
            }

            function r(e) {
                return "[object Array]" === d.call(e)
            }

            function o(e) {
                var t = [];
                if (r(e)) t = e;
                else if ("number" == typeof e.length)
                    for (var n = 0, i = e.length; i > n; n++) t.push(e[n]);
                else t.push(e);
                return t
            }

            function s(e, t, n) {
                if (!(this instanceof s)) return new s(e, t);
                "string" == typeof e && (e = document.querySelectorAll(e)), this.elements = o(e), this.options = i({}, this.options), "function" == typeof t ? n = t : i(this.options, t), n && this.on("always", n), this.getImages(), u && (this.jqDeferred = new u.Deferred);
                var r = this;
                setTimeout(function () {
                    r.check()
                })
            }

            function f(e) {
                this.img = e
            }

            function c(e) {
                this.src = e, v[e] = this
            }

            var u = e.jQuery,
                a = e.console,
                h = "undefined" != typeof a,
                d = Object.prototype.toString;
            s.prototype = new t, s.prototype.options = {}, s.prototype.getImages = function () {
                this.images = [];
                for (var e = 0, t = this.elements.length; t > e; e++) {
                    var n = this.elements[e];
                    "IMG" === n.nodeName && this.addImage(n);
                    for (var i = n.querySelectorAll("img"), r = 0, o = i.length; o > r; r++) {
                        var s = i[r];
                        this.addImage(s)
                    }
                }
            }, s.prototype.addImage = function (e) {
                var t = new f(e);
                this.images.push(t)
            }, s.prototype.check = function () {
                function e(e, r) {
                    return t.options.debug && h && a.log("confirm", e, r), t.progress(e), n++, n === i && t.complete(), !0
                }

                var t = this,
                    n = 0,
                    i = this.images.length;
                if (this.hasAnyBroken = !1, !i) return void this.complete();
                for (var r = 0; i > r; r++) {
                    var o = this.images[r];
                    o.on("confirm", e), o.check()
                }
            }, s.prototype.progress = function (e) {
                this.hasAnyBroken = this.hasAnyBroken || !e.isLoaded;
                var t = this;
                setTimeout(function () {
                    t.emit("progress", t, e), t.jqDeferred && t.jqDeferred.notify && t.jqDeferred.notify(t, e)
                })
            }, s.prototype.complete = function () {
                var e = this.hasAnyBroken ? "fail" : "done";
                this.isComplete = !0;
                var t = this;
                setTimeout(function () {
                    if (t.emit(e, t), t.emit("always", t), t.jqDeferred) {
                        var n = t.hasAnyBroken ? "reject" : "resolve";
                        t.jqDeferred[n](t)
                    }
                })
            }, u && (u.fn.imagesLoaded = function (e, t) {
                var n = new s(this, e, t);
                return n.jqDeferred.promise(u(this))
            }), f.prototype = new t, f.prototype.check = function () {
                var e = v[this.img.src] || new c(this.img.src);
                if (e.isConfirmed) return void this.confirm(e.isLoaded, "cached was confirmed");
                if (this.img.complete && void 0 !== this.img.naturalWidth) return void this.confirm(0 !== this.img.naturalWidth, "naturalWidth");
                var t = this;
                e.on("confirm", function (e, n) {
                    return t.confirm(e.isLoaded, n), !0
                }), e.check()
            }, f.prototype.confirm = function (e, t) {
                this.isLoaded = e, this.emit("confirm", this, t)
            };
            var v = {};
            return c.prototype = new t, c.prototype.check = function () {
                if (!this.isChecked) {
                    var e = new Image;
                    n.bind(e, "load", this), n.bind(e, "error", this), e.src = this.src, this.isChecked = !0
                }
            }, c.prototype.handleEvent = function (e) {
                var t = "on" + e.type;
                this[t] && this[t](e)
            }, c.prototype.onload = function (e) {
                this.confirm(!0, "onload"), this.unbindProxyEvents(e)
            }, c.prototype.onerror = function (e) {
                this.confirm(!1, "onerror"), this.unbindProxyEvents(e)
            }, c.prototype.confirm = function (e, t) {
                this.isConfirmed = !0, this.isLoaded = e, this.emit("confirm", this, t)
            }, c.prototype.unbindProxyEvents = function (e) {
                n.unbind(e.target, "load", this), n.unbind(e.target, "error", this)
            }, s
        })
    })
var template = "<span id=\"{0}\" class=\"label {1} _tag\" >{2}&nbsp<a href=\"#\" data-toggle=\"tooltip\" title=\"删除条件\" class=\"close-tag\" onclick=\"closeIt('{3}', {4})\">&times</a></span>"
/*global map*/
var tagsMap = new Map()

_setEvent("company_id",  "comp_{0}", template, "label-warning")
_setEvent("tags", "tags_{0}", template, "label-info")
_setEvent("clause", "clause_{0}", template, "label-danger")

function _setEvent(name, keyPlate, template, css) {
    var ckBox = $("[name="+name+"][type=checkbox]")
    var radio = $("[name="+name+"][type=radio]")
    radio.click(function () {
        ckBox.each(function (i, elem) {
            var cb = $(elem)
            if (cb.attr('checked') === 'checked' || cb.attr('checked') === true){
                tagsMap.remove(keyPlate.format(cb.val()))
                cb.removeAttr('checked')
            }
        })
        print_tags(tagsMap)
    })

    /**设置复选框事件*/
    ckBox.each(function (i, elem) {
        var cb = $(elem)
        cb.click(function () {
            radio.removeAttr("checked")
            var key = keyPlate.format(cb.val())
            var label = template.format(cb.val(), css, cb.parent().text(), name, cb.val())
            if (cb.attr('checked') === 'checked' || cb.attr('checked') === true) {
                tagsMap.remove(key)
                cb.removeAttr('checked')
            } else {
                cb.attr('checked', 'true')
                tagsMap.put(key, label)
            }
            print_tags(tagsMap)
        })
    })
}

function closeIt(name, value) {
    $("[name="+name+"][type=checkbox][value="+value+"]").click()
}

function print_tags(map) {
    var conditions = $("#conditions")
    conditions.empty()
    var p = conditions.append("<p></p>").last()
    map.each(function (key, value, index) {
        if ((index + 1) % 8 === 0) {
            p = conditions.append("<p></p>").last()
        }
        p.append(value)
    })
}

/**
 * string format:
 * useage:
 * "<a href=\"{0}\">{1}</>".format('http://www.', 'link to')
 * "<a href=\"{url}\">{name}</>".format({url:'http://www.', name:'link to'})
 * */
String.prototype.format = function (args) {
    if (arguments.length > 0) {
        var result = this
        if (arguments.length == 1 && typeof (args) == "object") {
            for (var key in args) {
                var reg = new RegExp("({" + key + "})", "g")
                result = result.replace(reg, args[key])
            }
        }
        else {
            for (var i = 0; i < arguments.length; i++) {
                if (arguments[i] == undefined) {
                    return ""
                }
                else {
                    var reg = new RegExp("({[" + i + "]})", "g")
                    result = result.replace(reg, arguments[i])
                }
            }
        }
        return result
    }
    else {
        return this
    }
}
/**
 * 自定义key-value Map
 * 支持添加，删除，获取，迭代，keys等基本操作
 * @constructor
 */
function Map() {
    this.keys = new Array()
    this.data = new Object()

    this.put = function (key, value) {
        if (this.data[key] == null) {
            this.keys.push(key)
        }
        this.data[key] = value
    }

    this.get = function (key) {
        return this.data[key]
    }

    this.remove = function (key) {
        this.keys.remove(key)
        this.data[key] = null
    }

    this.each = function (fn) {
        if (typeof fn != 'function') {
            return
        }
        var len = this.keys.length
        for (var i = 0; i < len; i++) {
            var k = this.keys[i]
            fn(k, this.data[k], i)
        }
    }

    this.entrys = function () {
        var len = this.keys.length
        var entrys = new Array(len)
        for (var i = 0; i < len; i++) {
            entrys[i] = {
                key: this.keys[i],
                value: this.data[i]
            }
        }
        return entrys
    }

    this.isEmpty = function () {
        return this.keys.length == 0
    }

    this.size = function () {
        return this.keys.length
    }
}
/**
 * array remove method
 * @returns {*}
 */
Array.prototype.remove = function() {
    var what, a = arguments, L = a.length, ax;
    while (L && this.length) {
        what = a[--L];
        while ((ax = this.indexOf(what)) !== -1) {
            this.splice(ax, 1);
        }
    }
    return this;
};
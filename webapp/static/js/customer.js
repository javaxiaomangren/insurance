//设置下拉框的事件
setEvents("#min_age_list", "a", function () {
    $("#age_min").val(this.text)
})

setEvents("#max_age_list", "a", function () {
    $("#age_max").val(this.text)
})

setEvents("#clause_list", "a", function () {
    $("#clause").val(this.text)
})

setEvents("#limit_list", "a", function () {
    $("#limit").val(this.text)
    $("#limits").val(this.text)
})

setEvents("#tags_list", "a", function () {
    var oldval = $("#tags").val()
    $("#tags").val(this.text + "," + oldval)
    $("#tags").css("display", "inline")
})
//表单验证
$("#insu_form").submit(function () {
    if ($("#pro_name").val() === "") {
        alert("产品名称不能为空")
        return false
    }
    var min_age = $("#age_min").val()
    var max_age = $("#age_max").val()
    if (max_age === "") {
        alert("请填写年龄")
        return false
    }
    if (min_age != "") {
        a = handle_age(min_age)
        if (a > 0) {
            $("#age_min").val(a)
        }
    }
    a = handle_age(max_age)
    if (a > 0) {
        $("#age_max").val(a)
    }

    if ($("#insu_days").val() === "") {
        alert("保期不能为空")
        return false
    }
    if ($("#clause_limit").val() === "") {
        alert("条款！！！")
        return false
    }


})

function setEvents(id, find, func) {
    $(id).find(find).each(function (i, elem) {
        $(elem).click(func)
    })
}

function generate() {
    var oldval = $("#clause_limit").val()
    var clause = $("#clause").val()
    var limit = $("#limits").val()
    if (clause != "" && limit != "") {
        var value = clause + ":" + limit
        if (oldval != "") {
            value = oldval + ", " + value
        }
        $("#clause_limit").val(value)
        limit = $("#limits").val("")
        $("#clause_limit").css("display", "inline")
    }
}



/**
 *转换时间字符到整数
 * @param age
 * @returns {number}
 * Usage:
 * date_to_num("2年") rt:730
 * date_to_num("2岁") rt:730
 * date_to_num("3天") rt:3
 */
function date_to_num(arg) {

    if (isRegularNum(arg)) {
        return arg
    }
    arg = arg.replace("岁", "年")
    var idx_y = arg.indexOf("年")
    var idx_d = arg.indexOf("天")
    if (idx_y > -1 && idx_y == arg.length-1) {
        var num = arg.slice(0, idx_y)
        if (isRegularNum(num)) {
            return parseInt(num) * 365
        }
        return -1
    }
    if (idx_d > -1 && idx_d == arg.length-1) {
        var num = arg.slice(0, idx_d)
        if (isRegularNum(num)) {
            return parseInt(num)
        }
        return -1
    }
    return -1
}
/**
 * 转换价格字符到整数
 * @param str
 * @returns {number}
 * usage str_to_name("5百")
 * usage str_to_name("5千")
 * usage str_to_name("10万")
 * usage str_to_name("10０万")
 */
function str_to_num(str){
    if (isRegularNum(str)) {
        return str
    }
    if (str.indexOf("百") > -1) {
        var num = str.slice(0, str.indexOf("百"))
        if (isRegularNum(num)) {
            return parseInt(num) * 100.0
        }
    }
    if (str.indexOf("千") > -1) {
        var num = str.slice(0, str.indexOf("千"))
        if (isRegularNum(num)) {
            return parseInt(num) * 1000.0
        }
    }
    if (str.indexOf("万") > -1) {
        var num = str.slice(0, str.indexOf("万"))
        if (isRegularNum(num)) {
            return parseInt(num) * 10000.0
        }
    }
    return -1
}

function isRegularNum(num) {
    var reg = new RegExp("^[0-9]*$");
    if (reg.test(num) && parseInt(num) > 0) {
        return true
    }
    return false
}
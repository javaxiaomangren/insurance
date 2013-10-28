<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>主页</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="description" content="">
    <meta name="author" content="">
    <meta http-equiv="Pragma" content="no-cache">
    <meta http-equiv="cache-control" content="no-cache, must-revalidate">
    <meta http-equiv="Expires" content="0">

    <!-- Le styles -->
    <link href="${rc.getContextPath()}/css/bootstrap.css" rel="stylesheet">
    <style type="text/css">
        body {
            padding-top: 60px;
            padding-bottom: 40px;
        }

        .sidebar-nav {
            padding: 9px 0;
        }

        label.error {
            padding-left: 16px;
            margin-left: 2px;
            color: red;
        }
    </style>
    <link href="${rc.getContextPath()}/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
    <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Le fav and touch icons -->
    <link rel="shortcut icon" href="${rc.getContextPath()}/js/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="144x144"
          href="${rc.getContextPath()}/js/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114"
          href="${rc.getContextPath()}/js/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72"
          href="${rc.getContextPath()}/js/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="${rc.getContextPath()}/js/apple-touch-icon-57-precomposed.png">

</head>

<body onkeydown="bindEnter(event)">

<div class="navbar navbar-fixed-top">
    <div class="navbar-inner">
        <div class="container-fluid">
            <a class="btn btn-navbar" data-toggle="collapse" data-target=".nav-collapse">
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </a>
            <a class="brand" href="#">Rules Manager Project</a>

            <div class="btn-group pull-right">
                <a class="btn dropdown-toggle" data-toggle="dropdown" href="#">
                    <i class="icon-user"></i>${(user.username)!}
                    <span class="caret"></span>
                </a>
                <ul class="dropdown-menu">
                    <li><a data-toggle="modal" data-backdrop="static" href="#pwdModal">修改密码</a></li>
                    <li class="divider"></li>
                    <li><a href="${rc.getContextPath()}/logout">注销</a></li>
                </ul>
            </div>
        </div>
    </div>
</div>
<div class="container-fluid">
    <div class="row-fluid">
        <div class="span3" style="width:150px;">
            <div class="well sidebar-nav">
                <ul class="nav nav-list">

                <#--<#if sa || user_permissions?seq_contains("user.list") || user_permissions?seq_contains("role.list")-->
                <#--|| user_permissions?seq_contains("res.list") || user_permissions?seq_contains("role_resource.list")>-->
                    <li class="nav-header">用户资源管理</li>
                    <li><a href="#">Link</a></li>
                    <li><a href="javascript:postRequest('${rc.getContextPath()}/test','testli')"/>test</li>
                <#--</#if>-->

                    <li class="nav-header">系统配置管理</li>
                    <li><a href="#">Link</a></li>
                    <li><a href="#">Link</a></li>
                    <li><a href="#">Link</a></li>



                </ul>
            </div>
            <!--/.well ?search_site=${search_site!}&search_userType=${search_userType!}&search_city=${search_city!}&search_sender=${search_sender!}&search_date=${search_date!}-->
        </div>
        <!--/span-->
        <div id="contentDiv" class="span9" style="width:82%">
            <div class="hero-unit">
                <h1>welcome</h1>
            </div>
        </div>
    </div>
    <!--/row-->

    <div class="modal hide" id="pwdModal">
        <div class="modal-header">
            <button type="button" class="close" data-dismiss="modal">×</button>
            <h3>修改密码</h3>
        </div>
        <div class="modal-body">
            <p>

            <form class="form-horizontal" id="userForm">
                <fieldset>
                    <div class="control-group">
                        <label class="control-label " for="usernamec">用户名:</label>

                        <div class="controls">
                            <input type="text" readonly="true" class="input-xlarge " id="usernamec" maxlength="20"
                                   name="usernamec" value="${(user.username)!}">
                        </div>
                    </div>
                    <div id="passdiv" class="control-group">
                        <label class="control-label" for="oldpasswordc">旧密码:</label>

                        <div class="controls">
                            <input type="password" class="input-xlarge" id="oldpasswordc" name="oldpasswordc">
                        </div>
                    </div>
                    <div id="passdiv2" class="control-group">
                        <label class="control-label" for="newpasswordc">新密码:</label>

                        <div class="controls">
                            <input type="password" class="input-xlarge" id="newpasswordc" name="newpasswordc">
                        </div>
                    </div>
                    <div id="confirmdiv" class="control-group">
                        <label class="control-label" for="confirm_passwordc">确认新密码:</label>

                        <div class="controls">
                            <input type="password" class="input-xlarge" id="confirm_passwordc" name="confirm_passwordc">
                        </div>
                    </div>
                </fieldset>
            </form>
            </p>
        </div>
        <div class="modal-footer">
            <a href="#" class="btn" data-dismiss="modal">取消</a>
            <a href="#" class="btn btn-primary" onclick="$('#userForm').submit();">保存</a>
        </div>
    </div>
    <hr>
    <footer>
        <p align="center">
            <span>&copy; Company 2012</span>
        </p>
    </footer>
</div>
<!--/.fluid-container-->

<!-- Le javascript
================================================== -->
<!-- Placed at the end of the document so the pages load faster -->
<script src="${rc.getContextPath()}/js/jquery-1.7.1.min.js"></script>
<script src="${rc.getContextPath()}/js/jquery.js"></script>
<script src="${rc.getContextPath()}/js/jquery.validate.js"></script>
<script src="${rc.getContextPath()}/js/bootstrap-transition.js"></script>
<script src="${rc.getContextPath()}/js/bootstrap-alert.js"></script>
<script src="${rc.getContextPath()}/js/bootstrap-modal.js"></script>
<script src="${rc.getContextPath()}/js/bootstrap-dropdown.js"></script>
<script src="${rc.getContextPath()}/js/bootstrap-scrollspy.js"></script>
<script src="${rc.getContextPath()}/js/bootstrap-tab.js"></script>
<script src="${rc.getContextPath()}/js/bootstrap-tooltip.js"></script>
<script src="${rc.getContextPath()}/js/bootstrap-popover.js"></script>
<script src="${rc.getContextPath()}/js/bootstrap-button.js"></script>
<script src="${rc.getContextPath()}/js/bootstrap-collapse.js"></script>
<script src="${rc.getContextPath()}/js/bootstrap-carousel.js"></script>
<script src="${rc.getContextPath()}/js/bootstrap-typeahead.js"></script>
<script src="${rc.getContextPath()}/js/WdatePicker.js"></script>
<script src="${rc.getContextPath()}/js/initCurrentDate.js"></script>

<script src="${rc.getContextPath()}/js/ajaxfileupload.js"></script>

<script src="${rc.getContextPath()}/js/uploadify/jquery.uploadify.min.js"></script>
<link href="${rc.getContextPath()}/js/uploadify/uploadify.css" rel="stylesheet">

<!--  jqChart-->
<link rel="stylesheet" type="text/css" href="${rc.getContextPath()}/css/jquery.jqChart.css"/>
<link rel="stylesheet" type="text/css" href="${rc.getContextPath()}/css/jquery.jqRangeSlider.css"/>
<script src="${rc.getContextPath()}/js/jquery.jqChart.min.js" type="text/javascript"></script>
<script src="${rc.getContextPath()}/js/jquery.jqRangeSlider.min.js" type="text/javascript"></script>
<!-- ie use-->
<script lang="javascript" type="text/javascript" src="${rc.getContextPath()}/js/excanvas.js"></script>


<script type="text/javascript">
    $(document).ready(function() {
        $("#userForm").validate({
            //验证成功
            submitHandler:function(form) {
                modifyPwd();
                $(form).ajaxSubmit();//验证全部通过调用的方法，退出验证的遍历
            },
            rules: {
                usernamec: {
                    required: true,
                    minlength: 2
                },
                oldpasswordc: {
                    required: true
                },
                newpasswordc: {
                    required: true,
                    minlength: 5
                },
                confirm_passwordc: {
                    required: true,
                    minlength: 5,
                    equalTo: "#newpasswordc"
                }
            },
            messages: {
                usernamec: {
                    required: "请输入用户名",
                    minlength: "你的用户名必须包含至少2个字符"
                },
                oldpasswordc: {
                    required: "请输入旧密码"
                },
                newpasswordc: {
                    required: "请输入新密码",
                    minlength: "你的密码必须至少5个字符长"
                },
                confirm_passwordc: {
                    required: "请输入新密码",
                    minlength: "你的密码必须至少5个字符长",
                    equalTo: "请输入与上面相同的密码"
                }
            }
        });
    });

    function modifyPwd() {
        var username = $("#usernamec").val();
        var oldpassword = $("#oldpasswordc").val();
        var newpassword = $("#newpasswordc").val();
        $.post(
                "${rc.getContextPath()}/update_password.json",
                { username : username, password : oldpassword,newPwd:newpassword },
                function(data) {
                    alert(data.msg);
                    if (data.msg == "修改密码成功") {
                        location.href = "login?reset-password";
                    }
                }, "json"
        );
    }
    function postRequest(url, liId) {
        $.ajax({type:"get",
            url: url,
            contentType:"application/x-www-form-urlencoded",
            cache:false,
            ifModified :true ,
            ajaxStart : waitingQuery,
            error: function() {
                $("#contentDiv").html("载入数据出错！");
            },
            success: function (text) {
                $("#contentDiv").empty();
                text = text.replace(/(^\s*)|(\s*$)/g, "");                              //把从freemarker得到的数据去掉前后空格
                $("#contentDiv").html(text);
                if (liId != undefined) {
                    $(".active").removeClass("active");
                    $('#' + liId).addClass("active");
                }
            }
        });
    }

    function waitingQuery() {
        var height = document.body.clientHeight;
        var word_left = document.body.clientWidth / 2 - 200;
        var _html = "<div id='loading' style='position: absolute;cursor:wait; left:190px;width:82%;height:" + height + "px;top:0;background:#E0ECFF;opacity:0.8;filter:alpha(opacity=80);'>\
         <span style='position: relative; left:" + word_left + "px;top:250px;width:180px;height:16px;padding:12px 5px 10px 30px;\
         background:#fff no-repeat scroll 5px 10px;border:2px solid #ccc;color:#000;'>\
         正在加载，请等待...\
         </span></div>";
        $("#contentDiv").append(_html);
    }

    function getPage(url, currpage) {
        url = url.replace("start=", "start=" + currpage);
        postRequest(url);
    }

    //打开新增界面
    function add(focusId, headerid, headerText, dateId) {
        $('#myModal').modal({backdrop : 'static', keyboard : false, show : true});
        $('#' + focusId).focus();
        $('#' + headerid).text(headerText);
    }

    //手动提交form,触发验证
    function save() {
        $("#editForm").submit();
    }

    function bindEnter(obj) {
        //使用document.getElementById获取到按钮对象
        var el = window.event.srcElement;
        var button = document.getElementById('gobutton');
        if (button && obj.keyCode == 13 && el.id == "pageNum") {
            button.click();
            obj.returnValue = false;
        }
    }

    function clearVal() {
        //这是啥意思
    }

    function analyticsLen(val) {
        index = val.indexOf("http://");
        if (index != -1) {
            val = val.substring(0, index);
        }
        var len = 0;
        for (var i = 0; i < val.length; i++) {
            if (val[i].match(/[^\x00-\xff]/ig) != null) { //全角
                len += 2;
            } else {
                len += 1;
            }
        }
        return len;
    }
    ;


    // 字符最大长度验证（一个中文字符长度为2）
    jQuery.validator.addMethod("analyticsLength", function(value, element, param) {
        index = value.indexOf("http://");
        if (index != -1) {
            value = value.substring(0, index);
        }
        var length = 0;
        for (var i = 0; i < value.length; i++) {
            if (value[i].match(/[^\x00-\xff]/ig) != null) { //全角
                length += 2;
            } else {
                length += 1;
            }
        }
        return this.optional(element) || (length <= param);
    }, $.validator.format("长度不能大于{0}!"));

    // 字符最大长度验证（一个中文字符长度为2）
    jQuery.validator.addMethod("picPath", function(value, element, param) {
        flag = true;
        if (value.indexOf("localhost") > -1 || value.indexOf("tuan800-inc.com") > -1) {
            flag = false;
        }
        return this.optional(element) || flag;
    }, $.validator.format("错误的图片地址,包含tuan800-inc.com等非法字符<a title='上传图片后请不要修改图片地址!!!'>[?]</a>"));
</script>
</body>
</html>
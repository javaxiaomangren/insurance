<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>登陆</title>
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
    </style>
    <style type="text/css" media="screen">
        .center {
            position: absolute;
            width: 300px;
            height: 150px;
            left: 45%;
            top: 45%;
            margin: -60px 0px 0px -60px;
            border: 0px solid #F00;
        }
    </style>
    <link href="${rc.getContextPath()}/css/bootstrap-responsive.css" rel="stylesheet">

    <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
    <!--[if lt IE 9]>
    <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
    <![endif]-->

    <!-- Le fav and touch icons -->
    <link rel="shortcut icon" href="/assets/images/favicon.ico">
    <link rel="apple-touch-icon-precomposed" sizes="144x144" href="/assets/images/apple-touch-icon-144-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="114x114" href="/assets/images/apple-touch-icon-114-precomposed.png">
    <link rel="apple-touch-icon-precomposed" sizes="72x72" href="/assets/images/apple-touch-icon-72-precomposed.png">
    <link rel="apple-touch-icon-precomposed" href="/assets/images/apple-touch-icon-57-precomposed.png">
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
        </div>
    </div>
</div>

<div class="row-fluid">
    <div class="span12">
        <div align="center" class="center">
            <span style="font-size:48px;">登录</span>
            <span style="font-size:16px;">rules manager</span>
            <br/>
            <br/>
            <br/>

            <form id="login" name="input" method="post" action="${rc.getContextPath()}/login">
                用户名:
                <input id="username" type="text" name="username" onkeydown="clearVal()" value="" autocomplete="off"/>
                <br>
                密　码:
                <input id="password" type="password" name="password" value="" autocomplete="off"/>
                <br>
                <font id="message" color="red">${msg!}</font>
                <br>
                <input type="submit" style="display:none;"/><#-- firefox兼容 -->
                <input id="loginbutton" type="button" class="btn btn-primary" onclick="validate(event)" value="登录"/>
                <input type="reset" class="btn" value="重置"/>
            </form>
        </div>
    </div>
</div>

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
<script type="text/javascript">

    $("#username").focus();

    function validate(obj) {
        var username = $("#username").val();
        var password = $("#password").val();
        if (username == "") {
            alert("用户名不能为空");
            $("#username").focus();
            obj.returnValue = false;
            return false;
        } else if (password == "") {
            alert("密码不能为空");
            $("#password").focus();
            obj.returnValue = false;
            return false;
        }
        $("#login").submit();
    }

    function clearVal() {
        $("#message").text("");
    }

    function bindEnter(obj) {
//使用document.getElementById获取到按钮对象
        var el = window.event.srcElement;
        var button = document.getElementById('loginbutton');
        if (button && obj.keyCode == 13) {
            if (el.id == "password")
                button.click();
            else if (el.id == "user")
                $("#password").focus();
            obj.returnValue = false;
        }
    }

    if ($("#contentDiv").html() != undefined) {
        window.location = "${rc.getContextPath()}/main";
    }
</script>
</body>
</html>
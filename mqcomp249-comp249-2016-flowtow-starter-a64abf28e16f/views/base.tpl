<!doctype html>
<html class="no-js">
<head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="description" content="">
    <meta name="keywords" content="">
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no">
    <title>{{title or 'No title'}}</title>

    <!-- Set render engine for 360 browser -->
    <meta name="renderer" content="webkit">
    <!-- No Baidu Siteapp-->
    <meta http-equiv="Cache-Control" content="no-siteapp"/>
    <link rel="icon" type="image/png" href="/static/i/favicon.png">
    <!-- Amaze UI CSS -->
    <link rel="stylesheet" href="/static/css/amazeui.min.css">
    <link rel="stylesheet" href="/static/css/app.min.css">

</head>
<body>
<header class="am-topbar am-topbar-fixed-top">
    <div class="am-container">
        <h1 class="am-topbar-brand">
            <a href="#">FlowTow</a>
        </h1>

        <div class="am-collapse am-topbar-collapse" id="collapse-head">
            <ul class="am-nav am-nav-pills am-topbar-nav">
                %if homeActive:
                <li class="am-active"><a href="/">Home</a></li>
                %else:
                <li><a href="/">Home</a></li>
                %end
                %if aboutActive:
                <li class="am-active"><a href="/about">About</a></li>
                %else:
                <li><a href="/about">About</a></li>
                %end
                %if userNick!=None:
                %if myActive:
                <li class="am-active"><a href="/my">My Images</a></li>
                %else:
                <li><a href="/my">My Images</a></li>
                %end
                %end
            </ul>

            %if userNick==None:
            <div class="am-topbar-right">
                <button class="am-btn am-topbar-btn am-btn-sm">
                    New?
                </button>
            </div>

            <div class="am-topbar-right">
                <form id="loginform" class="am-form-inline am-topbar-form" action="/login" method="post" role="form">
                    <div class="am-form-group">
                        <input type="text" name="nick" class="am-form-field am-input-sm" placeholder="usernick">
                    </div>

                    <div class="am-form-group">
                        <input type="password" name="password" class="am-form-field am-input-sm" placeholder="password">
                    </div>

                    <button type="submit" class="am-btn am-btn-default am-btn-sm" id="login-button">Login</button>
                </form>
            </div>
            %else:
            <div class="am-topbar-right">
                <form id="logoutform" class="am-form-inline am-topbar-form" action="/logout" method="post" role="form">
                    <label class="am-form-label">Logged in as {{userNick}}</label>
                    <input type="submit" class="am-btn am-btn-default am-btn-sm" name="logout" value="Logout"/>
                </form>
            </div>
            %end
        </div>
    </div>
</header>
{{!base}}

<!--[if lt IE 9]>
<script src="//libs.useso.com/js/jquery/1.11.1/jquery.min.js"></script>
<script src="//cdn.staticfile.org/modernizr/2.8.3/modernizr.js"></script>
<script src="/js/polyfill/rem.min.js"></script>
<script src="//libs.useso.com/js/respond.js/1.4.2/respond.min.js"></script>
<script src="//cdn.amazeui.org/amazeui/2.1.0/js/amazeui.legacy.min.js"></script>
<script src="/static/js/app.min.js"></script>
<![endif]-->

<!--[if (gte IE 9)|!(IE)]><!-->
<script src="/static/js/jquery.min.js"></script>
<script src="/static/js/amazeui.min.js"></script>
<script src="/static/js/app.min.js"></script>
<!--<![endif]-->

</body>
</html>
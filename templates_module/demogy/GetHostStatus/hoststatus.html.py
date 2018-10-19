# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1539879410.827
_enable_loop = True
_template_filename = 'C:/work/gydemo/telecom-demo/templates/GetHostStatus/hoststatus.html'
_template_uri = '/GetHostStatus/hoststatus.html'
_source_encoding = 'utf-8'
_exports = []


def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'<!DOCTYPE html>\r\n<html>\r\n\r\n<head>\r\n    <meta charset="utf-8" />\r\n    <meta http-equiv="X-UA-Compatible" content="IE=edge">\r\n    <meta name="viewport" content="width=device-width, initial-scale=1">\r\n    <title></title>\r\n    <!-- \u82e5\u60a8\u9700\u8981\u4f7f\u7528Kendo UI Professional\uff0c\u8bf7\u8054\u7cfb\u7248\u6743\u4eba\u83b7\u5f97\u5408\u6cd5\u7684\u6388\u6743\u6216\u8bb8\u53ef\u3002 -->\r\n    <!-- Bootstrap css -->\r\n    <link href="https://magicbox.bk.tencent.com/static_api/v3/assets/bootstrap-3.3.4/css/bootstrap.min.css" rel="stylesheet">\r\n    <!-- kendo ui css -->\r\n    <link href="https://magicbox.bk.tencent.com/static_api/v3/assets/kendoui-2015.2.624/styles/kendo.common.min.css" rel="stylesheet">\r\n    <link href="https://magicbox.bk.tencent.com/static_api/v3/assets/kendoui-2015.2.624/styles/kendo.default.min.css" rel="stylesheet">\r\n    <!-- font-awesome -->\r\n    <link href="https://magicbox.bk.tencent.com/static_api/v3/assets/fontawesome/css/font-awesome.css" rel="stylesheet">\r\n    <!--\u84dd\u9cb8\u63d0\u4f9b\u7684\u516c\u7528\u6837\u5f0f\u5e93 -->\r\n    <link href="https://magicbox.bk.tencent.com/static_api/v3/bk/css/bk.css" rel="stylesheet">\r\n    <link href="https://magicbox.bk.tencent.com/static_api/v3/bk/css/bk_pack.css" rel="stylesheet">\r\n    <!-- \u5982\u679c\u8981\u4f7f\u7528Bootstrap\u7684js\u63d2\u4ef6\uff0c\u5fc5\u987b\u5148\u8c03\u5165jQuery -->\r\n    <script src="https://magicbox.bk.tencent.com/static_api/v3/assets/js/jquery-1.10.2.min.js"></script>\r\n    <!-- \u5305\u62ec\u6240\u6709bootstrap\u7684js\u63d2\u4ef6\u6216\u8005\u53ef\u4ee5\u6839\u636e\u9700\u8981\u4f7f\u7528\u7684js\u63d2\u4ef6\u8c03\u7528\u3000-->\r\n    <script src="https://magicbox.bk.tencent.com/static_api/v3/assets/echarts-2.0/echarts-all.js"></script>\r\n    <script src="https://magicbox.bk.tencent.com/static_api/v3/assets/bootstrap-3.3.4/js/bootstrap.min.js"></script>\r\n    <!-- \u5305\u62ec\u6240\u6709kendoui\u7684js\u63d2\u4ef6\u6216\u8005\u53ef\u4ee5\u6839\u636e\u9700\u8981\u4f7f\u7528\u7684js\u63d2\u4ef6\u8c03\u7528\u3000-->\r\n    <script src="https://magicbox.bk.tencent.com/static_api/v3/assets/kendoui-2015.2.624/js/kendo.all.min.js"></script>\r\n    <script src="https://magicbox.bk.tencent.com/static_api/v3/assets/echarts-2.0/echarts-all.js"></script>\r\n    <script src="https://magicbox.bk.tencent.com/static_api/v3/bk/js/bk.js"></script>\r\n    <!-- \u6570\u636e\u57cb\u70b9\u7edf\u8ba1 -->\r\n    <script src="http://magicbox.bk.tencent.com/static_api/analysis.js"></script>\r\n    <!-- \u4ee5\u4e0b\u4e24\u4e2a\u63d2\u4ef6\u7528\u4e8e\u5728IE8\u4ee5\u53ca\u4ee5\u4e0b\u7248\u672c\u6d4f\u89c8\u5668\u652f\u6301HTML5\u5143\u7d20\u548c\u5a92\u4f53\u67e5\u8be2\uff0c\u5982\u679c\u4e0d\u9700\u8981\u7528\u53ef\u4ee5\u79fb\u9664 -->\r\n    <!--[if lt IE 9]><script src="https://magicbox.bk.tencent.com/static_api/v3/assets/js/html5shiv.min.js"></script><script src="https://magicbox.bk.tencent.com/static_api/v3/assets/js/respond.min.js"></script><![endif]-->\r\n</head>\r\n\r\n<body class="bg-white" data-bg-color="bg-white">\r\n    <div class="king-page-box">\r\n        <div class="king-container clearfix">\r\n            <nav class="">\r\n                <div style="overflow:hidden; z-index: inherit;" class="navbar king-horizontal-nav1  f14">\r\n                    <div class="navbar-container">\r\n                        <div class="navbar-header pull-left">\r\n                            <a class="navbar-brand" href="javascript:;">\r\n                                <img src="https://magicbox.bk.tencent.com/static_api/v3/bk/images/logo.png" class="logo"> </a>\r\n                        </div>\r\n                        <ul class="nav navbar-nav pull-left m0">\r\n                            <li ><a href="')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'GetHostStatus/">\u9996\u9875</a></li>\r\n                            <li class="active" ><a href="')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'GetHostStatus/hoststatus/">\u4e3b\u673a\u72b6\u6001</a></li>\r\n                            <li><a href="')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'GetHostStatus/history/">\u64cd\u4f5c\u8bb0\u5f55</a></li>\r\n                        </ul>\r\n                        <div class="navbar-header pull-right">\r\n                            <ul class="nav">\r\n                                <li class="user-info">\r\n                                    <a href="javascript:;">\r\n                                        <img class="img-rounded" src="https://magicbox.bk.tencent.com/static_api/v3/components/horizontal_nav1/images/avatar.png">\r\n                                        <span>admin</span>\r\n                                    </a>\r\n                                </li>\r\n                            </ul>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </nav>\r\n<form class="form-horizontal">\r\n                <div class="king-block-header king-info">\r\n                    <ul class="king-block-options">\r\n                        <li>\r\n                            <!-- <button type="button"><i class="fa fa-cog"></i></button> -->\r\n                        </li>\r\n                    </ul>\r\n                    <h3 class="king-block-title"> </h3>\r\n                </div>\r\n                <div class="form-group clearfix ">\r\n                    <label class="col-sm-3 control-label bk-lh30 pt0">\u4e1a\u52a1\uff1a</label>\r\n                    <div class="col-sm-9">\r\n                        <select name="" id="biz_id" class="form-control bk-valign-top">\r\n\r\n                        </select>\r\n                    </div>\r\n                </div>\r\n                <div class="form-group clearfix ">\r\n                    <label class="col-sm-3 control-label bk-lh30 pt0">IP\u5730\u5740\uff1a</label>\r\n                    <div class="col-sm-9">\r\n                        <select name="" id="ip" class="form-control bk-valign-top">\r\n                        </select>\r\n                    </div>\r\n                </div>\r\n                <div class="form-group clearfix">\r\n                    <div class="col-sm-9 col-sm-offset-3">\r\n                        <button type="button" class="king-btn mr10  king-success" onclick="refresh_chart(this)">\u63d0\u4ea4</button>\r\n                        <button type="button" class="king-btn king-default ">\u53d6\u6d88</button>\r\n                    </div>\r\n                </div>\r\n                                    <!-- \u4e0b\u62c9\u6846\u6a21\u677f -->\r\n                    <template id="app_tpl">\r\n                        <option value="#id#">#name#</option>\r\n                    </template>\r\n\r\n                    <template id="ip_tpl">\r\n                        <option value="#ip#">#ip#</option>\r\n                    </template>\r\n\r\n            </form>\r\n\r\n            <div class="king-block king-block-bordered king-block-themed mb0">\r\n                <div class="king-block-header king-info">\r\n                    <ul class="king-block-options">\r\n                        <li>\r\n                            <!-- <button type="button"><i class="fa fa-cog"></i></button> -->\r\n                        </li>\r\n                    </ul>\r\n                    <h3 class="king-block-title">\u4e3b\u673acpu\u3001\u5185\u5b58\u3001\u786c\u76d8\u4f7f\u7528\u8d8b\u52bf</h3>\r\n                </div>\r\n                <div class="king-block-content">\r\n                    <div style="height: 300px; -webkit-tap-highlight-color: transparent; user-select: none; cursor: pointer; background-color: rgba(0, 0, 0, 0);" id="chart_1538111754001" class="king-chart-box chart-area " _echarts_instance_="1538111661125"></div>\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n    <script>\r\n           function renderTpl(str, cfg) {\r\n            var re = /(#(.+?)#)/g;\r\n\r\n            return str.replace(re, function() {\r\n                var val = cfg[arguments[2]]+\'\';\r\n                if(typeof val == \'undefined\') {\r\n                    val = \'\';\r\n                }\r\n                return val;\r\n            });\r\n        }\r\n\r\n    /*\r\n    * \u67e5\u8be2\u8868\u5355\u7ea7\u8054\u6570\u636e\u62c9\u53d6\r\n    */\r\n    function select_ip(biz_id){\r\n        //\u7ea7\u8054\u9009\u62e9ip\r\n        $(\'#ip\').html(\'\');\r\n        $.get(\'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'GetHostStatus/get_ip_by_bizid/\', {\'biz_id\': biz_id}, function(data){\r\n                if(data.result){\r\n                    var _html = \'\';\r\n                    var list = data.data;\r\n                    var tpl = $(\'#ip_tpl\').html();\r\n                    for (var i=0,len=list.length; i < len; i++){\r\n                        var item = list[i];\r\n                        _html += renderTpl(tpl, item)\r\n                    }\r\n                    $(\'#ip\').html(_html);\r\n                }else{\r\n                    alert("\u83b7\u53d6\u5931\u8d25")\r\n                }\r\n            }, \'json\')\r\n        }\r\n\r\n        $(function(){\r\n        /*\r\n        * \u67e5\u8be2\u8868\u5355\u7ea7\u8054\u6570\u636e\u62c9\u53d6\r\n        */\r\n        $.get(\'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'GetHostStatus/get_biz_list/\', function(data){\r\n                if(data.result){\r\n                    var _html = \'\';\r\n                    var list = data.data;\r\n                    var tpl = $(\'#app_tpl\').html();\r\n                    for (var i=0,len=list.length; i < len; i++){\r\n                        var item = list[i];\r\n                        _html += renderTpl(tpl, item)\r\n                    }\r\n                    $(\'#biz_id\').html(_html);\r\n\r\n                    var biz_id = $("#biz_id").val();\r\n                    select_ip(biz_id);\r\n                }else{\r\n                    alert("\u83b7\u53d6\u5931\u8d25")\r\n                }\r\n            }, \'json\')\r\n\r\n        //\u4e1a\u52a1\u9009\u62e9\u4e0b\u62c9\u7ed1\u5b9achange\u4e8b\u4ef6\r\n        $("#biz_id").change(function(){\r\n            var biz_id = $("#biz_id").val();\r\n            console.log(biz_id)\r\n            select_ip(biz_id);\r\n        });\r\n    });\r\n\r\n\r\n\r\n\r\n        function createEStandLineChart(conf){    \r\n            var myChart = echarts.init(document.getElementById(conf.selector));\r\n            var legendData = []\r\n            for(var i=0; i < conf.data.series.length;i++){\r\n                legendData.push(conf.data.series[i].name)\r\n            }\r\n            myChart.setOption({\r\n                tooltip : {\r\n                    trigger: \'axis\'\r\n                },\r\n                legend: {\r\n                    y: \'bottom\',\r\n                    data:legendData\r\n                },\r\n                toolbox: {\r\n                    show : true,\r\n                    feature : {\r\n                        mark : {show: true},\r\n                        dataView : {show: true, readOnly: false},\r\n                        magicType : {show: true, type: [\'bar\',\'line\']},\r\n                        restore : {show: true},\r\n                        saveAsImage : {show: true}\r\n                    }\r\n                },\r\n                calculable : true,\r\n                xAxis : [\r\n                    {\r\n                        type : \'category\',\r\n                        data : conf.data.xAxis\r\n                    }\r\n                ],\r\n                yAxis : [\r\n                    {\r\n                        type : \'value\',\r\n                        splitArea : {show : true}\r\n                    }\r\n                ],\r\n                series : conf.data.series\r\n            });\r\n         }\r\n        function initEStandLineChart(conf){\r\n            $.ajax({\r\n                url: conf.url,\r\n                type: \'GET\',\r\n                data: {\'biz_id\': conf.biz_id,  \'ip\': conf.ip},\r\n                dataType: conf.dataType,\r\n                success: function(res){\r\n                    //\u83b7\u53d6\u6570\u636e\u6210\u529f\r\n                    if (res.result){\r\n                        createEStandLineChart({\r\n                            selector: conf.containerId, // \u56fe\u8868\u5bb9\u5668\r\n                            data: res.data, // \u56fe\u8868\u6570\u636e\r\n                        });\r\n                    }\r\n                }\r\n            })\r\n        }\r\n    </script>\r\n    <script>\r\n        $(function(){\r\n             var biz_id = $(\'#biz_id\').val();\r\n             var ip = $(\'#ip\').val();\r\n\r\n            initEStandLineChart({\r\n                url:\'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u"GetHostStatus/get_cpu_chartdata/',\r\n                dataType: 'json',\r\n                containerId: 'biz_id:biz_id,\\n' +\r\n                    '                 ip:ip,',\r\n                biz_id:biz_id,\r\n                ip:ip,\r\n            });   \r\n        });\r\n\r\n         function refresh_chart(obj){\r\n             var biz_id = $('#biz_id').val();\r\n             var ip = $('#ip').val();\r\n             initEStandLineChart({\r\n                 url: '")
        __M_writer(unicode(SITE_URL))
        __M_writer(u"GetHostStatus/get_cpu_chartdata/',\r\n                 dataType: 'json',\r\n                 containerId: 'chart_1538111754001',\r\n                 biz_id:biz_id,\r\n                 ip:ip,\r\n        });\r\n    }\r\n\r\n\r\n    </script>\r\n</body>\r\n\r\n</html>")
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"32": 158, "33": 251, "34": 251, "35": 264, "36": 264, "42": 36, "16": 0, "22": 1, "23": 46, "24": 46, "25": 47, "26": 47, "27": 48, "28": 48, "29": 138, "30": 138, "31": 158}, "uri": "/GetHostStatus/hoststatus.html", "filename": "C:/work/gydemo/telecom-demo/templates/GetHostStatus/hoststatus.html"}
__M_END_METADATA
"""

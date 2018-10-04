# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1538663175.182
_enable_loop = True
_template_filename = 'C:/work/gydemo/telecom-demo/templates/GetHostStatus/home.html'
_template_uri = '/GetHostStatus/home.html'
_source_encoding = 'utf-8'
_exports = [u'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, u'/base.html', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        SITE_URL = context.get('SITE_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer(u'\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer(u"\r\n    <script>\r\n    function renderTpl(str, cfg) {\r\n            var re = /(#(.+?)#)/g;\r\n\r\n            return str.replace(re, function() {\r\n                var val = cfg[arguments[2]]+'';\r\n                if(typeof val == 'undefined') {\r\n                    val = '';\r\n                }\r\n                return val;\r\n            });\r\n        }\r\n\r\n    /*\r\n    * \u67e5\u8be2\u8868\u5355\u7ea7\u8054\u6570\u636e\u62c9\u53d6\r\n    */\r\n    function select_ip(biz_id){\r\n        //\u7ea7\u8054\u9009\u62e9ip\r\n        $('#ip').html('');\r\n        $.get('")
        __M_writer(unicode(SITE_URL))
        __M_writer(u'GetHostStatus/get_ip_by_bizid/\', {\'biz_id\': biz_id}, function(data){\r\n                if(data.result){\r\n                    var _html = \'\';\r\n                    var list = data.data;\r\n                    var tpl = $(\'#ip_tpl\').html();\r\n                    for (var i=0,len=list.length; i < len; i++){\r\n                        var item = list[i];\r\n                        _html += renderTpl(tpl, item)\r\n                    }\r\n                    $(\'#ip\').html(_html);\r\n                }else{\r\n                    alert("\u83b7\u53d6\u5931\u8d25")\r\n                }\r\n            }, \'json\')\r\n        }\r\n\r\n        $(function(){\r\n        /*\r\n        * \u67e5\u8be2\u8868\u5355\u7ea7\u8054\u6570\u636e\u62c9\u53d6\r\n        */\r\n        $.get(\'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'GetHostStatus/get_biz_list/\', function(data){\r\n                if(data.result){\r\n                    var _html = \'\';\r\n                    var list = data.data;\r\n                    var tpl = $(\'#app_tpl\').html();\r\n                    for (var i=0,len=list.length; i < len; i++){\r\n                        var item = list[i];\r\n                        _html += renderTpl(tpl, item)\r\n                    }\r\n                    $(\'#biz_id\').html(_html);\r\n\r\n                    var biz_id = $("#biz_id").val();\r\n                    select_ip(biz_id);\r\n                }else{\r\n                    alert("\u83b7\u53d6\u5931\u8d25")\r\n                }\r\n            }, \'json\')\r\n\r\n        //\u4e1a\u52a1\u9009\u62e9\u4e0b\u62c9\u7ed1\u5b9achange\u4e8b\u4ef6\r\n        $("#biz_id").change(function(){\r\n            var biz_id = $("#biz_id").val();\r\n            console.log(biz_id)\r\n            select_ip(biz_id);\r\n        });\r\n    });\r\n\r\n\r\n    /*\r\n    * \u8868\u5355\u67e5\u8be2\u4e8b\u4ef6\u63d0\u4ea4\uff0c\u83b7\u53d6\u4f5c\u4e1a\u6267\u884c\u7ed3\u679c\r\n    */\r\n    function search(obj){\r\n        var biz_id = $(\'#biz_id\').val();\r\n        var ip = $(\'#ip\').val();\r\n        $.post(\'')
        __M_writer(unicode(SITE_URL))
        __M_writer(u'GetHostStatus/get_host/\', {\'biz_id\': biz_id, \'ip\': ip}, function(data){\r\n                /*console.log(data);*/\r\n                if(data.result){\r\n                    var list=data.data;\r\n\r\n                    var _html = \' \';\r\n                    var tpl = $(\'#tpl_15381116261452\').html();\r\n                    for (var i=0,len=list.length; i < len; i++){\r\n                        var item = list[i];\r\n                        _html += renderTpl(tpl, item);\r\n\r\n                    }\r\n\r\n\r\n                }else{\r\n                    alert("\u83b7\u53d6\u5931\u8d25")\r\n                }\r\n                $(\'#tbody15381116261452\').html(_html);\r\n            });\r\n    }\r\n\r\n\r\n\r\n    </script>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer(u'\r\n    <div class="king-page-box">\r\n        <div class="king-container clearfix">\r\n            <nav class="">\r\n                <div style="overflow:hidden; z-index: inherit;" class="navbar king-horizontal-nav1  f14">\r\n                    <div class="navbar-container">\r\n                        <div class="navbar-header pull-left">\r\n                            <a class="navbar-brand" href="javascript:;">\r\n                                <img src="https://magicbox.bk.tencent.com/static_api/v3/bk/images/logo.png" class="logo"> </a>\r\n                        </div>\r\n                        <ul class="nav navbar-nav pull-left m0">\r\n                            <li class="active"><a href="javascript:void(0);">\u9996\u9875</a></li>\r\n                            <li><a href="javascript:void(0);">\u4e3b\u673a\u72b6\u6001</a></li>\r\n                            <li><a href="javascript:void(0);">\u64cd\u4f5c\u8bb0\u5f55</a></li>\r\n                        </ul>\r\n                        <div class="navbar-header pull-right">\r\n                            <ul class="nav">\r\n                                <li class="user-info">\r\n                                    <a href="javascript:;">\r\n                                        <img class="img-rounded" src="https://magicbox.bk.tencent.com/static_api/v3/components/horizontal_nav1/images/avatar.png">\r\n                                        <span>admin</span>\r\n                                    </a>\r\n                                </li>\r\n                            </ul>\r\n                        </div>\r\n                    </div>\r\n                </div>\r\n            </nav>\r\n            <form class="form-horizontal">\r\n                <div class="king-block-header king-info">\r\n                    <ul class="king-block-options">\r\n                        <li>\r\n                            <!-- <button type="button"><i class="fa fa-cog"></i></button> -->\r\n                        </li>\r\n                    </ul>\r\n                    <h3 class="king-block-title"> </h3>\r\n                </div>\r\n                <div class="form-group clearfix ">\r\n                    <label class="col-sm-3 control-label bk-lh30 pt0">\u4e1a\u52a1\uff1a</label>\r\n                    <div class="col-sm-9">\r\n                        <select name="" id="biz_id" class="form-control bk-valign-top">\r\n\r\n                        </select>\r\n                    </div>\r\n                </div>\r\n                <div class="form-group clearfix ">\r\n                    <label class="col-sm-3 control-label bk-lh30 pt0">IP\u5730\u5740\uff1a</label>\r\n                    <div class="col-sm-9">\r\n                        <select name="" id="ip" class="form-control bk-valign-top">\r\n\r\n                        </select>\r\n                    </div>\r\n                </div>\r\n                <div class="form-group clearfix">\r\n                    <div class="col-sm-9 col-sm-offset-3">\r\n                        <button type="button" class="king-btn mr10  king-success" onclick="search(this)">\u63d0\u4ea4</button>\r\n                        <button type="button" class="king-btn king-default ">\u53d6\u6d88</button>\r\n                    </div>\r\n                </div>\r\n            </form>\r\n            <div class="king-block king-block-bordered king-block-themed mb0">\r\n                <div class="king-block-header king-info">\r\n                    <ul class="king-block-options">\r\n                        <li>\r\n                            <!-- <button type="button"><i class="fa fa-cog"></i></button> -->\r\n                        </li>\r\n                    </ul>\r\n                    <h3 class="king-block-title">\u67e5\u8be2\u7ed3\u679c</h3>\r\n                </div>\r\n                <div class="king-block-content">\r\n                    <table class="table mb0 pr15 ranger-box2  ">\r\n                        <thead>\r\n                            <tr>\r\n                                <th style="width: 70px;">#</th>\r\n                                <th style="width: 15%;">IP</th>\r\n                                <th style="width: 15%;">Mem/Disk/CPU</th>\r\n                                <th style="width: 15%;">\u6700\u540e\u5de1\u68c0\u65f6\u95f4</th>\r\n                                <th style="width: 15%;">\u5927\u533a</th>\r\n                                <th style="width: 15%;">\u6a21\u5757</th>\r\n                                <th style="width: 15%;">\u4e91\u533a\u57df</th>\r\n                                <th style="width: 10%;">\u7cfb\u7edf\u7c7b\u578b</th>\r\n                                <th>\u64cd\u4f5c</th>\r\n                            </tr>\r\n                        </thead>\r\n                        <tbody id="tbody15381116261452">\r\n                            <tr>\r\n                                <th style="width: 70px;">#</th>\r\n                                <th style="width: 15%;">IP</th>\r\n                                <th style="width: 15%;">Mem/Disk/CPU</th>\r\n                                <th style="width: 15%;">\u6700\u540e\u5de1\u68c0\u65f6\u95f4</th>\r\n                                <th style="width: 10%;">\u5927\u533a</th>\r\n                                <th style="width: 10%;">\u6a21\u5757</th>\r\n                                <th style="width: 10%;">\u4e91\u533a\u57df</th>\r\n                                <th style="width: 10%;">\u7cfb\u7edf\u7c7b\u578b</th>\r\n                                <th>\u64cd\u4f5c</th>\r\n\r\n                            </tr>\r\n\r\n\r\n                        </tbody>\r\n                    </table>\r\n                    <template id="header_tpl_15381116261452">\r\n                        <tr>\r\n                            <th style="width: 70px;">#Hostid#</th>\r\n                            <th style="width: 15%;">#innerip#</th>\r\n                            <th style="width: 15%;">#cpu#</th>\r\n                            <th style="width: 15%;">#date#</th>\r\n                            <th style="width: 15%;">#setname#</th>\r\n                            <th style="width: 15%;">#modulename#</th>\r\n                            <th style="width: 15%;">#setname#</th>\r\n                            <th style="width: 15%;">#region#</th>\r\n                            <th style="width: 15%;">#ostype#</th>\r\n                            <th>\u64cd\u4f5c</th>\r\n                        </tr>\r\n                    </template>\r\n                    <template id="tpl_15381116261452">\r\n                        <tr>\r\n                            <td style="width: 70px;">#host_id#</td>\r\n                            <td style="width: 15%;">#host_innerip#</td>\r\n                            <td style="width: 15%;">#cpu#</td>\r\n                            <td style="width: 15%;">#date#</td>\r\n                            <td style="width: 10%;">#setname#</td>\r\n                            <td style="width: 10%;">#modulename#</td>\r\n                            <td style="width: 10%;">#region#</td>\r\n                            <td style="width: 15%;">#osname#</td>\r\n                            <td>\r\n                                <button class="btn btn-xs btn-success"> <i class="glyphicon glyphicon-ok"></i> </button>\r\n                                <button class="btn btn-xs btn-warning"> <i class="glyphicon glyphicon-edit"></i> </button>\r\n                                <button class="btn btn-xs btn-danger"> <i class="glyphicon glyphicon-remove"></i> </button>\r\n                            </td>\r\n                        </tr>\r\n                    </template>\r\n                                <!-- \u4e0b\u62c9\u6846\u6a21\u677f -->\r\n                    <template id="app_tpl">\r\n                        <option value="#id#">#name#</option>\r\n                    </template>\r\n\r\n                    <template id="ip_tpl">\r\n                        <option value="#ip#">#ip#</option>\r\n                    </template>\r\n\r\n\r\n                    <!-- \u8bbe\u7f6e\u9762\u677fEnd -->\r\n                </div>\r\n            </div>\r\n        </div>\r\n    </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "utf-8", "line_map": {"64": 58, "35": 1, "40": 149, "41": 169, "42": 169, "43": 189, "44": 189, "45": 222, "46": 222, "52": 2, "58": 2, "27": 0}, "uri": "/GetHostStatus/home.html", "filename": "C:/work/gydemo/telecom-demo/templates/GetHostStatus/home.html"}
__M_END_METADATA
"""

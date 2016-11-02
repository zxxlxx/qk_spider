function keyOut(e, id) {
    var theEvent = window.event || e;
    var code = theEvent.keyCode || theEvent.which;
    if (code == 13) {  //回车键的键值为13
        document.getElementById(id).click();
    }
}
function changeUser() {
    window.location.reload()
}
$(function () {

    function isNull(value) {
        value = value ? value : "无";
        return value;
    }

    $(".customerBtn").click(function () {
        var reg = /^[\u4e00-\u9fa5]{2,9}$/;
        if (reg.test($(".customer").val())) {
            $(".messageName").html(" ");
            $(".idNumberDiv").slideDown(200);
            $(".hideName").hide();
            var customerName = $(".customer").val();
            $(".showName").append("<img style='width:60px;height:60px' src='static/img/user.png'>&nbsp;&nbsp;&nbsp;<span style=\" vertical-align: bottom;font-size:30px;font-family:'楷体';color:#666\">" + customerName + "</span><a class='clickChangeUser' onclick='changeUser()'>点击切换用户</a>");
            $(".idNumber").focus();
        } else {
            $(".messageName").html("姓名输入格式不正确！").css("color", "#e4393c");
        }
    });


    $(".idNumberBtn").click(function () {
        var data = $("#bigData").serialize()

        $(".showImg").html("<img src='static/img/loading.gif'> ");
        $.get('/api/v1.0/data?', data, function (data) {
            $(".messageIdnumber").html(" ");
            $(".hideIdnumber").hide()
            $(".showIdnumber").append("<div style='text-align:right;float:left;width:60px;height:60px;font-size:20px;color:#666;margin-top: -3px '><i class='fa fa-credit-card'></i></div>&nbsp;&nbsp;&nbsp;<span style='font-size:18px;color:#888'>" + $("#idNumber").val() + "</span>");

            if (data.pengyuan != null || data.zzc) {
                $(".showImg").hide();
                if (data.pengyuan) {
                    $(".dataShowPY").show();
                    var arrValue = [];
                    var data = data.pengyuan;
                    for (var t = 0; t < data.length; t++) {
                        if (data[t]) {
                            var cisReports = data[t].cisReports
                            //查询批次号
                            var batNo = cisReports.batNo;
                            arrValue.push(batNo);
                            //查询操作员登录名
                            var queryUserID = cisReports.queryUserID;
                            arrValue.push(queryUserID);
                            //查询请求数量
                            var queryCount = cisReports.queryCount;
                            arrValue.push(queryCount);
                            //分支机构名称
                            var subOrgan = cisReports.subOrgan;
                            arrValue.push(subOrgan);
                            //查询单位名称
                            var unitName = cisReports.unitName;
                            arrValue.push(unitName);
                            //查询申请时间,格式YYYYMMDD HH24:mm:ss
                            var receiveTime = cisReports.receiveTime;
                            arrValue.push(receiveTime);
                            var arrName = ["查询批次号", "查询操作员登录名", "查询请求数量", "分支机构名称", "查询单位名称", "查询申请时间"];
                            var htmlCisReports = "";
                            for (var i = 0; i < arrValue.length; i++) {
                                htmlCisReports += "<tr><td style='width:40%'>" + arrName[i] + "</td><td style='width:60%'>" + arrValue[i] + "</td></tr>";
                            }
                            //报告信息
                            // $("#cisReports").append(htmlCisReports);

                            //子报告
                            var cisReport = cisReports.cisReport;
                            var subArrValue = [];
                            //报告编号

                            //有否系统错误，true：有错误，false：无错误
                            var hasSystemError = cisReport.hasSystemError;
                            hasSystemError = hasSystemError ? "有错误" : "无错误";
                            subArrValue.push(hasSystemError);
                            //该客户是否被冻结，true：被冻结，false：未被冻结
                            var isFrozen = cisReport.isFrozen;
                            isFrozen = isFrozen ? "被冻结" : "未被冻结";
                            subArrValue.push(isFrozen);
                            var subArrName = ["有否系统错误", "该客户是否被冻结"];
                            var htmlCisReport = "";
                            for (var i = 0; i < subArrValue.length; i++) {
                                htmlCisReport += "<tr><td style='width:40%'>" + subArrName[i] + "</td><td style='width:60%'>" + subArrValue[i] + "</td></tr>";
                            }
                            //子报告信息
                            $("#cisReport").empty()
                            $("#cisReport").append(htmlCisReport);

                            <!-- 查询条件信息 1..1 -->
                            var item = cisReport.queryConditions.item;
                            //被查询者姓名
                            var name = item[0].name;
                            var caption = item[0].caption;
                            var value = item[0].value;
                            //被查询者证件号码
                            var nameID = item[1].name;
                            var captionID = item[1].caption;
                            var valueID = item[1].value;
                            <!-- 个人风险统计信息 0..1 -->
                            var personRiskStatInfo = cisReport.personRiskStatInfo;
                            if (personRiskStatInfo) {
                                var pinfoArrValue = [];
                                var pinfoArrName = ["个人风险统计信息收费子报告ID", "子报告查询状态", "错误描述信息"];
                                var htmlpinfo = "";
                                for (var i = 0; i < pinfoArrValue.length; i++) {
                                    htmlpinfo += "<tr><td style='width:40%'>" + pinfoArrName[i] + "</td><td style='width:60%'>" + pinfoArrValue[i] + "</td></tr>";
                                }
                            }

                            //子报告信息
                            // $("#personRiskStatInfo").append(htmlpinfo);
                            <!-- 个人身份认证信息 0..1 -->


                            if (cisReport.policeCheck2Info) {
                                var policeCheck2Info = cisReport.policeCheck2Info;
                                var InfoArrValue = [];
                                //详细信息
                                var item = policeCheck2Info.item;
                                //姓名
                                var nameItem = item.name;
                                InfoArrValue.push(nameItem);
                                //证件号码
                                var documentNoItem = item.documentNo;
                                InfoArrValue.push(documentNoItem);
                                //认证结果ID,1:姓名和公民身份号码一致。2：公民身份号码一致，姓名不一致。3：库中无此号，请到户籍所在地进行核实。
                                var resultItem = parseInt(item.result);
                                switch (resultItem) {
                                    case 1 :
                                        resultItem = "<span style='color:#5CB85C'><i class='fa fa-check'></i>&nbsp;姓名和公民身份号码一致</span>";
                                        break;
                                    case 2 :
                                        resultItem = "<span style='color:#FF6600'><i class='fa fa-warning'></i>&nbsp;公民身份号码一致，姓名不一致</span>";
                                        break;
                                    case 3 :
                                        resultItem = "<span style='color:#D8B303'><i class='fa fa-bolt'></i>&nbsp;库中无此号，请到户籍所在地进行核实</span>";
                                        break;
                                }
                                $(".showIdnumber").append("<span style='color:#32c5d2;margin-left: 20px'>" + resultItem + "</span>");
                                var infoArrName = ["姓名", "证件号码", "个人身份认证信息收费子报告ID", "个人身份认证信息子报告查询状态", "错误描述信息"];
                                var htmlInfo = "";
                                for (var i = 0; i < InfoArrValue.length; i++) {
                                    htmlInfo += "<tr><td style='width:40%'>" + infoArrName[i] + "</td><td style='width:60%'>" + InfoArrValue[i] + "</td></tr>";
                                }
                                //子报告信息
                                $("#policeCheck2Info").append(htmlInfo);


                                var photoItem = item.photo;
                                if (photoItem) {

                                    var html = '<image src="data:image/png;base64,' + photoItem + '">'
                                    $("#policeCheck2Info").after(html);
                                }


                            }


                        }
                    }
                }
                if (data.zzc) {
                    var parentriskLevel = $("#riskLevel");
                    var htmlriskLevel = "";
                    var parentreasonCode = $("#reasonCode");
                    var htmlreasonCode = "";
                    var parenthittedRules = $("#hittedRules");
                    var htmlhittedRules = "";
                    var data = data.zzc
                    $(".showData").slideDown(500);
                    $.each(data, function (name, value) {
                        if (name == "blacklist") {
                            $(".num1").html(value.count ? value.count : 0);
                            $(".num2").html(value.tenant_count ? value.tenant_count : 0);
                        } else if (name == "rule_result") {
                            //反欺诈结果显示
                            var riskLevel = value.risk_level;
                            var riskLevelText = "<span style='color:#5CB85C'><i class='fa fa-check'></i>&nbsp;低风险</span>";
                            switch (riskLevel) {
                                case "high" :
                                    riskLevelText = "<span style='color:#FF6600'><i class='fa fa-warning'></i>&nbsp;高风险</span>";
                                    break;
                                case "medium" :
                                    riskLevelText = "<span style='color:#D8B303'><i class='fa fa-bolt'></i>&nbsp;中度风险</span>";
                                    break;
                            }
                            htmlriskLevel += "<tr><td>" + riskLevelText + "</td></tr>";
                            parentriskLevel.append(htmlriskLevel);
                            console.log(htmlriskLevel)
                            //规则击中条件说明
                            var reasonCode = value.reason_code;
                            var lenreasonCode = reasonCode.length;
                            if (lenreasonCode > 0) {
                                for (var i = 0; i < lenreasonCode; i++) {
                                    htmlreasonCode += "<tr><td>" + reasonCode[i] + "</td></tr>";
                                }
                            } else {
                                htmlreasonCode += "<tr><td style='text-align: center'>表中没有可显示的数据</td></tr>";
                            }

                            parentreasonCode.append(htmlreasonCode);

                            //规则的威胁等级
                            var hittedRules = value.hitted_rules;
                            var len = hittedRules.length;
                            if (len > 0) {
                                for (var i = 0; i < hittedRules.length; i++) {
                                    var riskLevelTextT = "<span style='color:#5CB85C'><i class='fa fa-check'></i>&nbsp;低</span>";
                                    var riskLevelT = hittedRules[i].risk_level;
                                    switch (riskLevelT) {
                                        case "H" :
                                            riskLevelTextT = "<span style='color:#FF6600'><i class='fa fa-warning'></i>&nbsp;高</span>";
                                            break;
                                        case "M" :
                                            riskLevelTextT = "<span style='color:#D8B303'><i class='fa fa-bolt'></i>&nbsp;中</span>";
                                            break;
                                    }
                                    htmlhittedRules += "<tr><td>" + hittedRules[i].description + "</td><td>" + hittedRules[i].rule_type + "</td><td>" + riskLevelTextT + "</td></tr>";
                                }
                            } else {
                                htmlhittedRules += "<tr><td colspan='3' style='text-align: center'>表中没有可显示的数据</td></tr>";
                            }
                            parenthittedRules.append(htmlhittedRules);

                        }
                    });

                }
                $(".telDiv").slideDown(200);
                $(".tel").focus();
            }
            else {
                $(".showImg").hide();
                //$(".showError").html("<h4>查询数量已达上限，请联系您的客户经理。</h4>");
                $(".telDiv").slideDown(200);
            }

        });
    });
    $(".telBtn").click(function () {
        var parentriskLevel = $("#riskLevel");
        var htmlriskLevel = "";
        var parentreasonCode = $("#reasonCode");
        var htmlreasonCode = "";
        var parenthittedRules = $("#hittedRules");
        var htmlhittedRules = "";
        var regTel = /^1(3|4|5|7|8)\d{9}$/;
        if (regTel.test($(".tel").val())) {
            $(".messageTel").html(" ");
            $(".hideTel").hide();
            var tel = $(".tel").val();
            $(".showTel").append("<div style='text-align:right;float:left;width:60px;height:60px;font-size:25px;color:#666;margin-top: -7px '><i class='fa fa-mobile'></i></div>&nbsp;&nbsp;&nbsp;<span style='font-size:18px;color:#888'>" + tel + "</span>");
            $(".showImg").show().html("<img src='static/img/loading.gif'> ");
            var data = {
                user_name_cn: $.trim($("#customerBtn").val()),
                personal_id: $.trim($("#idNumberBtn").val()),
                mobile_num: $.trim($("#telBtn").val())
            }
            $.ajax({
                type: "get",
                url: "/api/v1.0/data?",
                data: $("#bigData").serializeArray(),
                success: function (result) {
                    $(".showImg").hide();
                    $(".showData").slideDown(500);
                    var data = result.zzc;
                    $.each(data, function (name, value) {
                        if (name == "blacklist") {
                            $(".num1").html(value.count ? value.count : 0);
                            $(".num2").html(value.tenant_count ? value.tenant_count : 0);
                        } else if (name == "rule_result") {
                            //反欺诈结果显示
                            var riskLevel = value.risk_level;
                            var riskLevelText = "<span style='color:#5CB85C'><i class='fa fa-check'></i>&nbsp;低风险</span>";
                            switch (riskLevel) {
                                case "high" :
                                    riskLevelText = "<span style='color:#FF6600'><i class='fa fa-warning'></i>&nbsp;高风险</span>";
                                    break;
                                case "medium" :
                                    riskLevelText = "<span style='color:#D8B303'><i class='fa fa-bolt'></i>&nbsp;中度风险</span>";
                                    break;
                            }
                            htmlriskLevel += "<tr><td>" + riskLevelText + "</td></tr>";
                            parentriskLevel.append(htmlriskLevel);


                            //规则击中条件说明
                            var reasonCode = value.reason_code;
                            var lenreasonCode = reasonCode.length;
                            if (lenreasonCode > 0) {
                                for (var i = 0; i < lenreasonCode; i++) {
                                    htmlreasonCode += "<tr><td>" + reasonCode[i] + "</td></tr>";
                                }
                            } else {
                                htmlreasonCode += "<tr><td style='text-align: center'>表中没有可显示的数据</td></tr>";
                            }

                            parentreasonCode.append(htmlreasonCode);

                            //规则的威胁等级
                            var hittedRules = value.hitted_rules;
                            var len = hittedRules.length;
                            if (len > 0) {
                                for (var i = 0; i < hittedRules.length; i++) {
                                    var riskLevelTextT = "<span style='color:#5CB85C'><i class='fa fa-check'></i>&nbsp;低</span>";
                                    var riskLevelT = hittedRules[i].risk_level;
                                    switch (riskLevelT) {
                                        case "H" :
                                            riskLevelTextT = "<span style='color:#FF6600'><i class='fa fa-warning'></i>&nbsp;高</span>";
                                            break;
                                        case "M" :
                                            riskLevelTextT = "<span style='color:#D8B303'><i class='fa fa-bolt'></i>&nbsp;中</span>";
                                            break;
                                    }
                                    htmlhittedRules += "<tr><td>" + hittedRules[i].description + "</td><td>" + hittedRules[i].rule_type + "</td><td>" + riskLevelTextT + "</td></tr>";
                                }
                            } else {
                                htmlhittedRules += "<tr><td colspan='3' style='text-align: center'>表中没有可显示的数据</td></tr>";
                            }
                            parenthittedRules.append(htmlhittedRules);
                        }
                    });

                },
                error: function () {
                    $(".showImg").html("输入姓名有误或连接超时！")
                }
            })
        } else {
            $(".messageTel").html("手机号码输入格式不正确！").css("color", "#e4393c");
        }
    });

})


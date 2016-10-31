# -*- coding: utf-8 -*-
import xmltodict
import json
from lxml import etree
import sys
import os
import io
sys.path.append("..")
from ..utils.tools import convert_dict
xmlStr = """
<?xml version="1.0" encoding="GBK"?>
<cisReports receiveTime="查询申请时间,格式YYYYMMDD HH24:mm:ss" queryCount="查询请求数量" queryUserID="查询操作员登录名" subOrgan="分支机构名称" unitName="查询单位名称" batNo="查询批次号">
<!-- 以下为每个查询申请的查询结果 1..n -->
<cisReport isFrozen="该客户是否被冻结，true：被冻结，false：未被冻结" hasSystemError="有否系统错误，true：有错误，false：无错误" refID="引用ID,为查询申请条件中的引用ID" treatResult="对应的收费子报告收费次数,与subReportTypes一一对应,为大于等于0的值的集合,用逗号分隔" subReportTypes="查询的收费子报告ID,多个收费子报告ID用逗号分隔" queryReasonID="查询原因ID，详见数据字典" buildEndTime="报告生成结束时间,格式YYYYMMDD HH24:mm:ss" reportID="报告编号">
<!-- 查询条件信息 1..1 -->
<queryConditions>
<!-- 1..n -->
<item>
<name>查询条件英文名称</name>
<caption>查询条件中文名称</caption>
<value>查询条件值</value>
</item>
</queryConditions>
<industrySentimentIndex treatResult="子报告查询状态,1：查得，2：未查得，3：其他原因未查得" errorMessage="treatResult=3时的错误描述信息,treatResult!=3时,该属性的值为空" treatErrorCode="treatResult=3时的错误代码,详见数据字典,treatResult!=3时,该属性不存在" subReportTypeCost="收费子报告ID" subReportType="子报告ID">
<industryCode>行业代码</industryCode>
<industryName>行业名称</industryName>
<lastestYear>最新更新年份</lastestYear>
<lastestMonth>最新更新月份</lastestMonth>
<lastestQuarter>最新更新季度</lastestQuarter>
<!--景气指数分析简报数据-->
<analysisBrief>
<lastest3YearAvgIndex>最近3年的平均景气指数</lastest3YearAvgIndex>
<lastestMonth>最新月份</lastestMonth>
<lastestMonthIndexValue>最新月份的景气指数，数值型</lastestMonthIndexValue>
<lastestMonthIncrIndexValue>景气指数最新一个月的增量，数值型</lastestMonthIncrIndexValue>
<briefCaption>行业景气指数分析简报描述</briefCaption>
</analysisBrief>
<!--景气指数列表数据-->
<sentimentIndex>
<item>
<year>年份</year>
<project>项目名称ID，1表示行业景气指数；2表示企业数量</project>
<secondMonth>第二个月的项目值，数值型</secondMonth>
<thirdMonth>第三个月的项目值，数值型</thirdMonth>
<forthMonth>第四个月的项目值，数值型</forthMonth>
<fifthMonth>第五个月的项目值，数值型</fifthMonth>
<sixthMonth>第六个月的项目值，数值型</sixthMonth>
<seventhMonth>第七个月的项目值，数值型</seventhMonth>
<eightnMonth>第八个月的项目值，数值型</eightnMonth>
<ninthMonth>第九个月的项目值，数值型</ninthMonth>
<tenthMonth>第十个月的项目值，数值型</tenthMonth>
<eleventhMonth>第十一个月的项目值，数值型</eleventhMonth>
<twelfthMonth>第十二个月的项目值，数值型</twelfthMonth>
</item>
</sentimentIndex>
<!--行业亏损企业比例变化趋势数据-->
<businessLossesRatio>
<item>
<year>所在年份</year>
<quarter>所在季度</quarter>
<ratioValue>所在年份季度比例值，数值型，单位为%</ratioValue>
<ratioBalance>变化量</ratioBalance>
</item>
</businessLossesRatio>
<!--行业累计销售收入同比增长率变化趋势数据-->
<salesRevenueGrowthRatio>
<item>
<year>所在年份</year>
<quarter>所在季度</quarter>
<ratioValue>所在年份季度比例值，数值型，单位为%</ratioValue>
</item>
<item>
<year>2016</year>
<quarter>3</quarter>
<ratioValue>1%</ratioValue>
</item>
</salesRevenueGrowthRatio>
<totalProfitGrowthRatio>
<!--行业利润总额同比增长率变化情况 0..1-->
<item>
<year>所在年份</year>
<quarter>所在季度</quarter>
<ratioValue>所在年份季度比例值，数值型，单位为%</ratioValue>
</item>
</totalProfitGrowthRatio>
</industrySentimentIndex>
</cisReport>
</cisReports>
"""


def format_result(xml_data, path, header=None):
    if header is None:
        document = etree.XML(xml_data)
    else:
        tempf = open("temp.xml", "w")
        tempf.write(xml_data.strip("\n"))
        tempf.close()
        document = etree.parse("temp.xml")
        os.remove("temp.xml")
    result_report = document.find(path)
    if result_report is None:
        return
    selected = etree.tostring(result_report, encoding='UTF-8')
    selected_dict = xmltodict.parse(selected, xml_attribs=False)

    # result = {}
    # # 顶层节点（industrySentimentIndex节点）
    # for name, value in selected_dict.items():
    #     map_name = config.get(name)
    #     result["name"] = map_name.get("name")
    #     result["value"] = parse_node(value)
    #     result["desc"] = name
    #     result["tag"] = map_name.get("tag")
    return convert_dict(selected_dict)


if __name__ == '__main__':
    report = format_result(xmlStr, 'cisReport/industrySentimentIndex', header=True)
    json_str = json.dumps(report, indent=2, ensure_ascii=False)
    print(json_str)

# -*- coding: utf-8 -*-
import requests

from app.datasource.third import Third
from app.datasource.utils.tools import params_to_dict


class BBD(Third):

    source = 'BBD'
    params_mapping = {
        'user_name_cn': 'name',
        'personal_id': 'documentNo',
        'query_reason_id': 'queryReasonID',
        'card_id': 'cardNos',
        'begin_date': 'beginDate',
        'end_date': 'endDate',
        'card_id': 'accountNo',
        'mobile_num': 'mobile',
        'py_open_bank_id': 'cardNos',
        'license_no': 'licenseNo',
        'car_type': 'carType'
    }

    @staticmethod
    def query(*args, **kwargs):
        kwargs = BBD.pre_query_params(*args, **kwargs)


    @staticmethod
    def query_qyxx_jbxx(company=None, qyxx_id=None):
        """
        企业工商数据-基本信息(Company与qyxx_id 二选一)
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param qk: 用户唯一性验证
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qyxx_jbxx/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '6218684779c4132bbf9180e20e2ebc4d'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_qyxx_gdxx(company=None, qyxx_id=None, page=None, page_size=None, start=None, end=None):
        """
        股东信息API查询
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page: 企业名称，精确匹配(key)
        :param page_size: 每页显示的条数
        :param start: bbd_dotime ：格式2016-01-29
        :param end: bbd_dotime ：格式2016-01-29
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qyxx_gdxx/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '91718c463d479eeb5bcf41b8bac114'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_qyxx_baxx(company=None, qyxx_id=None):
        """
        备案信息
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qyxx_baxx/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '3e2c21da398e8b0784742cc8065a5238'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_qyxx_fzjg_extend(company=None, qyxx_id=None):
        """
        分支机构
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qyxx_fzjg_extend/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '6da1647f095c34c4b7e3482fefc11624'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_qyxx_bgxx(company=None, qyxx_id=None):
        """
        企业信息变更信息
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qyxx_bgxx/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '08d8ed25b77d24ac006aa8d7fe50796c'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_qyxx_nb(company=None, qyxx_id=None, detail=None):
        """
        企业年报
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param detail: 是否显示细节
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qyxx_nb/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '9e210f0872288c1698a659ef4a74abfd'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_rel(company=None, qyxx_id=None):
        """
        关联方
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_rel/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = 'fdc1d84871df1eaa8554269fa3a788c7'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_dishonesty(company=None, qyxx_id=None, page_size=None):
        """
        失信被执行人
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_dishonesty/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '57fe32c5729cd3f5c7fe4d787502c5ca'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_zhixing(company=None, qyxx_id=None, page_size=None):
        """
        被执行人
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_zhixing/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '9cea84a1ec2b48bbfb64cdf2c27051fb'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_ktgg(company=None, qyxx_id=None, page_size=None):
        """
        开庭公告
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_ktgg/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '0b334fa836551ab594acc226590eadde'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_zgcpwsw(company=None, qyxx_id=None):
        """
        裁判文书
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_zgcpwsw/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '84e49e319e9807f755b33da8554d3adf'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_rmfygg(company=None, qyxx_id=None, page_size=None):
        """
        人民法院公告
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_rmfygg/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '432e3cf566973c502ef988ca690c5125'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_qyxg_qyqs(company=None, qyxx_id=None):
        """
        税务数据
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qyxg_qyqs/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '5228580d5cb1ebb510d330cd7775b512'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_ent_trademark(company=None, qyxx_id=None):
        """
        企业商标
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_ent_trademark/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = 'f6166a1b6a21eb132ab83e6a62941d0b'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_domain_name_website_info(company=None, qyxx_id=None, page_size=None):
        """
        域名备案
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_domain_name_website_info/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = 'ed63a43c3b4eba9c1d9d283e395f0356'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_patent(company=None, qyxx_id=None):
        """
        万方专利
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_patent/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '4ba7997f4126c57a4c0bb219fa76ba8e'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_qyxg_jyyc(company=None, qyxx_id=None, page_size=None):
        """
        经营异常
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qyxg_jyyc/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '7120c82b97dd195ce0943128fec8777a'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_ent_softw_copyr(company=None, qyxx_id=None):
        """
        软件著作权
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_ent_softw_copyr/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '1bd14a4c879eab50c67230f415c3885b'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_ent_copyrights(company=None, qyxx_id=None, page_size=None):
        """
        企业作品著作权
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_ent_copyrights/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = 'b257ad26738fa0f7c71ac2e61f357306'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_ent_admin_pena(company=None, qyxx_id=None):
        """
        行政处罚
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_ent_admin_pena/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '9c461172079a238072533432b432c4a6'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_recruit(company=None, qyxx_id=None, page_size=None):
        """
        企业招聘数据
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_recruit/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '57d9e580910823191df1d84e9469b933'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_bidinviting(company=None, qyxx_id=None, page_size=None):
        """
        招标数据
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_bidinviting/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = 'e9c79ff4d6c9cc788d0dc4d396b07203'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_bidwinner(company=None, qyxx_id=None, page_size=None):
        """
        中标数据
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_bidwinner/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '1e1c017da8bd340589c2d24c6f1c96a2'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_overseasinv(company=None, qyxx_id=None, page_size=None):
        """
        境外投资
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_overseasinv/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '73cb77ab6a84ad8aadfd3c8bb651e0ec'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_licence_mining(company=None, qyxx_id=None):
        """
        采矿许可
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_licence_mining/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = 'e042bb26d9982c4a93e97b1021600856'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_licence_pros(company=None, qyxx_id=None, page_size=None):
        """
        探矿许可
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_licence_pros/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '04e3434aec07d0a6bd3297713fbfa3fb'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_qua_comm_cons(company=None, qyxx_id=None, page_size=None):
        """
        通信建设资质
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qua_comm_cons/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '8d8535a1116ae9ba915deba093f37531'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_licence_bui_cons(company=None, qyxx_id=None):
        """
        建筑施工许可
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_licence_bui_cons/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = 'bc0a82246d1d941296b2bff9d99a8541'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_qyxx_gcjljz(company=None, qyxx_id=None):
        """
        工程监理资质
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qyxx_gcjljz/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = 'af7f4d5a48703bbfcc7b8c5901255506'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_qua_itsys_sup(company=None, qyxx_id=None, page_size=None):
        """
        信息系统工程监理资质
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qua_itsys_sup/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '5e7649f674de278856d5c9c3cc7f59d5'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_cert_soft_ent_pro(company=None, qyxx_id=None, page_size=None):
        """
        双软认证
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_cert_soft_ent_pro/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = 'e5338ab1413b22bca468ae1ff3b4145b'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_licence_ind_pro(company=None, qyxx_id=None):
        """
        企业工业产品生产许可
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_licence_ind_pro/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '3db96eeb4c54f43810c5fb913c122b3f'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_qua_pes_pro(company=None, qyxx_id=None):
        """
        农药生产资质
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qua_pes_pro/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '63ed7c6f23943c35838ff73add038794'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_licence_food_pro(company=None, qyxx_id=None, page_size=None):
        """
        食品生产许可
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_licence_food_pro/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '522b24b4f498e51aecc3fb29a07226d4'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_licence_medi_pro(company=None, qyxx_id=None, page_size=None):
        """
        企业药品生产许可证
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_licence_medi_pro/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '450b2c6b49ccfb5cf192c8d4cfb9232c'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_licence_medi_oper(company=None, qyxx_id=None, page_size=None):
        """
        药品经营许可证
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :param page_size: 每页显示的条数
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_licence_medi_oper/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '8bae1c379f46c6c695f6dd93f299f98e'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_qua_cos_pro(company=None, qyxx_id=None):
        """
        化妆品生产许可
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_qua_cos_pro/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '9e2a2e8f04de6920a09845c76201b8e'
        result = requests.get(url=url, params=kwargs)
        return result

    @staticmethod
    def query_gmp_auth(company=None, qyxx_id=None):
        """
        GMP认证
        :param company: 企业名称，精确匹配(key)
        :param qyxx_id: 企业信息ID
        :return:
        """
        url = 'http://dataom.api.bbdservice.com/api/bbd_gmp_auth/'
        kwargs = params_to_dict(1)
        kwargs['ak'] = '97260a333e906530bd32ddb007c67c17'
        result = requests.get(url=url, params=kwargs)
        return result

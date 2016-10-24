import inspect


def params_to_dict(outer=1):
    """
    根据外层参数名,生成参数字典,当参数值为None时,不生成该项,保证参数名符合接口要求
    :param outer: 本函数为第0层，默认获取调用本函数的参数
    :return: 生成的{参数:值}字典
    """
    cf = inspect.currentframe()
    frame = inspect.getouterframes(cf)[outer][0]
    args, _, _, values = inspect.getargvalues(frame)
    # print('function name "%s"' % inspect.getframeinfo(frame)[2])
    result = {i: values[i] for i in args if values[i] is not None}
    result.pop('self')
    return result

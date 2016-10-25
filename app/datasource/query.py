from abc import ABCMeta, abstractmethod

from app.datasource.cup.cup import ChinaUnionPay
from app.datasource.pengyuan.pengyuan import PengYuan
from app.datasource.zzc.zzc import Zzc


class Query:

    # TODO 这里以后可以用迭代的方式完成
    def __init__(self, third=None):
        py = PengYuan()
        zzc = Zzc()
        cup = ChinaUnionPay()
        self.finders = set()
        self.add_third(py)
        self.add_third(zzc)
        self.add_third(cup)
        if third:
            self.finders.add(third)

    def add_third(self, third):
        self.finders.add(third)

    def remove(self, third):
        self.finders.remove(third)

    def query(self, *args, **kwargs):

        for finder in self.finders:
            finder.query(args, kwargs)


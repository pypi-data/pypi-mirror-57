#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: base.py
# @time: 2019/12/10 23:50
# @Software: PyCharm

"""
协同过滤算法
"""
from abc import ABCMeta, abstractmethod


class CFBase(metaclass=ABCMeta):
    def __init__(self, k=3):
        self.k = k
        self.n_user = None
        self.n_item = None

    @abstractmethod
    def init_param(self, data):
        """
        初始化方法
        :param data:
        :return:
        """
        pass

    @abstractmethod
    def prediction(self, *args):
        """

        :param args:
        :return:
        """
        pass

    @abstractmethod
    def recommendation(self, user_id, data):
        pass

    def fit(self, data):
        """
        计算所有用户的推荐物品
        """
        self.init_param(data)
        all_users = []
        for i in range(self.n_user):
            all_users.append(self.recommendation(i, data))
        return all_users

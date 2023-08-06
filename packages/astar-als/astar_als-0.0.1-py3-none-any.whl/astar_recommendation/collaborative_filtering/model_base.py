#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: model_base.py
# @time: 2019/12/10 23:53
# @Software: PyCharm


from collections import defaultdict

import numpy as np

from astar_recommendation.collaborative_filtering.base import CFBase


class CFSVD(CFBase):
    """
    基于矩阵分解的协同过滤算法
    """

    def __init__(self, k=3, r=3):
        super(CFSVD, self).__init__(k)
        self.r = r  # 选取前k个奇异值
        self.uk = None  # 用户的隐因子向量
        self.vk = None  # 物品的隐因子向量

    def init_param(self, data):
        """
        初始化，预处理
        """
        self.n_user = data.shape[0]
        self.n_item = data.shape[1]
        self.svd_simplify(data)
        return data

    def svd_simplify(self, data):
        # 奇异值分解以及简化
        u, s, v = np.linalg.svd(data)
        u, s, v = u[:, :self.r], s[:self.r], v[:self.r, :]  # 简化
        sk = np.diag(np.sqrt(s))  # r*r
        self.uk = u @ sk  # m*r
        self.vk = sk @ v  # r*n
        return

    def prediction(self, user_ind, item_ind, user_row):
        """
        计算预推荐物品i对目标活跃用户u的吸引力
        :param user_ind:
        :param user_row:
        :param item_ind:
        :return:
        """
        rate_ave = np.mean(user_row)  # 用户已购物品的评价的平均值(未评价的评分为0)
        return rate_ave + self.uk[user_ind] @ self.vk[:, item_ind]  # 两个隐因子向量的内积加上平均值就是最终的预测分值

    def recommendation(self, user_ind, data):
        # 计算目标用户的最具吸引力的k个物品list
        item_prediction = defaultdict(float)
        user_row = data[user_ind]
        un_purchase_item_inds = np.where(user_row == 0)[0]
        for item_ind in un_purchase_item_inds:
            item_prediction[item_ind] = self.prediction(user_ind, item_ind, user_row)
        res = sorted(item_prediction, key=item_prediction.get, reverse=True)
        return res[:self.k]

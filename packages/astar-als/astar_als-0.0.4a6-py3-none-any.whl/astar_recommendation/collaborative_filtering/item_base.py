#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: 深圳星河软通科技有限公司 A.Star
# @contact: astar@snowland.ltd
# @site: www.astar.ltd
# @file: item_base.py
# @time: 2019/12/10 23:53
# @Software: PyCharm

from collections import defaultdict

import numpy as np

from astar_recommendation.collaborative_filtering.base import CFBase


class CFKNearest(CFBase):
    """
    基于物品的K近邻协同过滤推荐算法
    """

    def __init__(self, k, criterion='cosine'):
        super(CFKNearest, self).__init__(k)
        self.criterion = criterion
        self.simi_mat = None
        return

    def init_param(self, data):
        # 初始化参数
        self.n_user = data.shape[0]
        self.n_item = data.shape[1]
        self.simi_mat = self.cal_simi_mat(data)

    def cal_similarity(self, i, j, data):
        """
        计算物品i和物品j的相似度
        """
        items = data[:, [i, j]]
        del_inds = np.where(items == 0)[0]
        items = np.delete(items, del_inds, axis=0)
        if items.size == 0:
            similarity = 0
        else:
            v1 = items[:, 0]
            v2 = items[:, 1]
            if self.criterion == 'cosine':
                if np.std(v1) > 1e-3:  # 方差过大，表明用户间评价尺度差别大需要进行调整
                    v1 = v1 - v1.mean()
                if np.std(v2) > 1e-3:
                    v2 = v2 - v2.mean()
                similarity = (v1 @ v2) / np.linalg.norm(v1, 2) / np.linalg.norm(v2, 2)
            elif self.criterion == 'pearson':
                similarity = np.corrcoef(v1, v2)[0, 1]
            else:
                raise ValueError('the method is not supported now')
        return similarity

    def cal_simi_mat(self, data):
        """
        计算物品间的相似度矩阵
        :param data
        """
        simi_mat = np.ones((self.n_item, self.n_item))
        for i in range(self.n_item):
            for j in range(i + 1, self.n_item):
                simi_mat[i, j] = self.cal_similarity(i, j, data)
                simi_mat[j, i] = simi_mat[i, j]
        return simi_mat

    def prediction(self, user_row, item_ind):
        """
        计算预推荐物品i对目标活跃用户u的吸引力
        :param user_row:
        :param item_ind:
        :return:
        """
        purchase_item_inds = np.where(user_row > 0)[0]
        rates = user_row[purchase_item_inds]
        simi = self.simi_mat[item_ind][purchase_item_inds]
        return np.sum(rates * simi) / np.linalg.norm(simi, 1)

    def recommendation(self, user_ind, data):
        # 计算目标用户的最具吸引力的k个物品list
        item_prediction = defaultdict(float)
        user_row = data[user_ind]
        un_purchase_item_inds = np.where(user_row == 0)[0]
        for item_ind in un_purchase_item_inds:
            item_prediction[item_ind] = self.prediction(user_row, item_ind)
        res = sorted(item_prediction, key=item_prediction.get, reverse=True)
        return res[:self.k]

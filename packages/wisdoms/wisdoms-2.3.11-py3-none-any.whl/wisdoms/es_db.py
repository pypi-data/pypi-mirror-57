# Created by Q-ays.
# whosqays@gmail.com

# install elasticsearch_dsl before use

# elastic-search tools

from elasticsearch_dsl import Q, Search
from elasticsearch import Elasticsearch
from datetime import datetime


def inner_o2d_filter(o):
    for k in o:
        if isinstance(o[k], dict):
            inner_o2d_filter(o[k])
        if isinstance(o[k], datetime):
            o[k] = o[k].strftime("%Y-%m-%d %H:%M:%S")


def o2d(obj):
    is_arr = isinstance(obj, list)
    is_set = isinstance(obj, set)

    if is_set or is_arr:
        res = []
        for o in obj:
            if not isinstance(o, dict):
                d0 = o.to_dict(include_meta=True)
                d1 = d0.get('_source')
                d1['id'] = d0.get('_id')
                inner_o2d_filter(d1)
                res.append(d1)
            else:
                if o.get('_source'):
                    d0 = o.get('_source')
                    d0['id'] = o.get('_id')
                    inner_o2d_filter(d0)
                    res.append(d0)
                else:
                    res.append(o)

        return res

    if not isinstance(obj, dict):
        d0 = obj.to_dict(include_meta=True)
        d1 = d0.get('_source')
        d1['id'] = d0.get('_id')
        inner_o2d_filter(d1)
        return d1
    else:
        if obj.get('data'):
            data = obj.get('data')
            obj['data'] = o2d(data)

        return obj


doc_type0 = 'doc'


def repo_ref(doc_type):
    """
    基于es数据库增删改查的公共类
    :param doc_type:
    :return:
    """

    class BaseRepo:

        def __init__(self, ModelType, doc_type=doc_type):
            self.Model = ModelType
            self.index = ModelType.Index.name
            self.type = doc_type

        def add(self, data):
            print(data)
            model = self.Model(**data)
            model.save()
            return model

        def delete(self, did=None):
            if did:
                res = self.Model.get(did)
                res.delete()
                return res

        def update(self, did, data):
            model = self.Model.get(did)
            for key in data:
                if hasattr(model, key):
                    setattr(model, key, data[key])
            model.save()
            return model

        def get(self, did=None, p=None, **kwargs):
            """
            查询对象字段时，参数为对象
            :param did:
            :param p:
            :param kwargs:
            :return:
            """
            if did:
                if isinstance(did, list):
                    obj = self.Model.mget(did)
                else:
                    obj = self.Model.get(did)
            else:
                s = self.Model.search()
                for key in kwargs:
                    if isinstance(kwargs[key], dict):
                        s = s.query('nested', path=key, query=Q('match', **{str(key) + '.id': kwargs[key].get('id')}))
                    else:
                        s = s.query('match', **{key: kwargs[key]})

                if isinstance(p, list) or isinstance(p, tuple):
                    s = s[p[0]:p[1]]
                    res = s.execute()
                else:
                    res = s.scan()

                obj = []
                for o in res:
                    obj.append(o)

            return obj

        def paging(self, p=(0, 10), **kwargs):
            s = self.Model.search()
            for key in kwargs:
                if isinstance(kwargs[key], dict):
                    s = s.query('nested', path=key, query=Q('match', **{str(key) + '.id': kwargs[key].get('id')}))
                else:
                    s = s.query('match', **{key: kwargs[key]})

            if isinstance(p, list) or isinstance(p, tuple):
                s = s[p[0]:p[1]]
                res = s.execute()
                obj = []
                for o in res:
                    obj.append(o)

                data = dict()
                data['loc'] = p[0]
                data['size'] = p[1]
                data['total'] = res.hits.total
                data['data'] = obj

                return data

    return BaseRepo


class EsSearch:
    '''
     es查询其实是对repo_ref中get方法的完善（nested查询）
    '''

    def __init__(self, ES_HOST, http_auth=None):
        self.es = Elasticsearch([ES_HOST], http_auth=http_auth)

    def es_search(self, index, p=None, ns_key='id', **kwargs):
        s = Search(using=self.es, index=index)
        for key in kwargs:
            if isinstance(kwargs[key], dict):
                s = s.query('nested', path=key, query=Q('match', **{str(key) + '.' + ns_key: kwargs[key].get(ns_key)}))
            else:
                s = s.filter('term', **{key + '.keyword': kwargs[key]})

        if isinstance(p, list) or isinstance(p, tuple):
            s = s[p[0]:p[1]]
            res = s.execute()
        else:
            res = s.scan()

        return [{"id": o.meta.id, **o.to_dict()} for o in res]

    def paging(self, index: str, searches: dict, page=(0, 50), sort=None, types: str = None, ns_key='id', **kwargs):
        """

        :param index: index名称
        :param searches: 搜索字典
        :param page: (10,20) {"from": 10, "to": 20}
        :param sort: 排序
        :param types: 搜索类型
        :param ns_key:
        :param kwargs:
        :return:
        """

        s = Search(using=self.es, index=index)

        keyword = kwargs.get('keyword') if isinstance(kwargs.get('keyword'), str) else 'keyword'
        if keyword:
            keyword = '.' + keyword

        if searches:
            for key in searches:
                if isinstance(searches[key], dict):
                    s = s.query('nested', path=key,
                                query=Q('match', **{str(key) + '__' + ns_key: searches[key].get(ns_key)}))
                elif isinstance(searches[key], list):
                    s = s.query('range', **{key: {'gte': searches[key][0], 'lte': searches[key][1]}})
                else:
                    if types in ['term', 'match']:
                        s = s.filter(types, **{key + keyword: searches[key]})
                    else:
                        s = s.filter('wildcard', **{key + keyword: '*' + searches[key] + '*'})
        if sort:
            s = s.sort(sort)  # 排序

        if isinstance(page, list) or isinstance(page, tuple):
            s = s[page[0]:page[1]]
            res = s.execute()

            obj = [{'id': o.meta.id, **o.to_dict()} for o in res]

            data = dict()
            data['loc'] = page[0]
            data['to'] = page[1]
            data['total'] = res.hits.total
            data['data'] = obj

            return data
        else:
            res = s.scan()

            return [{'id': o.meta.id, **o.to_dict()} for o in res]


Repo = repo_ref(doc_type0)

if __name__ == '__main__':
    if not '':
        print('fsdsdf')

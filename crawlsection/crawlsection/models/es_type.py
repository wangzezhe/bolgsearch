
# -*- coding:utf-8 -*-
# 新版本elasticsearch_dsl中DocType变为Document
from elasticsearch_dsl import DocType,Nested,Date,Boolean,analyzer,Completion,Text,Keyword,Integer
from elasticsearch_dsl.connections import connections

# 新建连接
connections.create_connection(hosts="127.0.0.1")

class ArticleType(DocType):
    # 文章类型
    title = Text(analyzer="ik_max_word")
    delivery_time = Date()

    link = Keyword()

    author = Text(analyzer='ik_max_word')

    class Meta:
        # 数据库名称和表名称
        index = "search_engine"
        doc_type = "article_detail"


if __name__ == '__main__':
    ArticleType.init()


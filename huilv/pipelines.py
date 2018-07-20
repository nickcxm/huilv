# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class HuilvPipeline(object):
    def process_item(self, item, spider):
        db=pymysql.connect("localhost", "root", "root", "test")
        cursor=db.cursor();
        sql="insert into ratexe(name,cname,rate,time) values(%s,%s,%s,%s)"
        lis=(item["name"],item["cname"],item["rate"],item["time"])
        cursor.execute(sql,lis)
        db.commit()
        return item

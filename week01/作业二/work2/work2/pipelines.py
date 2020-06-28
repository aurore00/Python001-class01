# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Work2Pipeline:
    # def process_item(self, item, spider):
    #     return item
    # 每一个item管道组件都会调用该方法，并且必须返回一个item对象实例或raise DropItem异常
    def process_item(self, item, spider):
        title = item['title']
        typ = item['typ']
        rels = item['rels']
        output = f'|{title}|\t|{typ}|\t|{rels}|\n\n'
        with open('./movie.csv','a+', encoding='UTF-8') as file:
            file.write(output)
        return item

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import logging

''' 
After an item has been scraped by a spider, 
it is sent to the Item Pipeline which processes it through several components that are executed sequentially
'''
class SpiderTutorialPipeline:

    # This method is called for every item pipeline component.
    def open_spider(self, spider):
        logging.warning('Spider Opened - Pipeline')
    
    # This method is called when the spider is closed.
    def close_spider(self, spider):
        logging.warning('Spider Closed - Pipeline')
    
    # This method is called for every item pipeline component.
    def process_item(self, item, spider):

        ''' 
        Parameters
            item (item object) – the scraped item

            spider (Spider object) – the spider which scraped the item
        '''
        return item

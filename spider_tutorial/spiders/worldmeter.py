import scrapy
from spider_tutorial.items import SpiderTutorialItem

class WorldmeterSpider(scrapy.Spider):
    name = "worldmeter"
    allowed_domains = ["www.worldometers.info"]
    start_urls = ["https://www.worldometers.info/world-population/population-by-country"]

    # 处理服务器返回的响应
    def parse(self, response):
        # 获取页面 title
        # title = response.xpath('//h1/text()').get()

        # 获取页面所有 countries
        countries = response.xpath('//td/a')

        for country in countries:
            country_name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()

            # # 绝对url
            # absolute_url = f"https://www.worldometers.info/{link}"
            # yield scrapy.Request(url=absolute_url)

            # 相对url

            # 每次访问新url, 都会调用parse_country
            yield response.follow(url = link, callback = self.parse_country, meta={'country':country_name})

    # Getting data inside the "link" website
    def parse_country(self, response):

        ''' 
        在Scrapy中，response对象包含了对服务器返回的响应的所有信息，包括请求的元数据。
        response.request属性提供了关于发出请求的详细信息，如请求的URL、请求方法、请求头等。
        在这种情况下，response.request.meta属性用于访问请求的元数据，其中包含了在yield response.follow()方法中传递的meta参数。
        在parse_country方法中，通过response.request.meta['country']获取了之前在parse方法中传递的country参数的值。
        这样可以在处理每个国家的页面时，将国家名称与相应的数据关联起来。
        
        '''
        # Getting country names and each row element inside the population table
        country = response.request.meta['country']

        # You can also use the whole class value  --> response.xpath('(//table[@class="table table-striped table-bordered table-hover table-condensed table-list"])[1]/tbody/tr')
        rows = response.xpath("(//table[contains(@class,'table')])[1]/tbody/tr")  
        # Looping through the rows list
        for row in rows:
            year = row.xpath(".//td[1]/text()").get()
            population = row.xpath(".//td[2]/strong/text()").get()

            Item = SpiderTutorialItem(country = country, year = year, population = population)

            # Return data extracted
            # yield {
            #     'country':country,
            #     'year': year,
            #     'population':population,
            # }

            yield Item
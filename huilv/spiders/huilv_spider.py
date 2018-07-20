from scrapy import Spider
from scrapy import Request
from  huilv.items import HuilvItem

class huilv_Spider(Spider):
    name = "huilv"
    headers={
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url="https://www.xe.com/zh-CN/currencyconverter/convert/?Amount=1&From=USD&To=CNY"
        yield Request(url,headers=self.headers)

    def parse(self, response):
        list=['USD','EUR','GBP','CAD','CHF','DKK','HKD','HUF','JPY','SGD']
        # from scrapy.shell import inspect_response
        # inspect_response(response,self)
        item=HuilvItem();
        item["name"]=response.xpath('.//div[@class=" grid-item chartModule"]/h2/text()').extract()[0][0:3];
        item["cname"]=response.xpath('//div[@class="resultContentWrap"][1]/a/text()').extract()[0];
        item["rate"]=response.xpath('.//span[@class="uccResultAmount"]/text()').extract()[0];
        item['time']=response.xpath('.//span[@class="resultTime"]/text()').extract()[0];

        yield item;
        i=list.index(item["name"]);
        if i<len(list)-1:
            name1=list[i+1]
            next_url="https://www.xe.com/zh-CN/currencyconverter/convert/?Amount=1&To=CNY&From="+name1
            yield Request(next_url,headers=self.headers)

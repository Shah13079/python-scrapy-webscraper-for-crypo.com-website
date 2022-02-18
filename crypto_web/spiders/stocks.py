import scrapy


class StocksSpider(scrapy.Spider):
    name = "stocks"
    allowed_domains = ["crypto.com"]

    def __init__(self, start=1, end=238, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.start = start
        self.end = end


    def start_requests(self):
        for i in range(int(self.start),int(self.end)):
            yield scrapy.Request(
                url=f"https://crypto.com/price?page={i}",
                callback=self.parse,
                headers={
                    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
                },
            )
            

    def parse(self, response):
        all_rows = response.xpath("//tbody/tr")
        for eachRow in all_rows:
            rank = eachRow.xpath(".//td[2]/text()").get()
            name = eachRow.xpath(
                ".//div/span[@class='chakra-text css-1mrk1dy']/text()"
            ).get()
            code = eachRow.xpath(
                ".//div/span[@class='chakra-text css-ft1qn5']/text()"
            ).get()
            price = eachRow.xpath("(.//td[4]//div)[1]/text()").get()
            twnetyFourHourChange = eachRow.xpath(".//td[5]//p/text()").get()
            twentyFourHourVolume = eachRow.xpath(".//td[6]/text()").get()
            marketCap = eachRow.xpath(".//td[7]/text()").get()

            yield {
                "rank": rank,
                "name": name,
                "code": code,
                "price": price,
                "24_H_change": twnetyFourHourChange,
                "24H_volume": twentyFourHourVolume,
                "market_cap": marketCap,
            }


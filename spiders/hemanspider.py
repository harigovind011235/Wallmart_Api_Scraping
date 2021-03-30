import scrapy
import json


class HemanspiderSpider(scrapy.Spider):
    name = 'hemanspider'

    start_urls = ['https://www.walmart.com/cp/api/wpa?el=sponsored-container-middle-1&type=product&min=5&max=20&placementId=1145x345_B-C-OG_TI_5-20_HL-MID-DEALS-NY&platform=desktop&bucketId=1270&moduleLocation=bottom&zipCode=94066&isZipLocated=false&sMode=0&pageType=browse&vtc=WCY6K_1RDSaItr2MyC7cEE&uid=bb487b9f-7897-4877-9d5d-a0b18ac3807f&rviItems=398478802%2C882744417%2C224753442&itemsAddedToCart=0&viewportHeight=1366&viewportWidth=1024&userLoggedIn=false&showBrand=false&itemsList=729779812%2C366039097%2C964901959%2C473172375%2C955671887%2C281202008%2C319542893%2C200236824%2C221771890%2C872552797&pageNumber=1&pageId=4171&keyword=New%20Toys&taxonomy=4171&relUUID=96c4f5e8-9110-405b-afd6-769a81f794e4&persistControls=true&isTwoDayDeliveryTextEnabled=true&mloc=bottom&module=wpa']
    page_no = 2

    def parse(self, response):

        mydata = json.loads(response.body)
        products_list = mydata.get('result').get('products')

        for product in products_list:

            yield {
                'productID': product.get('id').get('productId'),
                'productBrand': product.get('brand'),
                'productName': product.get('productName'),
                'productPrice':product.get('price').get('currentPrice'),
                'productRating':product.get('ratings').get('rating'),
                'ImageLink':product.get('imageSrc'),
                'productURL':product.get('productUrl'),
                'avalibiltyStatus':product.get('availabilityStatus'),
                'pagenumber':HemanspiderSpider.page_no

                 }

        nexturl = f'https://www.walmart.com/cp/api/wpa?el=sponsored-container-middle-1&type=product&min=5&max=20&placementId=1145x345_B-C-OG_TI_5-20_HL-MID-DEALS-NY&platform=desktop&bucketId=1270&moduleLocation=bottom&zipCode=94066&isZipLocated=false&sMode=0&pageType=browse&vtc=WCY6K_1RDSaItr2MyC7cEE&uid=bb487b9f-7897-4877-9d5d-a0b18ac3807f&rviItems=398478802%2C882744417%2C224753442&itemsAddedToCart=0&viewportHeight=1366&viewportWidth=1024&userLoggedIn=false&showBrand=false&itemsList=729779812%2C366039097%2C964901959%2C473172375%2C955671887%2C281202008%2C319542893%2C200236824%2C221771890%2C872552797&pageNumber={HemanspiderSpider.page_no}&pageId=4171&keyword=New%20Toys&taxonomy=4171&relUUID=96c4f5e8-9110-405b-afd6-769a81f794e4&persistControls=true&isTwoDayDeliveryTextEnabled=true&mloc=bottom&module=wpa'

        if HemanspiderSpider.page_no <=10:
            HemanspiderSpider.page_no = HemanspiderSpider.page_no + 1
            yield response.follow(nexturl,callback=self.parse)



        has_next = mydata.get('has_next')

        if has_next:
            next_pageno = mydata.get('page') + 1
            yield scrapy.Request(url = f'https://quotes.toscrape.com/api/quotes?page={next_pageno}',callback=self.parse)








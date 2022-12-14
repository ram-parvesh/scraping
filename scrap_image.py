#scraping Image URLs using selenium
def scrap_image_url(driver):
    images = driver.find_elements_by_xpath("//img[@class='_2r_T1I']")
    brands = driver.find_elements_by_xpath("//div[@class='_2B_pmu']")
    product_description = driver.find_elements_by_xpath("//div[@class='_2LFGJH']/a[1]")
    prices = driver.find_elements_by_xpath("//a[@class='_2W-UZw']//div[@class='_1uv9Cb']")
    #print (len (images) , len (brands) , len (product_descripti.on) , len (prices) )

    product_data = {}
    product_data['image_urls'] = []
    product_data['product_description'] = []
    product_data['brands'] = []
    product_data['prices'] = []
    for image in images:
        source = image.get_attribute('src')
        product_data['image_urls'].append(source)

    for brand in brands:
        product_data['brands'].append(brand.text )
    for product_desc in product_description:
        product_data['product_description'].append(product_desc.text )

    for price in prices:
        product_data['prices'].append(price.text )
    print('Returning scraped data ')

    return product_data

    #driver . close ( )
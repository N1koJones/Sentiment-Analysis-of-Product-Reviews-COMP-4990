
# import the required libraries
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import re

# chromedriver_autoinstaller.install()


def scrape(targetURL):
    try:
        # set up Chrome options
        options = webdriver.ChromeOptions()

        options.add_argument("--headless=new")
        options.add_argument('--no-sandbox')
        options.add_argument("--disable-infobars")
        options.add_argument('--disable-dev-shm-usage')

        # install ChromeDriver and set up the driver instance
        driver = webdriver.Chrome(
            options=options,
        )
        driver.implicitly_wait(10)

        # visit the target URL (input)
        driver.get(targetURL)

        product_name = driver.find_elements(By.ID, "productTitle")[0].text

        price_item = driver.execute_script("return document.querySelector('#corePriceDisplay_desktop_feature_div > div.a-section.a-spacing-none.aok-align-center.aok-relative > span.aok-offscreen')")
        if (not price_item):
            price_item = driver.execute_script("return document.querySelector('#corePrice_desktop > div > table > tbody > tr > td.a-span12 > span.a-price.a-text-price.a-size-medium.apexPriceToPay > span.a-offscreen')")
        

        price = driver.execute_script("return arguments[0].textContent", price_item)

        reviewBox = driver.find_elements(By.CLASS_NAME, "review")
        reviewStarsBox = driver.find_elements(By.CLASS_NAME, "review-rating")
        reviewStars = []
        reviewer = []
        reviewTitle = []
        review = []

        for currReview in reviewStarsBox:
            reviewStars.append(re.findall("[0-5]",currReview.get_attribute("class")))

        for currReview in reviewBox:
            firstBreak = re.search("\n", currReview.text)
            secondBreak = re.search("\n(.)*\n", currReview.text)
            eorWithHelpfulButton = re.search("\nHelpful", currReview.text)
            eorWithFoundHelpful = re.search("\n[0-9]+ (people|person) found this helpful", currReview.text)
            eorWithReport = re.search("\nReport", currReview.text)
            verified = re.search("Verified Purchase\n", currReview.text)
            nonEnglish = re.search("Translate review to English", currReview.text)

            if (nonEnglish):
                reviewStars.pop(len(review))
                continue

            reviewer.append(currReview.text[:firstBreak.regs[0][0]])
            reviewTitle.append(re.sub("\n", "",currReview.text[firstBreak.regs[0][0]:secondBreak.regs[0][1]]))

            if ((not eorWithFoundHelpful) and (not eorWithHelpfulButton)):
                review.append(re.sub("\n", " ", re.sub("Read more", "", currReview.text[verified.regs[0][1]:eorWithReport.regs[0][0]])))
            elif(eorWithFoundHelpful):
                review.append(re.sub("\n", " ",re.sub("Read more", "",currReview.text[verified.regs[0][1]:eorWithFoundHelpful.regs[0][0]])))
            else:
                review.append(re.sub("\n", " ",re.sub("Read more", "",currReview.text[verified.regs[0][1]:eorWithHelpfulButton.regs[0][0]])))
        
            
        driver.quit() 
        #test stuff
        # print (product_name, price, reviewer, reviewTitle, review, reviewStars)
        return (product_name, price, reviewer, reviewTitle, review, reviewStars)
    except Exception as e: 
        print(str(e))
        driver.quit()

#test stuff
# scrape('https://www.amazon.ca/Corduroy-Crossbody-Satchel-Zipper-College/dp/B0CHM6GCJL/ref=pd_vtp_h_pd_vtp_h_d_sccl_1/132-4153041-9409963?pd_rd_w=De0WN&content-id=amzn1.sym.5c9f0cb5-2d5e-4447-9905-de7f3ec4ec72&pf_rd_p=5c9f0cb5-2d5e-4447-9905-de7f3ec4ec72&pf_rd_r=MVT3FZSNNBRBCFM2SSH9&pd_rd_wg=mD9hU&pd_rd_r=52fce5d9-ce00-4b8e-9202-f45487305a77&pd_rd_i=B0CYLV8TFB&th=1')

#Import Libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
import csv
import sys
import pandas as pd
from geopy.geocoders import Nominatim

#Browser Open for Selenium
options = webdriver.ChromeOptions();
options.add_argument('--user-data-dir/.User_Data')
driver = webdriver.Chrome(chrome_options=options)
driver.maximize_window()
driver.get('https:www.google.com/')
time.sleep(2)


CompanyInputFileName =[]
Sub_Name_List =[]
multiListComments= []
multilistnames =[]
multiliststars =[]
google_address_list= []
page_exist = []
google_review_page_name =[]
review_rating_list =[]
address_in_review_page = []
phone_no_in_review_page = []
address_on_google= []
google_total_review = []
stars_rate_each_customer = []
company_website_link =[]
multicustomerlinks = []
CompanyOwnerReply=[]
dayandtime =[]
all_sm_link =[]
#all list define
with open('Testing - Copy - Copy.csv', newline='') as csvfile:
    data = csv.DictReader(csvfile)

    # File Open and company name on browser
    for row in data:
        company_name = (row['name'])
        city_name = (row['city'])
        CompanyInputFileName.append(company_name)
        driver.find_element_by_tag_name("input").send_keys(company_name + ' '+ city_name)
        driver.find_element_by_tag_name("input").send_keys(Keys.ENTER)
        sleep(2)
        website_links = driver.current_url
        google_address_list.append(website_links)
        #print("Google link: ", driver.current_url)
        time.sleep(2)


        #Check side bar review page exist or not
        try:
            checking = driver.find_element_by_class_name('SPZz6b')
            if checking.is_displayed():

                # Get company name from right side review box
                try:
                    Company_name_google_review = driver.find_element_by_class_name('qrShPb')
                    print('Company name on Google:' , Company_name_google_review.text)
                    google_review_page_name.append(Company_name_google_review.text)
                except:
                    #print('No Name Mention')
                    google_review_page_name([])

                #Get SubType Name of Company
                try:
                    Sub_name = driver.find_element_by_class_name('YhemCb')
                    print('Company Sub Name:', Sub_name.text)
                    Sub_Name_List.append(Sub_name.text)
                except:
                    Sub_Name_List.append([])

                # Company Website Link from Right Side
                try:
                    company_name_link = driver.find_element_by_class_name('ab_button').get_attribute('href')
                    print('Company website link', company_name_link)
                    company_website_link.append(company_name_link)
                except:
                    print('No Website Link')
                    company_website_link.append([])

                # Comapany Rating on Google
                try:
                    review_rating = driver.find_element_by_class_name('Aq14fc')
                    print('Company Review', review_rating.text)
                    review_rating_list.append(review_rating.text)
                except:
                    print('No Rating on Google')
                    review_rating_list.append([])

                # Total number of reviews
                try:
                    total_review = driver.find_element_by_class_name('hqzQac')
                    split_review_no = total_review.text
                    G_review = split_review_no.split('Google')
                    G_review_apend = G_review[0]
                    print('Total no of Reviews', G_review_apend)
                    google_total_review.append(G_review_apend)
                except:
                    print('Zero Reviews on Google')
                    google_total_review.append([])

                # Adreess on google Maps
                try:
                    review_adrees = driver.find_elements_by_class_name('Z1hOCe')
                    address = review_adrees[0].text
                    if address[0] == 'A':
                        print(address)
                        address_on_google.append(address[9:])
                    else:
                        print('No Address mention')
                        address_on_google.append([])
                except:
                    address_on_google.append([])
                    print('No address Title on Google Maps')

                # Phone Number in Google Maps
                try:
                    review_phone = driver.find_elements_by_class_name('Z1hOCe')
                    phone = review_phone[1].text
                    if phone[0] == 'P':
                        phone_no_in_review_page.append(phone[7:])
                        print(phone)
                except:
                    phone_no_in_review_page.append([])
                    # print('No Phone Number Mention at Google')

                #Day and office hours of Company at Google maps
                try:
                    ofce_hours_btn = driver.find_element_by_class_name('BTP3Ac')
                    ofce_hours_btn.click()
                    time.sleep(1)
                    officetiming = driver.find_elements_by_class_name('WgFkxc')
                    for dayntime in officetiming:
                        dayandtime.append(dayntime.text)
                        #print(dayntime.text)
                except:
                    #print('No Day and Office hours in Google Maps')
                    dayandtime.append([])


                # Scoial Media Urls
                s_medialist = []
                try:
                    all_links = driver.find_elements_by_class_name('ap3N9d')
                    for smlinks in all_links:
                        SM_Links = smlinks.find_element_by_tag_name('a').get_attribute('href')
                        print('Social Media Links', SM_Links)
                        s_medialist.append(SM_Links)
                except:
                    s_medialist.append([])
                all_sm_link.append(s_medialist)





                #(Check Reviews link is avaialble or not)
                try:#ashar
                    abc = driver.find_element_by_class_name('hqzQac')
                    #if abc.is_displayed():
                    abc.click()
                    print('clickss')
                    time.sleep(5)
                    review_list = driver.find_element_by_class_name('review-dialog-list')
                    last_height = driver.execute_script(
                        "return document.getElementsByClassName(\'review-dialog-list\')[0].scrollHeight")
                    while True:
                        driver.execute_script("document.getElementsByClassName(\'review-dialog-list\')[0].scrollTo(0, document.getElementsByClassName(\'review-dialog-list\')[0].scrollHeight)")
                        sleep(5)
                        new_height = driver.execute_script("return document.getElementsByClassName(\'review-dialog-list\')[0].scrollHeight")
                        # print('new_height:', new_height)
                        if new_height == last_height:
                            break

                        else:
                            last_height = new_height
                            time.sleep(2)
                    # Expand review to click more button
                    more_button = driver.find_elements_by_class_name("review-more-link")
                    for MClick in more_button:
                        MClick.click()

                    # Customers Reviews comments
                    try:
                        customer_review = driver.find_elements_by_class_name('Jtu6Td')
                        each_customer_comment = []
                        for customers_Reviews in customer_review:
                            customer_comment = customers_Reviews.text
                            customer_comment.replace('\n', ' ')
                            each_customer_comment.append(customer_comment)
                    except:
                        print_no_comment = 'No Comments from Customers'
                        each_customer_comment.append(print_no_comment)
                    multiListComments.append(each_customer_comment)

                    # Each Response from owner
                    try:
                        OwnerAnswer = driver.find_elements_by_class_name('LfKETd')
                        each_owner_reply =[]
                        for owner_reply in OwnerAnswer:
                            replies = owner_reply.text
                            replies.replace('\n',' ')
                            each_owner_reply.append(replies)
                    except:
                        print('No Reply from Owner')
                        each_owner_reply.append([])
                    CompanyOwnerReply.append(each_owner_reply)

                    # Customers Name on Google Maps
                    try:
                        customer_Name = driver.find_elements_by_class_name('TSUbDb')
                        all_customers_names = []
                        for check in customer_Name:
                            all_customers_names.append(check.text)
                    except:
                        # print('No Names found on Google maps')
                        all_customers_names.append([])
                    multilistnames.append(all_customers_names)


                    # Each Customer ID Links
                    try:
                        Customer_link = driver.find_elements_by_class_name('TSUbDb')
                        link_customer = []
                        for CLINK in Customer_link:
                            co_link = CLINK.find_element_by_tag_name('a').get_attribute('href')
                            link_customer.append(co_link)
                    except:
                        # print('Not find link of Customer')
                        link_customer.append([])
                    multicustomerlinks.append(link_customer)

                    # Each Customer stars ratings on Google
                    list = []
                    try:
                        star_review = driver.find_elements_by_css_selector('span.Fam1ne.EBe2gf')
                        for stars in star_review:
                            Customers_Stars = stars.get_attribute("aria-label")
                            list.append(Customers_Stars[6])
                    except:
                        print('No Star rated by Customer')
                        list.append([])
                    multiliststars.append(list[4:])






                    time.sleep(2)
                    #print('May I waiting for back ')
                    driver.back()
                    time.sleep()
                    driver.back()
                except:
                    driver.back()
            else:
                print('Page name on google side bar is not display')
                '''multiListComments.append([])
                multicustomerlinks.append([])
                multiliststars.append([])
                multilistnames.append([])'''
                driver.back()
        except:
            print(company_name + ' Not in Google Reviews')
            google_review_page_name.append([])
            Sub_Name_List.append([])
            company_website_link.append([])
            review_rating_list.append([])
            google_total_review.append([])
            address_on_google.append([])
            phone_no_in_review_page.append([])
            multilistnames.append([])
            multiliststars.append([])
            multicustomerlinks.append([])
            multiListComments.append([])
            dayandtime.append([])
            all_sm_link.append([])
            CompanyOwnerReply.append([])
            driver.back()

driver.quit()
# Google Cordinates
latitudes = []
longitudes =[]
for location in address_on_google:
    locator = Nominatim(user_agent='myGeocoder')
    cordinates = locator.geocode(location)
    if cordinates is not None:
        latitudes.append(cordinates.latitude)
        longitudes.append(cordinates.longitude)
    else:
        latitudes.append('No address')
        longitudes.append('No Address')

#Print all lists
print(google_address_list)
print(Sub_Name_List)
print(google_review_page_name)
print(company_website_link)
print(review_rating_list)
print(google_total_review)
print(address_on_google)
print(phone_no_in_review_page)
print(multilistnames)
print(multiliststars)
print(multicustomerlinks)
print(multiListComments)
print(latitudes)
print(longitudes)
print(dayandtime)
print(all_sm_link)
#Data Save on the Csv File


df = pd.DataFrame(list(zip(google_address_list,Sub_Name_List,google_review_page_name,company_website_link,review_rating_list,
                           address_on_google,phone_no_in_review_page,multilistnames,multiliststars,multicustomerlinks,multiListComments,
                           latitudes,longitudes, dayandtime,all_sm_link)),
             columns=['google_address_list',
                      'google_review_page-name',
                      'company_website_link',
                      'review_rating_list',
                      'address_on_google',
                      'phone_no_in_review_page',
                      'multilistnames',
                      'multiliststars',
                      'multicustomerlinks',
                      'multiListComments',
                      'latitudes',
                      'longitudes',
                      'dayandtime',
                      'all_sm_link'])

df.set_index(['google_address_list','google_review_page','company_website_link','review_rating_list','address_on_google','phone_no_in_review_page',
              'latitudes','longitudes','dayandtime','all_sm_link']).apply(pd.Series.explode).reset_index()

check.to_csv(r'C:\Users\92334\PycharmProjects\460Scraping\Save.csv', index = False, header=True)

'''with open("GoogleMapsReview.csv","w", newline='', encoding="utf-8") as csvFile:
    fieldnames = ['GoogleLink','CompanyName','CompanyWebsite','CompanyRating','TotalReviews','CompanyAddress','CompanyPhone','CustomerNames','CustomersLinks','CustomerStars','CustomerComments','Latitude','Longitude','OfficeTimings','SocialMediaLinks']
    writer = csv.DictWriter(csvFile, fieldnames=fieldnames)
    writer.writeheader()
    for G_link, G_company_name,G_sub_Name,C_website_link,C_over_all_rating,G_total_review,C_adress,C_Phone,C_Name,C_Links,C_Rating,C_comments,lat,lng,Ofice_time,sm_links in zip(google_address_list, google_review_page_name,Sub_Name_List,company_website_link,review_rating_list,google_total_review,address_on_google,phone_no_in_review_page,multilistnames,multicustomerlinks,multiliststars,multiListComments,latitudes,longitudes,dayandtime,all_sm_link):
        writer.writerow({'GoogleLink': G_link, 'CompanyName': G_company_name,'SubName':G_sub_Name,'CompanyWebsite': C_website_link,'CompanyRating':C_over_all_rating,'TotalReviews':G_total_review,'CompanyAddress':C_adress,'CompanyPhone':C_Phone,'CustomerNames':C_Name,'CustomersLinks':C_Links,'CustomerStars':C_Rating,'CustomerComments':C_comments,'Latitude':lat,'Longitude':lng,'OfficeTimings':Ofice_time,'SocialMediaLinks':sm_links})
    sys.exit()'''


import json
Final_data_list = []
for i in range(len(google_address_list)):
    data = {
        "Searching Name": CompanyInputFileName[i],
        "Company Name" : google_review_page_name[i],
        "Sub Name" : Sub_Name_List[i],
        "Website Link" : company_website_link[i],
        "Company Overall Rating" : review_rating_list[i],
        "Total Reviews" : google_total_review[i],
        "Address" : google_address_list[i],
        "Phone No" : phone_no_in_review_page[i],
        "Customers Names" : multilistnames[i],
        "Each Customer Star": multiliststars[i],
        "Address as latitude":latitudes[i],
        "Address as longitude": longitudes[i],
        "Office Timings": dayandtime[i],
        "Social Media Links":  all_sm_link[i],
        "Each Customer Profile Link": multicustomerlinks[i],
        "Each Customer Comments": multiListComments[i],
        "Each Owner Reply":CompanyOwnerReply[i]

                }

    Final_data_list.append(data)
print(Final_data_list)
fl = open("data_file.json", "w",encoding='utf-8')
json.dump(Final_data_list,fl,sort_keys=True,indent=4)
fl.close()

#The End

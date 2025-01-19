import csv

fileName = "top_100_products_reviews.csv"


feilds = []         #feilds from csv (Id,ProductId,UserId,Score,Summary,Text)
review_id = []      #id of the review
product_id = []     #product id
user_id = []        #user id
scores = []         #1,2,3,4,5
tagline = []        #tagline of the review (GREAT, BEST EVER PRODUCT, etc.)
tokens = []         #the review broken up into tokens based on whitespace/spaces


with open(fileName, "r") as csv_line:  
    reader = csv.reader(csv_line)

    feilds = next(reader)

    for row in reader:
        review_id.append(row[0])
        product_id.append(row[1])
        user_id.append(row[2])
        scores.append(row[3])
        tagline.append(row[4])
        tokens.append(row[5].split())

fileName.close()
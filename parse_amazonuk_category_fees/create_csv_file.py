import csv

def create(results):
    with open('amazonuk_category_fees.csv', 'w', newline='') as file:
        file.write("'Category', 'Referral Fee', 'Min Referral Fee'\n")
        file.close()

    with open('amazonuk_category_fees.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(results)
        file.close()
    

    # for i in results:
    #     i = re.sub('\)', '', str(i))
    #     i = re.sub('\(', '', i)
    #     i = re.sub('\t', '', i)
    #     i = re.sub('•', '', i)
    #     print(i)

        # with open('amazonuk_category_fees.csv', 'a') as file:
        #     file.write(i)
        #     file.close()


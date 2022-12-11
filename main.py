from amazon.customdriver import CustomDriver
from amazon.amazon import Amazon
import time
from amazon.amazon_filter import Filters



custom_driver = CustomDriver()
amazon= Amazon(custom_driver)
amazon.first_page()
    

amazon.item_search("nike socks")
# amazon.item_search(input("What do you want to buy : "))
time.sleep(2)
amazon.take()
# amazon.minPrice("20")
# amazon.minPrice(input("Please enter minimum price : "))
amazon.maxPrice("70")
time.sleep(2)
# amazon.minPrice(input("Please enter maximum price : "))
amazon.review(star="3")
# amazon.Review(int(input("Please enter review point ( note: max 4, min 1 ) : ")))
# amazon.sort_by_low()
# amazon.ShoeSize(value="5")
# amazon.Size(xsize="M")
time.sleep(3)
# bot.filter(input("Maximum price? : "))
amazon.report()  


# except Exception as e:
#     print(f'Exception encountered: {e}')
#     exc_type, exc_obj, exc_tb = sys.exc_info()
#     fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
#     print(exc_type, fname, exc_tb.tb_lineno)



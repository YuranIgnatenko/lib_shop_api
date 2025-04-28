from lib_shop_api.parser import Parser 
from lib_shop_api.constants import *
from lib_shop_api.urls import URLS

def test():
	parser = Parser()
	with open("out.txt", "a", encoding="utf-8") as file:
		for key in URLS.keys():
			url = URLS[key]
			count_pages = parser.get_count_pages(key)
			count_products = parser.get_count_products(key)
			products = parser.get_products(key,count_pages)
			out = f"url: {url}\nall products: {count_products}\nall pages: {count_pages}\nproducts: {[str(product) for product in products]}\n\n"
			print(url)
			file.write(out)

def test_iterator(iters=1):
	parser = Parser()
	with open("out2.txt", "a", encoding="utf-8") as file:
		for key in URLS.keys():
			url = URLS[key]
			file.write(f"\nurl: {url}\n")
			for product in parser.get_products_iterator(key, iters):
				out = f"product: {str(product)}\n"
				print(out)
				file.write(out)

# test()
test_iterator(1)



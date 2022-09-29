import unittest

# Counts the number of a's in a sentence (e.g., a string)
def count_a(sentence):
	total = 0
	for i in range(len(sentence)):
		if sentence[i] == 'a':
			total += 1
	return total


# Item class
# Describes an item to be sold. Each item has a name, a price, and a stock.
class Item:
	# Constructor.
	def __init__(self, name, price, stock):
		self.name = name
		self.price = price
		self.stock = stock

	# Print
	def __str__(self):
		return ("Item = {}, Price = {}, Stock = {}".format(self.name, self.price, self.stock))

# Warehouse class
# A warehouse stores items and manages them accordingly.
class Warehouse:

	# Constructor
	def __init__(self, items = []):
		self.items = items[:]

	# Prints all the items in the warehouse, one on each line.	
	def print_items(self):
		for item in self.items:
			print(item)
			print("\n")	

	# Adds an item to the warehouse	
	def add_item(self, item):
		self.items.append(item)

	# Returns the item in the warehouse with the most stock		
	def get_max_stock(self):
		max_stock_dict = {}
		max_stock_dict = {i:self.items.count(i) for i in self.items}
		return max(max_stock_dict, key=max_stock_dict.get)
	
	# Returns the item in the warehouse with the highest price
	def get_max_price(self):
		return max(Item.item[1])
		


# Tests
class TestAllMethods(unittest.TestCase):

	# SetUp -- we create a bunch of items for you to use in your tests.
	def setUp(self):
		self.item1 = Item("Beer", 6, 20)
		self.item2 = Item("Cider", 5, 25)
		self.item3 = Item("Water", 1, 100)
		self.item4 = Item("Fanta", 2, 60)
		self.item5 = Item("CocaCola", 3, 40)

	## Check to see whether count_a works
	def test_count_a(self):
		#print(f"Testing count_a(The cat makes cake), it should output 3 {count_a("The cat makes cake")}")
		self.assertEqual(count_a("The cat makes cake"),3, "Tested count_a for The cat makes cake, which should equal 3")
		self.assertEqual(count_a("aaaaaa"),6, "Tested count_a for aaaaaa, which should equal 6")
		self.assertEqual(count_a("Winter hats are warm and fashionable"),6, "Tested count_a for Winter hats are warm and fashionable, which should equal 6")

	## Check to see whether you can add an item to the warehouse
	def test_add_item(self):
		self.assertEqual(Warehouse.add_item(self.item1),"Beer")

	## Check to see whether warehouse correctly returns the item with the most stock
	def test_warehouse_max_stocks(self):
		items = []
		items.append(self.Item1)
		items.append(self.Item3)
		items.append(self.Item3)
		self.assertEqual(Warehouse.get_max_stock(self.items),"Water")


	# Check to see whether the warehouse correctly return the item with the highest price
	def test_warehouse_max_price(self):
		self.assertEqual(Warehouse.get_max_price(self.items),"Beer")
		

def main():
	unittest.main()

if __name__ == "__main__":
	main()
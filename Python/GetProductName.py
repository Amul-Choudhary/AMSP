import cv2
import pytesseract
import re

path = "../Samples/"

products = ["DMP Plus", "ABC", "Remin"]
compounds = ["paracetamol", "domperidone"]

def getStrings(image):
	raw_image = cv2.cvtColor(cv2.imread(path + image), cv2.COLOR_BGR2RGB)
	return pytesseract.image_to_string(raw_image)

def getProduct(image):
	texts = getStrings(image).lower()
	pred_product = None
	contents = []
	for product in products:
		if (product.lower() in texts):
			pred_product = product

	for line in texts.split("\n"):
		comp = None
		#print(line)
		for word in line.split(" "):
			if (word in compounds):
				comp = word
		q = None
		if (comp):
			x = re.search("(\d)+( mg|mg)?", line)
			if (x):
				q = x.group(0)

		if (comp):
			contents.append((comp, q))

	return {"product_name": pred_product, "components": contents}
				

if __name__ == "__main__":
	#print(getStrings('4.jpeg'))
	print(getProduct('4.jpeg'))
	

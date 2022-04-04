"""
Author: Jaimin Bhoi(ajaymin28)
Date: 4/4/2022

Do whatever you want with this code. Just keep the Author same.

"""


import base64
from PIL import Image
from io import BytesIO

class Helpers:

	def __init__(self):
		pass

	def get_img_from_array(self,arry):
		pil_img = Image.fromarray(arry)
		buff = BytesIO()
		pil_img.save(buff, format="JPEG")
		img = base64.b64encode(buff.getvalue()).decode("utf-8")
		return img
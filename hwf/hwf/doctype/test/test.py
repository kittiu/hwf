# Copyright (c) 2023, Kitti U. and contributors
# For license information, please see license.txt

import frappe
import json
import os
from frappe.model.document import Document

class Test(Document):

	DATA_FILE = "/home/kittiu/frappe-bench/apps/hwf/hwf/hwf/doctype/test/data_file.json"

	@staticmethod
	def get_current_data() -> dict[str, dict]:
		"""Read data from disk"""
		print("----------------0", str, dict)
		if not os.path.exists(Test.DATA_FILE):
			return {}
		with open(Test.DATA_FILE) as f:
			return json.load(f)

	# @staticmethod
	# def update_data(data: dict[str, dict]) -> None:
	# 	print("----------------1")
	# 	"""Flush updated data to disk"""
	# 	with open(Test.DATA_FILE, "w+") as data_file:
	# 		json.dump(data, data_file)

	# def db_insert(self, *args, **kwargs):
	# 	print("----------------2",args, kwargs)
	# 	d = self.get_valid_dict(convert_dates_to_str=True)

	# 	data = self.get_current_data()
	# 	data[d.name] = d

	# 	self.update_data(data)

	# def load_from_db(self):
	# 	print("----------------3", self)
	# 	data = self.get_current_data()
	# 	d = data.get(self.name)
	# 	super(Document, self).__init__(d)

	# def db_update(self, *args, **kwargs):
	# 	print("----------------4", args, kwargs)
	# 	# For this example insert and update are same operation,
	# 	# it might be  different for you.
	# 	self.db_insert(*args, **kwargs)

	# def delete(self):
	# 	print("----------------5")
	# 	data = self.get_current_data()
	# 	data.pop(self.name, None)
	# 	self.update_data(data)

	@staticmethod
	def get_list(args):
		print("----------------6", args)
		data = Test.get_current_data()
		return [frappe._dict(doc) for name, doc in data.items()]

	@staticmethod
	def get_count(args):
		print("----------------7", args)
		data = Test.get_current_data()
		return len(data)

	@staticmethod
	def get_stats(args):
		print("----------------8", args)
		x = 1/9
		return {}

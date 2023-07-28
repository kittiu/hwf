def sum_total(doc, method=None):
	# sum lines
	doc.total_amount = sum(list(map(lambda x: x.amount, doc.items)))

#!/usr/bin/python3

nums = [2, 8, 9, 48, 8, 22, -12, 2]
news = []
for i in nums:
	if i > 5:
		news.append(i + 2)
print("Original array:", nums)
print("New array:", news)

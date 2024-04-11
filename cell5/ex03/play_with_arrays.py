#!/usr/bin/python3

nums = [2, 8, 9, 48, 8, 22, -12, 2]
news = []
for i in nums:
	if i > 5:
		news.append(i + 2)
news = set(news)
print(nums)
print(news)

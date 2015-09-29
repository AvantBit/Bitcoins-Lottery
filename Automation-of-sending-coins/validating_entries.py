from itertools import islice, imap
import csv
from collections import defaultdict

with open("Entries#x1.csv") as f,open("winningnumbers.csv") as nums:
    nums = set(imap(str.rstrip, nums))
    r = csv.reader(f)
    results = defaultdict(list)
    for row in r:
        results[sum(n in nums for n in islice(row, 1, None))].append(row[0])

print(results)

number_matched_0 = results[0]
number_matched_1 = results[1]
number_matched_2 = results[2]
number_matched_3 = results[3]
number_matched_4 = results[4]
number_matched_5 = results[5]

print(number_matched_0, number_matched_1, number_matched_2, number_matched_3, number_matched_4, number_matched_5)
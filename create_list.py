import json, random

'''
titles scraped from the following Polygon article
"Animal Crossing: New Horizons Nook Mileage rewards list"
by Julia Lee
https://www.polygon.com/animal-crossing-new-horizons-switch-acnh-guide/2020/3/20/21186746/nook-mileage-rewards-titles-list-tasks-miles-chart-table

my endless gratitude to Julia Lee and the folks at Polygon!
'''

acTitlesFirst = []
acTitlesSecond = []

#make a list out of the left titles
with open("left.txt") as f:
	for line in f:
		x = line.rstrip('\r\n')
		acTitlesFirst.append(x)

#make a list out of the right titles
with open("right.txt") as f:
	for line in f:
		x = line.rstrip('\r\n')
		#this deals with the multi gender titles (like "Mr./Ms. Popular")
		if "/" in x:
			masc = x.split("/")[0]
			fem = x.split("/")[-1]
			beginning = masc.split(" ")[0] + " "
			if beginning == masc + " ":
				beginning = ""
			ending = " " + fem.split(" ")[-1]
			if ending == " " + fem:
				ending = ""
			acTitlesSecond.append(beginning + fem)
			acTitlesSecond.append(masc + ending)
		else:
			acTitlesSecond.append(x)

allTitles = []

#make every possible combination of the two titles (which is surprisingly, a lot)
for l in acTitlesFirst:
	for r in acTitlesSecond:
		allTitles.append(l + " " + r)

#randomize the order and write to a json file for later usage
random.shuffle(allTitles)
with open("titles.json", 'w') as f:
	json.dump(allTitles, f)

with open("outbox.json", 'w') as f:
	json.dump([], f)

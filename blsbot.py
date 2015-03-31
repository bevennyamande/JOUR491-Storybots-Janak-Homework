import csv, string, datetime

reader = csv.reader(open("blsdata.csv", "rU"), dialect = csv.excel)

reader.next()

blslist = [row for row in reader]

currentyear = filter(None,blslist[-1])

yearlen = len(currentyear)

if yearlen != 1:
	currentmonth = currentyear[-1]
	previousmonth = currentyear[-2]
	reportyear = int(currentyear[0])
	reportmonth = len(currentyear)-1
	reportdate = datetime.datetime(reportyear, reportmonth, 1)
else:
	currentmonth = currentyear[1]
	previousyear = blslist[-2]
	previousmonth = previousyear[-6]
	reportyear = int(currentyear[0])
	reportmonth = len(currentyear)-1
	reportdate = datetime.datetime(reportyear, reportmonth, 1)

previousyear =  blslist[-2]
previousyearmonth = previousyear[yearlen-1]

if currentmonth > previousmonth:
	verb = "increased"
elif currentmonth == previousmonth:
	verb = "held steady"
else:
	verb = "dropped"
	
pctchange = ((float(currentmonth)-float(previousmonth))/float(previousmonth)*100)

# so the %change does print as a negative number: print verb, abs(pctchange)

print("The Labor Department reported on Sept."
	"5 that the unemployment rate {} to {} percent in Aug."
	"That's down 1.1 percentage points campared to {} percent in Aug. 2013.".format((verb, currentyear[-1], previousyear[-6]))


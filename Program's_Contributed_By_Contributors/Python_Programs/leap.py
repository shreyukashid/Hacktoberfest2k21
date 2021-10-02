#PYTHON FUNCTION TO CHECK WETHER YEAR IS A LEAP YEAR OR NOT

def is_leap(year):
	leap=False
	if int(year)%4==0:
		if int(year)%100==0:
			if int(year)%400==0:
				leap=True
		else:
			leap=True
	return leap
year=int(input())
print(is_leap(year))
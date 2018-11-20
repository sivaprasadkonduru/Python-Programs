'''
Design a generic function that takes following input
Maximum score: Smax
Minimum Score: Smin
Number of Bands: X
Calculate Score: Sac

Score range is divided equally among the bands. Find out the band in which the calculated score lies ?
Eg. If Maximum score is 100.
Minimum score is 1
Number of Bands is 5
Then each band is divided into 20 scores -
Band 1 = 1-20						Band 2 = 21-40
Band 3 = 41-60						Band 4 = 61-80
Band 5 = 81-100

'''

def find_band(min_score, max_score, no_of_bands, cscore):

    if min_score < 1:
        raise ValueError('Min score cannot be lesser than 1')

    if max_score > 100:
        raise ValueError('Max score cannot be greater than 100')

    bands = max_score - min_score
    bands = bands / no_of_bands
    divide_bands = {i+1: list(range(int(bands * i), int(bands * (i + 1)))) for i in range(no_of_bands)}
    for k, v in divide_bands.items():
        if cscore in v:
            print(k)


find_band(1, 100, 5, 65)

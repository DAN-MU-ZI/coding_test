fest_2017_awards_table = (0, 500, 300, 300, 200, 200, 200,
                         50, 50, 50, 50, 30,
                          30, 30, 30, 30, 10, 10,
                           10, 10, 10, 10)
fest_2018_awards_table = (0, 512, 256, 256, 128, 128,
                        128, 128, 64, 64, 64, 64,
                         64, 64, 64, 64, 32, 32,
                          32, 32, 32, 32, 32, 32,
                           32, 32, 32, 32, 32, 32,
                            32, 32)

num_lines = int(input())
total_awards = []

for i in range(num_lines):
    fest_2017, fest_2018 = [int(x) for x in input().split()]
    award = 0
    if fest_2017 < len(fest_2017_awards_table):
        award+=fest_2017_awards_table[fest_2017]
    if fest_2018 < len(fest_2018_awards_table):
        award+=fest_2018_awards_table[fest_2018]
    
    total_awards.append(award)

for total in total_awards:
    print(total*10000)
#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Site    : 
# @File    : main.py


import numpy as np

ds = """
1000
1000
1000
1000
1000
1000
1000
1066
1160
1254
1186
1142
1027
1069
1097
1003
1009
1087
1029
1012
927
880
878
785
644
696
746
875
822
822
808
797
770
837
914
1133
1200
1321
1356
1540
1702
1614
1628
1691
1604
1634
1650
1680
1642
1849
1955
1942
1951
1897
1849
1879
1891
1657
1421
1626
1473
1524
1488
1491
1302
1188
968
906
958
994
950
790
750
825
804
760
773
765
807
798
740
812
855
880
908
795
560
464
394
574
556
593
631
672
645
597
578
792
859
909
920
973
1009
991
971
871
"""
dt = [int(d) for d in ds[1:-1].split("\n")]


def adjust(new_order, old_order, rate):
    order_adjusted = old_order + (new_order - old_order) * rate
    return int(order_adjusted)

def main(rate):
    arrive_today = [1000]  # since day 8
    arrive_tomorrow = [1000]  # since day 8
    inventory_yeterday = [0]  # since day 7 end
    inventory_today = []  # since day 8
    shorage_today = []  # since day 8
    z = 1.64
    order_yeterday=[1000]



    for day in range(8, 107):
        for_sale = arrive_today[-1] + inventory_yeterday[-1]  # receive goods
        needs_today = dt[day - 1]  # customer consume
        if for_sale > needs_today:  # supply>demand
            inventory_today.append(for_sale - needs_today)
            shorage_today.append(0)
        else:  # supply <=demand
            shorage_today.append(needs_today - for_sale)
            inventory_today.append(0)
        # demand forcasting
        dt1 = int(np.average(dt[day - 3:day]))
        dt2 = int((sum(dt[day - 2:day]) + dt1) / 3)
        dTL = int((dt1 + dt2)/2)
        sig = int(np.sqrt(2 * np.var(dt[day - 7:day])))
        order = int(dTL + sig * z - inventory_today[-1])
        order=adjust(order,order_yeterday[-1],rate)
        #start delivery
        arrive_today.append(arrive_tomorrow[-1])
        arrive_tomorrow.append(order)
        inventory_yeterday.append(inventory_today[-1])
        # break
    return (order_yeterday,shorage_today,inventory_today)

datas=[]
for rate in np.arange(0,1,0.02):
    datas.append(main(rate))
    print(rate)
# for data in datas:
#     print(np.average(data[2]))


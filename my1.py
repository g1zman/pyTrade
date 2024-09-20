# 29.08.2024
# trade
import os
import time
import sys
from pathlib import Path
import math
import random
import http.client
data = {}
with open("ranData.txt","r",encoding="utf-8") as file:
    for line in file:
        line = line.strip()
        if "=" in line:
            key,numbers = line.split("=")
            key = key.strip()
            numbers = numbers.strip()
            number_list = list(map(float,numbers.split(" ")))
            data[key] = number_list
            print("market added: " + key)
            print(data)
            index = int(input("Enter the required index:"))
            values_at_index = [number_list[index] for number_list in data.values() if len(number_list) > index]
            if values_at_index:
                minn = values_at_index[0]
                for d in values_at_index[1:]:
                    if d <= minn:
                        minn = d
            if values_at_index:
                maxx = 0
                for l in values_at_index:
                    if l > maxx:
                        maxx = l
                print(f"Highest price on index {index}:", maxx, "on market:",)
                print(f"Lowest price on index {index}:", minn, "on market:",)
                print(f"Potential spread on index {index}:", maxx - minn)
            else:
                print(f"Insufficient data on index {index}")
                # классы читать
                # массивы
                # git + github DONE
                # add time - index correlation. add hc lc - market connection - ??
                # 06.09. 24_
           # lowcost = min(data)
            #highcost = max(data)
            #print("Наименьшая цена:", lowcost)
            #print("Наибольшая цена:",  highcost)
            #print("Потенциальный spread:", highcost - lowcost,  "$")
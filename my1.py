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
            print(data)
            index = 1
            values_at_index = [number_list[index] for number_list in data.values() if len(data) > index]
            if values_at_index:
                lowcost = min(values_at_index)
                highcost = max(values_at_index)
                print(f"Наименьшая цена по индексу {index}:", lowcost)
                print(f"Наибольшая цена по индексу {index}:", highcost)
                print(f"Потенциальный спред по индексу {index}:", highcost - lowcost)
            else:
                print(f"Недостаточно данных по индексу {index}")
                # классы читать
                # массивы
                # git + github
                #
           # lowcost = min(data)
            #highcost = max(data)
            #print("Наименьшая цена:", lowcost)
            #print("Наибольшая цена:",  highcost)
            #print("Потенциальный spread:", highcost - lowcost,  "$")
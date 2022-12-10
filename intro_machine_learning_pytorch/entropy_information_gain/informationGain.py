import numpy as np
from pandas import read_csv


def two_group_ent(first, tot):
    return -(first/tot*np.log2(first/tot) +
             (tot-first)/tot*np.log2((tot-first)/tot))

#Reference for below Code =>

# tot_ent = two_group_ent(10, 24)
# g17_ent = 15/24 * two_group_ent(11,15) + 9/24 * two_group_ent(6,9)
#
# answer = tot_ent - g17_ent
#
# print(answer)
def get_avg(num,total):
    return num/total

def get_child_ent(totalCount, totalCriteriaCount, totalChildWithCriteriaCount):
    return get_avg(totalCriteriaCount,totalCount) * two_group_ent(totalChildWithCriteriaCount, totalCriteriaCount)

data = read_csv("ml-bugs.csv")
colorGreenCount = (data['Color']=="Green" ).sum()
colorBrownCount = (data['Color']=="Brown").sum()
colorBlueCount = (data['Color']=="Blue").sum()

speciesMoBugCount = ( data['Species']=="Mobug" ).sum()
speciesLoBugCount = (data['Species']=="Lobug").sum()

lengthLessThan17Count = (data['Length (mm)'] < 17).sum()
lengthGreaterThan20Count = (data['Length (mm)'] > 20).sum()

print ("colors size:",len(data['Color']))
print("green count: ",colorGreenCount)
print("blue count : ",colorBlueCount)
print("brown count : ",colorBrownCount)

print("Mobug count : ",speciesMoBugCount)
print("Lobug count : ",speciesLoBugCount)


print("LengthLessThan17Count count : ", lengthLessThan17Count)
print("LengthGreaterThan20Count count : ", lengthGreaterThan20Count)

colorGreenCount_df = data.loc[data['Color']=="Green"]
colorBlueCount_df = data.loc[data['Color']=="Blue"]
colorBrownCount_df = data.loc[data['Color']=="Brown"]
speciesMoBugWithColorGreenCount = ( colorGreenCount_df['Species']=="Mobug" ).sum()
speciesMoBugWithColorBlueCount = ( colorBlueCount_df['Species']=="Mobug" ).sum()
speciesMoBugWithColorBrownCount = ( colorBrownCount_df['Species']=="Mobug" ).sum()


speciesMoBugWithColorNotGreenCount = speciesMoBugWithColorBlueCount+speciesMoBugWithColorBrownCount
speciesMoBugWithColorNotBlueCount = speciesMoBugWithColorGreenCount+speciesMoBugWithColorBrownCount
speciesMoBugWithColorNotBrownCount=speciesMoBugWithColorBlueCount+speciesMoBugWithColorGreenCount

print("speciesMoBugWithColorGreenCount count : ",speciesMoBugWithColorGreenCount)
print("speciesMoBugWithColorBlueCount count : ",speciesMoBugWithColorBlueCount)
print("speciesMoBugWithColorBrownCount count : ",speciesMoBugWithColorBrownCount)

lengthLessThan17_df = data.loc[data['Length (mm)'] < 17]
lengthGreaterThan20_df = data.loc[data['Length (mm)'] > 20]

lengthGreaterThan17_df = data.loc[data['Length (mm)'] > 17]
lengthLessThan20_df = data.loc[data['Length (mm)'] < 20]


print("lengthGreaterThan17_df count : ",len(lengthGreaterThan17_df))
print("lengthLessThan17_df count : ",len(lengthLessThan17_df))
print("lengthGreaterThan20_df count : ",len(lengthGreaterThan20_df))
print("lengthLessThan20_df count : ",len(lengthLessThan20_df))

speciesMoBugWithLengthLessThan17Count = ( lengthLessThan17_df['Species']=="Mobug" ).sum()

speciesMoBugWithLengthGreaterThan20Count = ( lengthGreaterThan20_df['Species']=="Mobug" ).sum()

speciesMoBugWithLengthGreaterThan17Count = ( lengthGreaterThan17_df['Species']=="Mobug" ).sum()

speciesMoBugWithLengthLessThan20Count = ( lengthLessThan20_df['Species']=="Mobug" ).sum()


print("speciesMoBugWithLengthLessThan17Count count : ",speciesMoBugWithLengthLessThan17Count)
print("speciesMoBugWithLengthGreaterThan20Count count : ",speciesMoBugWithLengthGreaterThan20Count)
print("speciesMoBugWithLengthGreaterThan17Count count : ",speciesMoBugWithLengthGreaterThan17Count)
print("speciesMoBugWithLengthLessThan20Count count : ",speciesMoBugWithLengthLessThan20Count)

total_ent = two_group_ent(speciesMoBugCount,len(data))
entTotalSpeciesMoBugWithLengthLessThan17 = get_child_ent(len(data),len(lengthGreaterThan17_df),speciesMoBugWithLengthGreaterThan17Count) + get_child_ent(len(data),len(lengthLessThan17_df),speciesMoBugWithLengthLessThan17Count)

infoGainSpeciesMoBugWithLengthLessThan17 = total_ent - entTotalSpeciesMoBugWithLengthLessThan17



entTotalSpeciesMoBugWithLengthGreaterThan20 = get_child_ent(len(data),len(lengthGreaterThan20_df),speciesMoBugWithLengthGreaterThan20Count) + get_child_ent(len(data),len(lengthLessThan20_df),speciesMoBugWithLengthLessThan20Count)

infoGainSpeciesMoBugWithLengthGreaterThan20 = total_ent - entTotalSpeciesMoBugWithLengthGreaterThan20

entTotalSpeciesMoBugWithLengthGreaterThan20 = get_child_ent(len(data),len(lengthGreaterThan20_df),speciesMoBugWithLengthGreaterThan20Count) + get_child_ent(len(data),len(lengthLessThan20_df),speciesMoBugWithLengthLessThan20Count)

infoGainSpeciesMoBugWithLengthGreaterThan20 = total_ent - entTotalSpeciesMoBugWithLengthGreaterThan20


entTotalSpeciesMoBugWithColorGreen = get_child_ent(len(data),len(colorGreenCount_df),speciesMoBugWithColorGreenCount) + get_child_ent(len(data),len(data)-len(colorGreenCount_df),speciesMoBugWithColorNotGreenCount)

infoGainSpeciesMoBugWithColorGreen = total_ent - entTotalSpeciesMoBugWithColorGreen

entTotalSpeciesMoBugWithColorBlue = get_child_ent(len(data),len(colorBlueCount_df),speciesMoBugWithColorBlueCount) + get_child_ent(len(data),len(data)-len(colorBlueCount_df),speciesMoBugWithColorNotBlueCount)

infoGainSpeciesMoBugWithColorBlue = total_ent - entTotalSpeciesMoBugWithColorBlue

entTotalSpeciesMoBugWithColorBrown = get_child_ent(len(data),len(colorBrownCount_df),speciesMoBugWithColorBrownCount) + get_child_ent(len(data),len(data)-len(colorBrownCount_df),speciesMoBugWithColorNotBrownCount)

infoGainSpeciesMoBugWithColorBrown = total_ent - entTotalSpeciesMoBugWithColorBrown


print(infoGainSpeciesMoBugWithLengthLessThan17)
print(infoGainSpeciesMoBugWithLengthGreaterThan20)
print(infoGainSpeciesMoBugWithColorGreen)
print(infoGainSpeciesMoBugWithColorBlue)
print(infoGainSpeciesMoBugWithColorBrown)

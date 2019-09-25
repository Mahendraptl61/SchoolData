import csv, time, itertools
schoolData='school_data.csv'
csvData=[]
SchoolNameList=[]
SchoolStateList=[]
SchoolMetroCentricList=[]
SchoolCityList=[]
SchoolCityCount={}
def readCsv(fileName):
  with open(fileName,'rU') as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
   csv_reader.next()
   for row in csv_reader:
        csvData.append(row)
        
  return csvData


def print_counts():
    global SchoolNameList,SchoolStateList
    schoolsInStateCount=0
    schoolsInMetroCentricCount=0
    schoolsInCityCount=0
    schoolCityCount=0
    TotalSchoolData=readCsv(schoolData)
    print "Total Number Records :",len(TotalSchoolData)
    for data in TotalSchoolData:
          global SchoolMetroCentricList
          global SchoolCityList
          SchoolNameList.append(data[3])
          SchoolStateList.append(data[5])
          SchoolMetroCentricList.append(data[8])  
          SchoolCityList.append(data[4])
    SchoolNameList=set(SchoolNameList)
    SchoolStateList=set(SchoolStateList)      
    SchoolMetroCentricList=set(SchoolMetroCentricList)
    SchoolCityList=set(SchoolCityList)
    
    print "Schools by State:"
    for school in SchoolStateList:
        for schoolData1 in TotalSchoolData:
            if school in schoolData1:
               schoolsInStateCount+=1
        
        SchoolState=school.lstrip()
        SchoolState=SchoolState.rstrip()
        print school ," : ",schoolsInStateCount           
        schoolsInStateCount=0   
    
    print "\n\nSchools by Metro-Centric locale :"
    for metro in SchoolMetroCentricList:
        for schoolData2 in TotalSchoolData:
            if metro in schoolData2:
                   schoolsInMetroCentricCount+=1
        
        SchoolState=school.lstrip()
        SchoolState=SchoolState.rstrip()
        print metro ," : ",schoolsInMetroCentricCount           
        schoolsInMetroCentricCount=0       
    
    #Logic For To Find the City Name With Most Schools 
    for city in SchoolCityList:
      for schoolData3 in TotalSchoolData:
          if city in schoolData3:
            schoolCityCount+=1    
      
      SchoolCityCount.update({city:schoolCityCount})
      schoolCityCount=0
    mostCityValue = max(SchoolCityCount.items(), key=lambda x : x[1])
    print "City With Most Schools: ",mostCityValue[0]," (",mostCityValue[1]," Schools)"
    
    #Logic For Finding Unique Cities With One School
    listOfUniqueCityWithOneSchool = [key  for (key, value) in SchoolCityCount.items() if value == 1]
    print "Unique Cities With At Least One School: ",len(listOfUniqueCityWithOneSchool)


    

print_counts()




import csv, time, itertools
from difflib import get_close_matches 
schoolData='/Users/mahendra.aricent/Documents/PythonCode/schools-data-python-srhinos-1170-master/school_data.csv'
csvData=[]
searchSchoolRes=[]
schoolName=''

#Logic For To Load data from CSV file and store in Python List 
def readCsv(fileName):
  with open(fileName,'rU') as csv_file:
   csv_reader = csv.reader(csv_file, delimiter=',', quotechar='|')
   csv_reader.next()
   for row in csv_reader:
        csvData.append(row)
        
  return csvData


# Logic For To Search The school
def search_schools(schoolName1):
    global searchSchoolRes,schoolName
    schoolName=schoolName1
    count=0
    substringSchoolList=schoolName.split(' ')
    TotalSchoolData=readCsv(schoolData)
    for data1 in substringSchoolList:
       data1=data1.upper()
       for data in TotalSchoolData:  
         if (data1 in data ) or (data1 in data[3]) or (data1 in data[4] ) or  (data1 in data[5]):
             #print data
             searchSchoolRes.append([data[3],data[4],data[5]])
                                     
        
#schoolName="elementary school highland park"          
search_schools("elementary school highland park"  )
#search_schools("jefferson belleville")
#search_schools("riverside school 44")
#search_schools("granada charter school")
#search_schools("foley high alabama")
#search_schools("KUSKOKWIM")
start_time=time.time()   
count=0
end_time=time.time()     
print "Results For ",schoolName," Search Took (",(end_time-start_time)*1000," ms... )"
if len(searchSchoolRes)<3:
    for data1 in searchSchoolRes:
       count+=1 
       print count, " ", data1[0]," ",data1[1]," ",data1[2]
else:
   for data1 in searchSchoolRes:
       count+=1
       print count, " ", data1[0]," ",data1[1]," ",data1[2]
       if count==3:
           break 
  

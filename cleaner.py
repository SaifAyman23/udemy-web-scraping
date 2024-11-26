import pandas as pd
import numpy as np

courses_list = []

with open("data.txt") as file:
    courses_list = file.read().split("================================")
    
courses_list = [x.split("\n") for x in courses_list]
del courses_list[-1]

data = []
for course in courses_list:
    element = []
    del course[-1]
    
    if course[-1] == "Bestseller":
            course[-1] = "Yes"
    else:
        course.append(np.nan)
    for piece in course:
        if isinstance(piece,str) and (piece in ("Instructor:", "Instructors:", "Current Price", "Original Price", "Current price", "Original price", "") or "Rating:" in piece):
            continue
        
        element.append(piece)
    data.append([element[0],*element[2:]])
            
for element in data:
    for piece in element:
        print(piece)
    print("-------------------------------------------")



courses = pd.DataFrame(data, columns=["Name", 
                                "Description", 
                                "Instructor", 
                                "Rating", 
                                "Number of Ratings", 
                                "Total Hours", 
                                "Number of Lectures", 
                                "Level", 
                                "Current Price", 
                                "Original Price", 
                                "Bestseller"])
print(courses)

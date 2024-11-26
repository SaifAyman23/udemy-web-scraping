import pandas as pd
import numpy as np

courses_list = []

# To split the courses into individual elements
with open("data.txt") as file:
    courses_list = file.read().split("================================")
    
# To further split courses into specific info.
courses_list = [x.split("\n") for x in courses_list]
del courses_list[-1]

data = []
for course in courses_list:
    element = []
    
    # Since the list element is a result of using '\n', we don't need it
    del course[-1]
    
    if course[-1] == "Bestseller":
            course[-1] = "Yes"
    else:
        course.append(np.nan)
        
    for piece in course:
        # To remove unwanted data
        if isinstance(piece,str) and (piece in ("Instructor:", "Instructors:", "Current Price", "Original Price", "Current price", "Original price", "") or "Rating:" in piece):
            continue
        
        element.append(piece)
    data.append([element[0],*element[2:]])
            
columns = ["Name", "Description", "Instructor", "Rating", "Number of Ratings",  
           "Total Hours", "Number of Lectures", "Level", "Current Price",  
           "Original Price", "Bestseller"]
courses = pd.DataFrame(data, columns=columns)
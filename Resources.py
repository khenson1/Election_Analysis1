import os
import csv
#create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("Analysis", "election_analysis.txt")


#Using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:

    #write a header and three counties
    txt_file.write("Counties in the Election\n--------------\nArapahoe\nDenver\nJefferson")



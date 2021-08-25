##Introduction  
The program Assignment07.py collects a list of movie names and ratings from the user, displays them back to the user, and stores them in binary file movie_ratings.dat.  The user can also read a pre-existing binary file (made from Assignment07.py) and add to it.  
##The Script  
At the top of the script there is a header and pseudo code to orient any future developers.  Next, the pickle function is imported and the remaining code is broken into Data, Processing, and Presentation & Main sections.  
In the Data and Processing sections, simple functions are defined to save data, read data, and pause the program.  The Pickle program is used to both dump (i.e. save) and load (i.e. read) data to/from the movie_ratings.dat binary file.  See Figure 1 for details.  
(Add Fig1)  
The Presentation & Main section contains code supporting user interactions and the main logic of the program.  The main logic operates through a while(True) loop that holds nested if elif statements.  All movie and rating data is added to list of dictionaries where “Movie” and “Rating” are used as keys.  
The Presentation & Main section also contains two try except-as chunks of code that catch errors when the user: 
a) tries to load a non-existent output file   
b) enters a non-numeric value for a movie rating   
In both cases, a custom error message is displayed and the user is returned to the main menu. See Figure 2 for a screenshot of the Presentation & Main section.  
(Add Fig2)  
##Running the Code and the Output File  
The script operates as intended in both PyCharm and console mode.  Screenshots of the code running in console mode, running in Pycharm, and the output binary file movie_ratings.dat are presented in Figure 4, Figure 5, and Figure 6.  
(Add Fig3)  
(Add Fig4)  
(Add Fig5)  
##Summary  
The focus of this assignment was pickling and error handling.  The Assignment07.py program utilizes both of these Python functionalities while:   
•	capturing a list of the user’s movie ratings  
•	storing that list in a binary file (movie_ratings.dat)  
•	presenting sensible error messages in response to likely input errors  

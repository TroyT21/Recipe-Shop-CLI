# Recipe-Shop-CLI
CLI front end for Recipe-Shop

# How to run
The CLI was tested and runs on aviary machines.

Pre-requisites: Have Python 3 and pip installed (these were already installed on aviary machines when I tested)

1. Open terminal in same folder as "rs.py" file
2. Run command "pip install ascii_magic" to install ASCII Magic (used for displaying images as ascii art in terminal)
3. Run command "python3 rs.py" to start CLI

\
The CLI is set to connect to a machine hosting our server by default (ip: recipeshop.ca, port:80).\
If the CLI is not connecting to the server for some reason, you can run our server code (link to repo at bottom) on a different machine and change the ip address and port the CLI tries to connect to with the command "connect [ip] [port]" to connect to a different machine.

# Feature
I implemented the "Search for Recipes" feature of our project in this CLI.\
https://github.com/njzfjiang/Recipe-Shop/issues/34

Use the command "search" to search for recipes which has 4 different versions:
1. "search [keywords]"
2. "search [keywords] [mealType]" 
3. "search [keywords] [minTime] [maxTime]"
4. "search [keywords] [minTime] [maxTime] [mealType]"

\
[mealType] can be "Breakfast", "Dinner", "Lunch", "Snack", or "Teatime"\
[minTime] and [maxTime] are whole number integers in minutes for cooking time\
[keywords] text string, separate multiple keywords with a "/" (no spaces between keywords)

After using the "search" command you can use the "recipe" command to view more info on a specific recipe.\
Run command "recipe [recipeNumber]" to view info on the recipe at [recipeNumber] in the most recent search.\
This also generates an "image.html" file in the same folder as "rs.py" that can be opened in a browser to see a more detailed ascii art image (if you want to see it).

You can run the "last" command to view the results of your most recent search.\
Run command "last"

# Reflection
Using distributed/n-tier architecture for our project made it easy to make this CLI interface, because I only needed to implement a UI (presentation layer) and to know how to interact with our server (logic layer) through our api. I did not need to know the specifics of what the server does or how the server interacts with the database (data layer), I only needed to know what requests to send to the server.

This code base does follow n-tier architecture. This CLI is just a presentation layer UI that interacts with the data layer (server). It does do some checks to ensure it's sending valid requests to the server though.

The documentation in our project was accurate and easy for me to understand. I find it easy to understand, but I might be a little biased since I had hand in working on most of the different layers of our project. So I already understood most of it before reading through the documentation.

I did not have to change any code outside of the UI layer. This CLI uses the same requests to our server as our other two front ends use, so nothing on server or db needed to change. The only thing that's different is how this CLI presents the responses it gets from our server.

# Honesty Declaration
UNIVERSITY OF MANITOBA
Faculty of Science
Department of Computer Science

Honesty Declaration for Individual Work

I, the undersigned, declare that the attached assignment is wholly the 
product of my own work, and that no part of it has been:
  - copied by manual or electronic means from any work produced by any 
    other person(s), present or past, including tutors or tutoring services,
  - based on laboratory work that I did not complete due to unexcused 
    absence(s),
  - produced by several students working together as a team (this includes 
    one person who provides any portion of an assignment to another student
    or students),
  - copied from any other source including textbooks and web sites, or
  - modified to contain falsified data, except as directly authorized by 
    the Instructor.

I understand that penalties for submitting work which is not wholly my own, 
or distributing my work to other students is considered an act of Academic 
Dishonesty and is subject to penalty as described by the University of 
Manitoba's Student Discipline Bylaw*.

Please PRINT all information: 

Course                : COMP4350 \
Section               : A01 \
Last Name, First Name : Thomas, Troy \
Student Number        : 7768464 \
UM Email              : thomast9@myumanitoba.ca \
Date                  : 2024-12-08 

(*) Penalties that may apply, as provided for under the University of 
Manitoba's Student Discipline By-Law, range from a grade of zero for the 
assignment, failure in the course to expulsion from the University. The 
Student Discipline By-Law may be accessed at:

http://umanitoba.ca/admin/governance/governing_documents/students/868.htm



# Extra Info
Recipe-Shop-CLI made by Troy Thomas\
GitHub username: TroyT21\
email: thomast9@myumanitoba.ca or troy21thomas@gmail.com

Recipe-Shop server and web client\
https://github.com/njzfjiang/Recipe-Shop

Recipe-Shop-App-Version\
https://github.com/njzfjiang/Recipe-Shop-App-Version

Uses Python cmd library for base CLI framework\
https://docs.python.org/3/library/cmd.html

Uses ASCII Magic to convert images to ASCII art\
https://pypi.org/project/ascii-magic/
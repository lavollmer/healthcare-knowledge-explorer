# Healthcare Knowledge Explorer Application

This project was aimed at learning about Azure, neoj4, cypher and data management. In the process, I was unable to continue with neoj4 due to free instance ending. I switched to Python, SQL and Streamlit to showcase the data.

## Table of contents

- [Overview](#overview)
  - [Links](#links)
- [My process](#my-process)
  - [Built with](#built-with)
  - [Learnings](#learnings)
  - [Useful resources](#useful-resources)
- [Author](#author)

## Overview

Tech Stack:
Frontend: Streamlit
Backend API: Flask (Python) with neo4j-driver
Database: Neo4j Aura Free - switched to SQL

### Links

- Live Site URL: [Laura Dev Healthcare Knowledge Explorer]()

## My process

I began by determining my tech stack and what my minimum viable product would be. I wanted to make a small REST API that accepts a medication generic name query or parameter and Neo4j would display the brand name. It would return JSON which will eventually be displayed in React. I wanted to start small in order to build upon code that was functioning properly.

I began by setting up the backend folder. I wanted to include a .env file, requirements txt file and the main python file to run the script. I determined which version I had installed of Python on my computer which was Python 3.13.2. Before starting my new Python project, I created a virtual environment to install Python Flask. virtual environments allow for more customizable, and isolated experiences in the sense of being able to download dependencies without it affecting other things. Pip allows an indviidual to freeze dependencies to record the versions we are using in a file called requirements.txt. I installed Python Flask on my file which I used because of it's flexibility with single-page applications.

After setting up the basics of Python Flask, I proceeded to install neo4j Python driver which will let me connect and query the Neo4j graph database. My finall installation was for flask-cors because I plan to use this backend API with a React frontend.

### Built with

- Azure
- Python 3.13.2
- Neo4j Aura
- [React](https://reactjs.org/) - JS library
- TailwindCSS
- Vite
- Google Fonts
- Flexbox
- CSS Grid
- Mobile-first workflow

### Learnings

Takeaways from this project:
1. Once you install Neo4j driver and have a running instance of the driver then you connect the database. You connect the database by creating a Driver object and providing a URL and login credentials. I came back to this project a few weeks later and found out that my neo4j instance free trail had expired. I decided to move towards to SQL.

### Useful resources

Resources I used to help build my project or reference:
- [Set Up Python Flask](https://www.twilio.com/docs/usage/tutorials/how-to-set-up-your-python-and-flask-development-environment)
-[Creation of Virtual Environments](https://docs.python.org/3/library/venv.html)
- [Python Flask](https://www.geeksforgeeks.org/python/flask-tutorial/)
- [Neo4j Driver Manual](https://neo4j.com/docs/python-manual/current/install/)

## Author

- Website - [Laura V](https://lauradeveloper.com/)
- Frontend Mentor - [@lavollmer](https://www.frontendmentor.io/profile/lavollmer)
- Github - [@lavollmer](https://github.com/lavollmer)
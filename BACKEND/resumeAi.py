
import requests
import json
from jinja2 import Environment, FileSystemLoader
import os
import random

class BasicInfo:
    def __init__(self, name, endYear, email, number):
        self.name = name
        self.endYear = endYear
        self.email = email
        self.number = number 
        self.skill_list = []
        self.experience_list = []

    # ... (rest of the BasicInfo class methods) def getName(self):
        return self.name
    
    def getEndYear(self):
        return self.endYear

    def getEmail(self):
        return self.email

    def getNumber(self):
        return self.number
     
    def enterSkill(self):
        skill = input() 
        self.skill_list.append(skill)
    
    def getExperience(self):
        experince = input()
        self.experience_list.append(experince)

    def printSkills(self):
        print(self.skill_list)

    def printExperience(self):
        print(self.experience_list)

def main():
    # Create an empty JSON template structure
    template_data = {
        "basics": {
            "name": "",
            "email": "",
            "phone": "",
            "website": ""
        },
        "work": [],
        "education": [],
        "skills": [],
        "projects": [],
        "languages": [],
        "experience": []
    }

    curName = input("Name: ")
    curEmail = input("Email: ")
    curNumber = input("Number: ")
    curEndYear = input("End Year: ")

    # Collect user data for different sections
    # ...

    # Update the JSON template structure with user data
    template_data["basics"]["name"] = curName
    template_data["basics"]["email"] = curEmail
    template_data["basics"]["phone"] = curNumber
    template_data["basics"]["website"] = ""  # Add website if needed

    # Handle the "work" section separately
    work_experience = input("Work Experience: ")
    template_data["work"].append({
        "company": work_experience,
        "position": "",
        "startDate": "",
        "endDate": "",
        "summary": ""
    })

    # Collect and append data for other sections (education, skills, etc.)
    # ...

    # At this point, template_data contains the merged data
    # You can proceed to convert it to JSON or render it into a document
    # ...
    env = Environment(loader=FileSystemLoader('.'))
    template = env.get_template('resume_template.html')

    #Render the template with the merged JSON data
    html_resume = template.render(template_data)

    # Save the HTML to a file
    with open('resume.html', 'w') as html_file:
        html_file.write(html_resume)
        

if __name__ == "__main__":
    main()


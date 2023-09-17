import requests; 
import json;

class BasicInfo:
    def __init__(self, name, endYear, email, number):
        self.name = name
        self.endYear = endYear
        self.email = email
        self.number = number 
        self.skill_list = []
        self.experience_list = []
        
    def getName(self):
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




    #def setName(self, name):
    #    self.name = name
    #def setEndYear(self, endYear):
    #   self.endYear = endYear
    #def setEmail(self, email):
    #    self.email = email
    #def setNumber(self, number):
    #    self.number = number 


def main():    
    
    resume_info = {
  "basics": {
    "name": "",
    "email": "",
    "phone": "",
    "website": ""
  },
  "work": [
    {
      "company": "",
      "position": "",
      "startDate": "",
      "endDate": "",
      "summary": ""
    }
  ],
  "education": [
    {
      "institution": "",
      "degree": "",
      "endDate": ""
    }
  ],
  "skills": [
    {
      "name": "",
      "level": ""
    },
    {
      "name": "",
      "level": ""
    }
  ],
  "projects": [
    {
      "name": "",
      "description": "",
      "url": ""
    },
    {
      "name": "",
      "description": "",
      "url": ""
    }
  ],
  "languages": [
    {
      "language": ""
    },
    {
      "language": ""
    }
  ],
  "experience": [
    {
      "name": ""
    },
    {
      "name": ""
    }
  ]
}


    
    curName = input("Name: ")
    curEmail = input("Email: ")
    curNumber = input("Number: ")
    curEndYear = input("End Year: ")

    # Collect more user data for different resume sections
    # You can use functions similar to enterSkill() and getExperience() for each section

    # For example:
    work_experience = input("Work Experience: ")
    education = input("Education: ")
    skills = input("Skills: ")

    # Update the resume_info dictionary with the collected user data
    resume_info["basics"]["name"] = curName
    resume_info["basics"]["email"] = curEmail
    resume_info["basics"]["phone"] = curNumber
    resume_info["basics"]["endDate"] = curEndYear

    # Update other sections in resume_info with user data

    # Merge user data with the template
    with open('structure.json', 'r') as template_file:
        template_data = json.load(template_file)

    for section, section_data in resume_info.items():
        if section in template_data:
            print(f"Updating section: {section}")
            template_data[section].update(section_data)

    #for section, section_data in resume_info.items():
    #    if section in template_data:
    #        template_data[section].update(section_data)

    # At this point, template_data contains the merged data
    # You can proceed to convert it to JSON or render it into a document
    # ...

if __name__ == "__main__":
    main()

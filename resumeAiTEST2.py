import requests
import json
from jinja2 import Environment, FileSystemLoader
import os
import random
from google.oauth2 import service_account
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials

class Institution:
    def __init__(self, institutionName, start, end, degree, grad):
        self.institutionName = institutionName
        self.start = start
        self.end = end
        self.degree = degree
        self.grad = False


    def setGraduation(self):
        self.degree = input()
        if(self.degree == False): return False
        else: return True

    def setStart(self):
        self.start = input()
        return self.start

class BasicInfo:
    def __init__(self, name, email, number):
        self.fullName = name
        self.endYear = 'N\A'
        self.email = email
        self.number = number 
        self.skill_list = []
        self.experience_list = []
        self.institutions = []

    def getName(self):
        #Add wordcount 25-30
        return self.fullName
    
    def getEndYear(self):
        return self.endYear

    def getEmail(self):
        return self.email

    def getNumber(self):
        return self.number
     
    def enterSkill(self):
        #Add count word
        skill = input() 
        self.skill_list.append(skill)
    
    def getExperience(self):
        experince = input()
        self.experience_list.append(experince)
    
    def createInstitution(self):
        resInstitution = Institution() 
        resInstitution.degree = input()
        resInstitution.start = input()
        resInstitution.end = input()
        resInstitution.grad = input()
        if(resInstitution.grad == True):
            resInstitution.grad = True
        else:
            resInstitution.grad = False
        return resInstitution

    def enterInstitution(self, Institution):
        self.institutions.append(Institution)

    def printSkills(self):
        if(self.skill_list.size() == 0): return 'N\A'
        print(self.skill_list)

    def printExperience(self):
        if(self.experience_list.size() == 0): return 'N\A'
        print(self.experience_list)

SCOPES = ["https://www.googleapis.com/auth/drive", "https://www.googleapis.com/auth/documents"]
resume_templates = [idToVariable1, idToVariable2, idToVariable3, idToVariable4, idToVariable5, idToVariable6, idToVariable7]
chosen_template_id = random.choice(resume_templates)
copy_title = 'User Resume'
copied_doc = service_drive.files().copy(fileId = chosen_template_id, body ={"name": copy_title}).execute()
secret_key_code = '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'
flow = InstalledAppFlow.from_client_secrets_file(secret_key_code, SCOPES)
creds = flow.run_local_server(port =0)
service_drive = build('drive', 'v3', credentials=creds)
service_docs = build('docs', 'v1', credentials=creds)
doc_id = copied_doc['id']

def main():

    
    
    idToVariable1 = '1ZVi3Muf8rPZHzvPXD-W8WxJrNL2lhw569d2sAZg7sdg'
    idToVariable2 = '16Sptf5FwGZajLE5kPs0OB5Qy5lECqyckzx_K4hCY09Y'
    idToVariable3 = '1h343u1ygb6LejA4_Q63yMqXp4IPtxfvzthlGRWFXAsQ'
    idToVariable4 = '1SeQegOCyBWWymq37oaXc5_Iix-_-tbSdW7QYUyH8_bM'
    idToVariable5 = '1aFD1218D7h86fRFGwartl4xRwRMgaDevKJ2Y7ohUAmQ'
    idToVariable6 = '1nD47ABjCAq5TUmhEP0qaSrPD2_rJzTeFFFzAaLNpqSg'
    idToVariable7 = '1CsKpa30HnmIF_9dgQnwav3j842PJ9vKRZrnCyHYQe5I'

    
    

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
    #curEndYear = input("End Year: ")

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

requests = [
    {
        'replaceAllText':{
            'containsText':{
                'text': '{{NAME}}',
                'matchCase': True
            },
            'replaceText': curName,
        }
    },
    {
        'replaceAllText':{
            'containsText':{
                'text':'{{EMAIL}}',
                'matchCase':True
            },
            'replaceText': curEmail,
        }
    },
    {
        'replaceAllText':{
            'containsText':{
                'text':'{{PHONE}}',
                'matchCase':True
            },
            'replaceText': curNumber,
        }
    },
    {
        'replaceAllText':{
            'containsText':{
                'text':'{{WORK_EXPERIENCE}}',
                'matchCase':True
            },
            'replaceText':work_experience,
        }
    }
]

service_docs.documents().batchUpdate(documentId=doc_id, body ={'requests':requests}).execute()  
exported_resume = service_drive.files().export(fileId=doc_id, mimeType = 'application/pdf').execute()
with open('resume.pdf', 'wb') as f:
            f.write(exported_resume)
    
print("Resume has been exported as 'resume.pdf'")
        

if __name__ == "__main__":
    main()

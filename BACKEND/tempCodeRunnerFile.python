import json
from jinja2 import Environment, FileSystemLoader

class ResumeBuilder:
    def __init__(self):
        self.template_data = {
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

    def get_user_data(self):
        self.template_data["basics"]["name"] = input("Name: ")
        self.template_data["basics"]["email"] = input("Email: ")
        self.template_data["basics"]["phone"] = input("Phone: ")
        self.template_data["basics"]["website"] = input("Website: ")

        # Collect user data for work experience
        num_work_experiences = int(input("Enter the number of work experiences: "))
        for _ in range(num_work_experiences):
            company = input("Company: ")
            position = input("Position: ")
            start_date = input("Start Date: ")
            end_date = input("End Date: ")
            summary = input("Summary: ")
            self.template_data["work"].append({
                "company": company,
                "position": position,
                "startDate": start_date,
                "endDate": end_date,
                "summary": summary
            })

        # Collect user data for education
        num_education_entries = int(input("Enter the number of education entries: "))
        for _ in range(num_education_entries):
            institution = input("Institution: ")
            degree = input("Degree: ")
            end_date = input("End Date: ")
            self.template_data["education"].append({
                "institution": institution,
                "degree": degree,
                "endDate": end_date
            })

        # Collect user data for skills, projects, languages, and experience
        # Add similar sections for these as needed

    def generate_resume(self):
        env = Environment(loader=FileSystemLoader('.'))
        template = env.get_template('resume_template.html')

        # Render the template with the merged JSON data
        html_resume = template.render(self.template_data)

        # Save the HTML to a file
        with open('resume.html', 'w') as html_file:
            html_file.write(html_resume)

    def build_resume(self):
        self.get_user_data()
        self.generate_resume()

if __name__ == "__main__":
    resume_builder = ResumeBuilder()
    resume_builder.build_resume()

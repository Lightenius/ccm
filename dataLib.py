import sqlite3 as sql
import libc

class Database:
    def __init__(self) -> None:
        self.cx = sql.connect("data/occupations.db")
        self.cu = self.cx.cursor()
        

    def skill_str_to_list(self, skills: str) -> list:
        return libc.capitalize_words(skills).split(", ")


    def get_osp_list(self, ospString: str):
        splitted = ospString.lower().split(", ")
        return splitted


    def add_oc(self, name: str, skills: str, description: str, osp: str, credit_rating: str):
        self.cu.execute(f"INSERT INTO jobs (job_name, desc, cr) VALUES (?, ?, ?);", [libc.capitalize_words(name), description, credit_rating])
        skill_list = self.skill_str_to_list(skills)
        self.jobxskill(libc.capitalize_words(name), skillList=skill_list)
        ospList: list= self.get_osp_list(osp)
        
        self.jobxosp(name, ospList=ospList)
        self.cx.commit()
    
    def get_oc_byname(self, name: str):
        for row in self.cu.execute(f"SELECT * FROM jobs WHERE name = '{name}';"):
            return row
        

    def remove_from_list(self, name):
        self.cu.execute(f"DELETE FROM jobs WHERE name = '{name}';")
        self.cx.commit()


    # reading from the sql database with sqlite3 cursor object returns the data as a tuple

    def skillList_of_item(self, name: str):
        tup: tuple = self.read_oc_byname(name=name)
        str_skills: str = tup[2]
        list_skills = str_skills[1:-1].split(",")
        for i in range(len(list_skills)):
            list_skills[i] = list_skills[i].lstrip()
        return list_skills


    def get_oc_list(self):
        oc_names: list = []
        rows = self.cu.execute("SELECT job_name FROM jobs;")
        for row in rows:
            oc_names.append(row[0])
        return oc_names


    def addSkills(self, skills_list: list): # Skill List Should Be in [[skill, bp], [skill, bp]] format
        for skill in skills_list:
            capped = libc.capitalize_words(skill[0])
            bp = skill[1]
            self.cu.execute("INSERT INTO skills (skill_name, skill_bp) VALUES (?, ?);", [capped, bp])
            self.cx.commit()


    def jobxskill(self, jobName: str, skillList: list):
        for skill in skillList:
            self.cu.execute("INSERT INTO jobxskill (job_id, skill_id) VALUES ((SELECT job_id FROM jobs WHERE job_name=?), (SELECT skill_id FROM skills WHERE skill_name=?));", [libc.capitalize_words(jobName), libc.capitalize_words(skill)])
            self.cx.commit()


    def jobxosp(self, jobName: str, ospList: list):
        for osp in ospList:
            self.cu.execute("INSERT INTO jobxosp (job_id, osp_id) VALUES ((SELECT job_id FROM jobs WHERE job_name=?), (SELECT osp_id FROM osps WHERE osp_name=?));", (jobName, osp))
            self.cx.commit()



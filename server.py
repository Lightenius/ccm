from dataLib import Database
import libc

odb = Database()

#odb.add_oc("Accountant", "[Accounting, Law, Library Use, Listen, Persuade, Spot Hidden, +2]", "Either employed within a business or working as a freelanceconsultant with a portfolio of self-employed clientsor businesses. Diligence and an attention to detailmeans that most accountants can make good researchers,being able to support investigationsthrough the careful analysis of personal andbusiness transactions, financial statements,and other records.", "EDUx4", "30-70")


name = "accounTant"

skills = ["Accounting", "Law", "Library Use", "Listen", "Persuade", "Spot Hidden", "+2"]

odb.jobxskill(name, skills)

'SELECT * FROM ((jobs INNER JOIN jobxskill ON jobs.job_id = jobxskill.job_id) INNER JOIN skills ON skills.skill_id=jobxskill.skill_id);'
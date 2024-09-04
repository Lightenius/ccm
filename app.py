from flask import render_template, Flask, request
from dataLib import Database
import libc

app = Flask(__name__)




@app.route("/")
def index():
    return render_template("index.html")


@app.route("/add-oc", methods=["GET", "POST"])
def add_oc():
    if request.method == "POST":
        odb = Database()
        odb.add_oc(libc.capitalize_words(request.form.get("name")), request.form.get("skills"), request.form.get("desc"), request.form.get("osp"), request.form.get("cr"))
        return render_template("add_occupation.html")
    elif request.method == "GET":
        return render_template("add_occupation.html")


@app.route("/occupations")
def list_oc():
    occ = Database()
    names = occ.get_oc_list()
    req_o = request.args.get("o", "boş")
    req_oc = libc.capitalize_words(req_o)
    print(req_o)
    print(req_oc)


    if "boş" == req_o:     
        return render_template("list_occupations.html", occupation_names=names)
    else:
        if req_oc in names:
            selected_occupation = occ.get_oc_byname(req_oc)
            # (id, name, skills, desc, osp, cr)
            return render_template("display_occupation.html", name=selected_occupation[1], skills=selected_occupation[2], desc=selected_occupation[3], osp=selected_occupation[4], cr=selected_occupation[5])
        else:
            return render_template("list_occupations.html", occupation_names=names)
        


if __name__ == "__main__":
    app.run("0.0.0.0", 5515)

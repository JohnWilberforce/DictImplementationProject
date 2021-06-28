from flask import Flask, render_template, request, redirect
from jinja2 import DictLoader

app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        req = request.form
        vehicle_no = req.get("vehicle")  # the key is the name'vehicle' in the
        # home.html forms which returns what user input

        return redirect(request.url)
    return render_template('home.html')


@app.route('/number', methods=["GET", "POST"])
def convert_vehicle_number():
    convert = {

        "AS-2011-16": "0208791000",
        "AS-1336-G": "0549279937",
        "GR-2234-17": "0245085500",
        "AS-9570-19": "0205833163",
        "GS-173-13": "0249980456",
        "AS-6103-21": "0203873924",
        "AS-7489-18": "0203873924",
        "AS-8380-20": "0243983991",
        "GN-4247-18": "0209360390",
        "AS-3337-17": "0247663640",
        "GS-3740-21": "0208791000",
        "GT-8537-17": "0244860484",
        "AS-5001-16": "0242947741",
        "DV-1088C-21": "0208358750",
        "GW-1333-17": "0543052793",
        "AS-8188-14": "0208233439",
        "GR-7590-20": ["0241883090", "John"]
    }

    return convert.get(request.form.get("vehicle").upper(), "NOT FOUND PLEASE TRY AGAIN")


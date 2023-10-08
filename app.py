from flask import Flask,render_template, jsonify

app=Flask(__name__)


JOBS=[
    {
        'Role': 'Software Developer',
        'Location': 'Delhi, India',
        'Company': 'Paypal',
        'Salary': '20,000 INR'
    },
    {
        'Role': 'Software Developer',
        'Location': 'Hyderabad, India',
        'Company': 'Amazon',
        'Salary': '40,000 INR'
    },
    {
        'Role': 'Front End Developer',
        'Location': 'Bengaluru, India',
        'Company': 'Stripe',
        
    },
    {
        'Role': 'SRE',
        'Location': 'Chennai, India',
        'Company': 'Rakuten',
        'Salary': '20,000 INR'
    }
]



@app.route("/")
def home():
    return render_template('base.html',jobs=JOBS)

@app.route("/api/jobs")
def jobs():
    return jsonify(JOBS)


if __name__=="__main__":
    app.run(debug=True)
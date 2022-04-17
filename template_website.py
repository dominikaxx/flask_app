from flask import Flask, render_template
import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('website_home.html', utc_dt=datetime.datetime.utcnow())

@app.route('/about/')
def about():
    return render_template('website_about.html')

@app.route('/articles/')
def articles():
    articles = ['Prvy clanok.',
                'Druhy clanok.',
                'Treti clanok.',
                'Stvrty clanok.'
                ]
    return render_template('website_articles.html', articles = articles)

if __name__ == "__main__":
    app.run(debug=True)




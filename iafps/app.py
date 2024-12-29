from csv_loader import load_schedule_from_csv
from search import search_schedules
from flask import Flask as fs, render_template

app = fs(__name__)
@app.route("/")
@app.route("/home")
def home(): 
 return render_template('home.html')


@app.route("/schedule_filter")
def schedule_filter(): 
 return render_template('schedule_filter.html')

@app.route("/favorites")
def favorites(): 
 return render_template('favorites.html')


@app.route("/about")
def about(): 
 return render_template('about.html')


@app.route("/help")
def help(): 
 return render_template('help.html')

if __name__ == "__main__":
  app.run(debug=True)
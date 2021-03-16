from flask import Flask, render_template
import data

app = Flask(__name__)


@app.route('/')
def render_main():
    return render_template('index.html')


@app.route('/departures/<departure>/')
def render_departures(departure):
    return render_template('departure.html')


@app.route('/tours/<id>/')
def render_tours(id):
    return render_template('tour.html')


@app.route('/data/')
def render_data():
    s_data = '<h1>Все туры:</h1>' + '\n'
    for tour in data.tours:
        s_data += "<p>" + data.tours[tour]['country'] + ': <a href="/data/tours/' + str(tour) + '/">'
        s_data += data.tours[tour]['title'] + " " + data.tours[tour]['stars'] + "*" + " </a> </p>" + '\n'
    return s_data


@app.route('/data/departures/<departure>')
def render_data_departure(departure):
    s_data = '<h1>Туры по направлению ' + data.departures[departure] + ':</h1>' + '\n'
    for tour in data.tours:
        if data.tours[tour]['departure'] == departure:
            s_data += "<p>" + data.tours[tour]['country'] + ': <a href="/tours/' + str(tour) + '/">'
            s_data += data.tours[tour]['title'] + " " + str(data.tours[tour]['price']) + " " + str(data.tours[tour]['stars']) + "* </a> </p>" + '\n'
    #print(s_data)
    return s_data


@app.route('/data/tours/<int:id_tour>/')
def render_data_tour(id_tour):
    my_tour = data.tours[id_tour]
    s_data = '<h1>' + my_tour['country'] + ': ' + my_tour['title'] + ' ' + str(my_tour['price']) + ':' + '</h1>' + '\n'
    s_data += "<p>" + str(my_tour['nights']) + ' ночей</p>' + '\n'
    s_data += "<p>" + 'Стоимость: ' + str(my_tour['price']) + ' Р</p>' + '\n'
    s_data += "<p>" + my_tour['description'] + '</p>'
    return s_data

@app.route('/my/')
def render_my():
    my_user = {'is_logged': True, 'not_logged': False}
    return render_template('my.html', user=my_user, links=links, carriers=carriers)


links = [
  {"title":"Главная","link":"/"},
  {"title":"О Нас","link":"/about/"},
  {"title":"Контакты","link":"/contact/"},
]
positions = [
  {
    "title": "Руководитель отдела web-разработки",
    "salary": "180 000 - 200 000",
    "level":"lead",
    "tags": ["ООП","Git","Flask","Redis","Управление проектами","Управление людьми",
             "Построение команды","Ведение переговоров"],
  },
  {
    "title":"Python Developer",
    "salary":"200 000",
    "level":"middle",
    "tags":["Python","Django","PostgreSQL","Linux","Git"],
  },
  {
    "title":"Python developer",
    "salary":"130 000 - 180 000",
    "level":"middle",
    "tags": ["Django","Python","Flask","PostgreSQL","Высоконагруженные системы","Git","Docker"],
   }
]
carriers = [
  {"name": "American Airlines", "planes": 950, "founded": 1934, "passengers": 193.7},
  {"name": "Lufthansa", "planes": 351, "founded": 1955 , "passengers": 77.5},
  {"name": "Ryanair", "planes": 438, "founded": 1984,  "passengers": 66.5},
  {"name": "Southwest Airlines", "planes": 746,"founded": 1971,"passengers": 101.3},
  {"name": "Delta", "planes": "809", "founded": "1929" , "passengers": 161.1},
]

app.run()

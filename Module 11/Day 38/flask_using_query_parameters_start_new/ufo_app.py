import csv
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>UFO Sightings</title>
        </head>
        <body>
            <h1>Welcome to the UFO Sightings API</h1>
            <p>Use the /sightings route to get UFO sighting data.</p>
        </body>
    </html>
    """

def load_ufo_data(filepath):
    sightings = []
    with open(filepath, mode='r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            sightings.append(row)
    return sightings

@app.route('/ufo_sightings', methods=['GET'])
def get_sightings():
    country = request.args.get('country', '') # this lets us pass in parameters for our function from the address bar. Default is 

    page = int(request.args.get('page', 1)) # looks for a page parameter. Sets it to 1 by default
    per_page = int(request.args.get('per_page', 10)) # looks for a per_page paramter. Sets it to 10 by default

    scrubbed_sightings = load_ufo_data('data/scrubbed.csv')

    # make a copy of our data 
    filtered_sighting = scrubbed_sightings.copy() # makes a complete seprate copy of the data  

    # loop through our original data and remove anything we don't want from the filtered data 
    for sighting in scrubbed_sightings:
        if country and sighting['country'].lower() != country.lower():
            filtered_sighting.remove(sighting) 
    # pagination setup
    start = (page -1) * per_page
    end = start + per_page 

    paged_sightings = filtered_sighting[start:end]
    return jsonify(scrubbed_sightings)

@app.route('/research_stations', methods=['GET'])
def get_research_stations():
    stations = []
    with open('data/research_stations.csv', mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            stations.append(row)
    return jsonify(stations)

@app.route('/add-research-station', methods=['POST'])
def add_research_station():
    data = request.get_json()
    name = data.get('name') 
    location = data.get('location')

    if not name or not location: 
        return jsonify({'error': "Name and location are required"}),400 # throws an error and a 400 - Bad Data error 

    # if we have what we need 
    with open ('data/research_stations.csv') as file:
        fieldnames = ['name','location'] # create our keys 
        writer = csv.DictWriter (file,fieldnames=fieldnames)

        writer.writerow({'name': name,'location': location})

    return jsonify({'message': "Research station added successfully"}), 201  #success response code 
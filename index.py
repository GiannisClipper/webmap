def region(regions, perfecture):
  for k in regions:
    if perfecture in regions[k]['perfectures']:
      return k
  return ''

def create_map():
  regions={'Αν. Μακεδονία και Θράκη':{'population':606170, 'GDP':15272, 'perfectures':'ΕΒΡΟΥ ΡΟΔΟΠΗΣ ΞΑΝΘΗΣ ΚΑΒΑΛΑΣ'},
  'Κεντρική Μακεδονία':{'population':1874590, 'GDP':16559, 'perfectures':'ΔΡΑΜΑΣ ΣΕΡΡΩΝ ΚΙΛΚΙΣ ΠΕΛΛΑΣ ΘΕΣΣΑΛΟΝΙΚΗΣ ΧΑΛΚΙΔΙΚΗΣ ΗΜΑΘΙΑΣ ΠΙΕΡΙΑΣ'},
  '(αυτοδιοικούμενο)':{'population':None, 'GDP':None, 'perfectures':'ΑΓΙΟ ΟΡΟΣ'},
  'Δυτική Μακεδονία':{'population':282120, 'GDP':18786, 'perfectures':'ΦΛΩΡΙΝΑΣ ΚΑΣΤΟΡΙΑΣ ΓΡΕΒΕΝΩΝ ΚΟΖΑΝΗΣ'},
  'Ήπειρος':{'population':336650, 'GDP':14221, 'perfectures':'ΘΕΣΠΡΩΤΙΑΣ ΙΩΑΝΝΙΝΩΝ ΑΡΤΑΣ ΠΡΕΒΕΖΑΣ'},
  'Θεσσαλία':{'population':730730, 'GDP':15772, 'perfectures':'ΚΑΡΔΙΤΣΑΣ ΤΡΙΚΑΛΩΝ ΛΑΡΙΣΑΣ ΜΑΓΝΗΣΙΑΣ'},
  'Ιόνιοι Νήσοι':{'population':206470, 'GDP':17726, 'perfectures':'ΚΕΡΚΥΡΑΣ ΛΕΥΚΑΔΑΣ ΚΕΦΑΛΛΟΝΙΑΣ ΖΑΚΥΝΘΟΥ'},
  'Δυτική Ελλάδα':{'population':680190, 'GDP':14332, 'perfectures':'ΑΙΤΩΛΟΑΚΑΡΝΑΝΙΑΣ ΑΧΑΪΑΣ ΗΛΕΙΑΣ'},
  'Στερεά Ελλάδα':{'population':546870, 'GDP':19007, 'perfectures':'ΕΥΡΥΤΑΝΙΑΣ ΦΩΚΙΔΑΣ ΦΘΙΩΤΙΔΑΣ ΕΥΒΟΙΑΣ ΒΟΙΩΤΙΑΣ'},
  'Αττική':{'population':3812330, 'GDP':26968, 'perfectures':'ΑΘΗΝΩΝ ΑΝΑΤΟΛΙΚΗΣ ΑΤΤΙΚΗΣ ΔΥΤΙΚΗΣ ΑΤΤΙΚΗΣ ΠΕΙΡΑΙΩΣ ΚΑΙ ΝΗΣΩΝ'},
  'Πελοπόννησος':{'population':581980, 'GDP':16580, 'perfectures':'ΚΟΡΙΝΘΟΥ ΑΡΓΟΛΙΔΑΣ ΑΡΚΑΔΙΑΣ ΛΑΚΩΝΙΑΣ ΜΕΣΣΗΝΙΑΣ'},
  'Βόρειο Αιγαίο':{'population':197810, 'GDP':16638, 'perfectures':'ΛΕΣΒΟΥ ΧΙΟΥ ΣΑΜΟΥ'},
  'Νότιο Αιγαίο':{'population':308610, 'GDP':24828, 'perfectures':'ΚΥΚΛΑΔΩΝ ΔΩΔΕΚΑΝΗΣΩΝ'},
  'Κρήτη':{'population':621340, 'GDP':18421, 'perfectures':'ΧΑΝΙΩΝ ΡΕΘΥΜΝΟΥ ΗΡΑΚΛΕΙΟΥ ΛΑΣΙΘΙΟΥ'}}

  import json
  import folium
  
  map=folium.Map(location=(37.94, 23.64), zoom_start=7, tiles='OpenStreetMap')

  lines=folium.FeatureGroup(name='Lines')

  path='webmap/static/'
  stream=open(path+'nomoi.geojson', 'r', encoding='utf-8-sig')
  data=json.load(stream)
  stream.close()

  for x in data['features']:
    print(x['properties']['NAME_GR'])
    #print(type(x['geometry']['coordinates']))
    y={}
    y['type']=x['type']
    y['id']=x['id']
    y['geometry']=x['geometry']
    y['properties']={
        'name':x['properties']['NAME_GR'],
        'capital':x['properties']['EDRA'],
        'region':region(regions, x['properties']['NAME_GR'][3:])}
    lines.add_child(folium.GeoJson(data=y, tooltip=y['properties'], style_function=lambda x:{'fillColor':'red'}))

  map.add_child(lines)
  map.add_child(folium.LayerControl())

  path='webmap/templates/'
  map.save(path+'webmap.html')
  return 'webmap.html'

###############################################################

from flask import Flask, render_template
import os

app=Flask(__name__)

@app.route('/')
def home():
  return 'Webmap home page!!!\n\n'+os.getcwd()

@app.route('/about/')
def about():
  return render_template('about.html')

@app.route('/create/')
def create():
  return render_template(create_map())

if __name__=='__main__':
  app.run(debug=True)

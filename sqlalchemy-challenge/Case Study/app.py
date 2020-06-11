from flask import Flask
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.automap import automap_base
app = Flask(__name__)

engine = create_engine("sqlite:///hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

print('Testing -- looking for the keys(Table)')
print(Base.classes.keys())
print('end test')
conn = engine.connect()
#%%
Measurement = Base.classes.measurement
Station = Base.classes.station 
#%%

app = Flask(__name__)

#%%

@app.route("/")
def welcome():
    return(
        f'/api/v1.0/precipitation'
        f'/api/v1.0/stations'
        f'/api/v1.0/tobs'
        f'/api/v1.0/<start>'
        f'/api/v1.0/<start>/<end>'
        )
        
#%%

@app.route("/api/v1.0/precipitation")
def precipitation():
    result = pd.read_sql("Select data,prcp FROM measurement", engine)
    result_json = result.to_json(orient = 'records')
    return result_json
    
#%%

if __name__ == "__main__":
    app.run(debug=True)
    

from fastapi import FastAPI
app = FastAPI()

# Define Endpoint
@app.get('/')
def read_root():
    return {'message': 'welcome to my fast api app'}

# Define a POST endpoint that asks for a user name
@app.post('/submit-name')
def submit_name(name:str):
    return {'message': f'Hello, {name}!'}
"""
To run: 
"""
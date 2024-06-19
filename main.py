from fastapi import FastAPI, Request, HTTPException, Response
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import threading
from pydantic import BaseModel
import random
import time

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/dist", StaticFiles(directory="dist"), name="static")

list1 = [
    'Banana', 'Unicorn', 'Taco', 'Ninja', 'Penguin', 'Disco', 'Potato', 'Pirate', 
    'Rainbow', 'Moon', 'Zombie', 'Ninja', 'Cheese', 'Galaxy', 'Cookie', 'Dinosaur', 
    'Magic', 'Pancake', 'Laser', 'Dragon', 'Wizard', 'Funky', 'Space', 'Avocado', 
    'Robot', 'Samurai', 'Bubble', 'Bacon', 'Yeti', 'Taco', 'Vampire', 'Pirate', 
    'Banana', 'Disco', 'Unicorn', 'Pizza', 'Cupcake', 'Alien', 'Jello', 'Rocket'
]

list2 = [
    'Party', 'Explosion', 'Dance', 'Adventure', 'Ninja', 'Rain', 'Storm', 'Tornado', 
    'Cheese', 'Galaxy', 'Panda', 'Disco', 'Magic', 'Pancake', 'Laser', 'Dragon', 
    'Wizard', 'Funk', 'Space', 'Avocado', 'Robot', 'Samurai', 'Bubble', 'Bacon', 
    'Yeti', 'Storm', 'Vampire', 'Pirate', 'Unicorn', 'Donut', 'Monkey', 'Disco', 
    'Galaxy', 'Party', 'Explosion', 'Rainbow', 'Adventure', 'Taco', 'Cheese', 'Ninja'
]

status = {'statusText': 'IDLE', 'lastError': random.choice(list2), 'lastTest': "No test was made"}

# def toggle_status(interval):
#     global status
#     while True:
#         status['statusText'] = "IDLE"
#         time.sleep(interval)
#         status['statusText'] = "TESTING"
#         time.sleep(interval)

# toggler_thread = threading.Thread(target=toggle_status, args=(2,), daemon=True)
# toggler_thread.start()

@app.get('/')
async def index():
    return FileResponse(".\dist\index.html")

# Example API endpoint
@app.get('/status')
async def hello():
    global status
    status["lastError"] = random.choice(list2)
    return status
    # return {'statusText': random.choice(list1), 'lastError': random.choice(list2), 'lastTest': "No test was made"}

@app.post('/flag')
async def change_flag(request: Request):
    body = (await request.body()).decode()
    if False:
        # How to return a specific status code -
        return Response(content="Bad", status_code=404)
    print(body)
    return body

@app.get('/scan')
async def start_scan():
    global status
    status["statusText"] = "SCANNING"
    return "Starting"

@app.get('/test')
async def start_test():
    print("hi")
    global status
    status["statusText"] = "TESTING"
    status["lastTest"] = "Meh /:"
    return "Testing"

@app.get('/dev/release-status')
async def _release():
    global status
    status["statusText"] = "IDLE"
    return 'OK'
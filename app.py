from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return app.redirect('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    
@app.route('/home')
def home():
    return '<h1>Home Page</h1>'

@app.route('/about')
def about():
    return '<h1>About Page</h1>'
    
@app.route('/fanyu')
def fanyu():
    return app.redirect('https://fanyu.vercel.app')  
    
if __name__ == '__main__' : 
    app.run(port=3000)
    

from app import app
from .db_access import DbAccess


@app.route('/')
def index():
    return "Home Here"


@app.route('/add', methods=['GET', 'POST'])
def add():
    simple = DbAccess()
    return simple.insert_number("Edward", "0897775555")


@app.route('/remove')
def remove():
    return "Number Removed"

from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

def format_date(value):
    return datetime.strptime(value, "%Y-%m-%d").strftime("%d/%m/%Y")

# Adicionando o filtro format_date ao ambiente do Jinja2
app.jinja_env.filters['format_date'] = format_date

loans = [
    {
        "id": 1,
        "name": "João",
        "book": "Aventuras de Tom Sawyer",
        "curse": "Técnico em Informática",
        "loan": "2024-02-01",
        "devolution": "2024-02-15"
    },
    {
        "id": 2,
        "name": "Maria",
        "book": "Nieztsche",
        "curse": "Técnico em Informática",
        "loan": "2024-01-15",
        "devolution": "2024-02-10"
    }
]

@app.route('/')
def index():
    return render_template('index.html', loans=loans)

@app.route('/add')
def add():
    return render_template('add.html')

@app.route('/add_loan', methods=['POST'])
def add_loan():
    name = request.form['name']
    book = request.form['book']
    curse = request.form['curse']
    loan_date = request.form['loan']
    devolution = request.form['devolution']

    loan = {
        "id": len(loans) + 1,  # Gerar ID automático (só funciona para este exemplo)
        "name": name,
        "book": book,
        "curse": curse,
        "loan": loan_date,
        "devolution": devolution
    }
    loans.append(loan)
    return redirect(url_for('index'))

@app.route('/delete_loan/<int:id>', methods=['GET'])
def delete_loan(id):
    for loan in loans:
        if loan['id'] == id:
            loans.remove(loan)
            break
    return redirect(url_for('index'))

@app.route('/edit/<int:id>')
def edit(id):
    edit_data = []
    for loan in loans:
        if loan['id'] == id:
            name = loan['name']
            book = loan['book']
            curse = loan['curse']
            loan_date = loan['loan']
            devolution = loan['devolution']

            edit_data.append(id)
            edit_data.append(name)
            edit_data.append(book)
            edit_data.append(curse)
            edit_data.append(loan_date)
            edit_data.append(devolution)
        
    return render_template('edit.html', data=edit_data)

@app.route('/edit_loan', methods=['POST'])
def edit_loan():
    id = int(request.form['id'])
    name = request.form['name']
    book = request.form['book']
    curse = request.form['curse']
    loan_date = request.form['loan']
    devolution = request.form['devolution']


    for loan in loans:
        print(loan['id'])
        print(id)
        if loan['id'] == id:
            print(loan)
            loan['name'] = name
            loan['book'] = book
            loan['curse'] = curse
            loan['loan'] = loan_date
            loan['devolution'] = devolution

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)

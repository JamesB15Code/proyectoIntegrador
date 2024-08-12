from flask import Flask, request, render_template, redirect, url_for, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'mi_secreto'  # Cambia esto por una clave secreta segura

@app.route('/')
def home():
     return render_template('formulario.html')

@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        user_id = request.form['user_id']
        correo = request.form['correo']
        product_id = request.form['product_id']
        product_name = request.form['product_name']
        purchase_date = request.form['purchase_date']

        if not user_id or not correo or not product_id or not product_name or not purchase_date:
            flash('Todos los campos son obligatorios', 'error')
        else:
            flash(f'Formulario enviado con éxito para el usuario {user_id} y el producto {product_name}', 'success')
            return redirect(url_for('form'))

    return render_template('formulario.html')

if __name__ == '__main__':
    app.run(debug=True)

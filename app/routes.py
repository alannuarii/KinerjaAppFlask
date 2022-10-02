from app import app
from flask import render_template, request, redirect
import pandas as pd
from db import conn

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            kinerja = request.files['kinerja']
            if not kinerja.filename.endswith('xlsx'):
                print('File harus format xlsx')
                return redirect('/')

            import_xlsx = pd.read_excel(kinerja)
            for i in range(len(import_xlsx)):
                base_command = ("INSERT INTO unit(nama_unit) VALUES('{value_nama_unit}')")
                insert_db = base_command.format(value_nama_unit=import_xlsx['nama_unit'][i])
                conn.cur.execute(insert_db)
                conn.conn.commit()
            conn.cur.close()
        except Exception as error:
            print(error)

    return render_template('index.html', title="Input Kinerja")
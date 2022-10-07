import imp
from app import app
from flask import render_template, request, redirect
from app.conn import conn, cur
from app.kinerja import Kinerja
import pandas as pd

@app.route('/', methods=['GET','POST'])
def index():
    if request.method == 'POST':
        try:
            if 'unit' in request.files:
                unit = request.files['unit']
                if unit.filename != 'unit.xlsx':
                    print('File tidak sesuai')

                import_xlsx = pd.read_excel(unit)
                for i in range(len(import_xlsx)):
                    base_command = ("INSERT INTO unit(nama_unit) VALUES('{nama_unit}')")
                    insert_db = base_command.format(nama_unit=import_xlsx['nama_unit'][i])
                    conn.cur.execute(insert_db)
                    conn.conn.commit()
                conn.cur.close()

            elif 'spesifikasi' in request.files:
                spesifikasi = request.files['spesifikasi']
                if spesifikasi.filename != 'spesifikasi.xlsx':
                    print('File tidak sesuai')

                import_xlsx = pd.read_excel(spesifikasi)
                for i in range(len(import_xlsx)):
                    base_command = ("INSERT INTO spesifikasi(unit, nama_mesin, tipe_mesin, serial_number, tahun_operasi, dtp, dmn, unit_id) VALUES('{unit}', '{nama_mesin}', '{tipe_mesin}', '{serial_number}', '{tahun_operasi}', {dtp}, {dmn}, {unit_id})")
                    insert_db = base_command.format(unit=import_xlsx['unit'][i], nama_mesin=import_xlsx['nama_mesin'][i], tipe_mesin=import_xlsx['tipe_mesin'][i], serial_number=import_xlsx['serial_number'][i], tahun_operasi=import_xlsx['tahun_operasi'][i], dtp=import_xlsx['dtp'][i], dmn=import_xlsx['dmn'][i], unit_id=import_xlsx['unit_id'][i])
                    conn.cur.execute(insert_db)
                    conn.conn.commit()
                conn.cur.close()                

            elif 'pengusahaan' in request.files:
                pengusahaan = request.files['pengusahaan']
                if pengusahaan.filename != 'pengusahaan.xlsx':
                    print('File tidak sesuai')

                import_xlsx = pd.read_excel(pengusahaan)
                for i in range(len(import_xlsx)):
                    base_command = ("INSERT INTO pengusahaan(periode, produksi, ps_sentral, ps_trafo, bbm, batubara, po, mo, fo, fo_omc, sh, ph, epdh, eudh, esdh, efdhrs, trip_internal, trip_eksternal, spesifikasi_id) VALUES('{periode}', {produksi}, {ps_sentral}, {ps_trafo}, {bbm}, {batubara}, {po}, {mo}, {fo}, {fo_omc}, {sh}, {ph}, {epdh}, {eudh}, {esdh}, {efdhrs}, {trip_internal}, {trip_eksternal}, {spesifikasi_id})")
                    insert_db = base_command.format(periode=import_xlsx['periode'][i], produksi=import_xlsx['produksi'][i], ps_sentral=import_xlsx['ps_sentral'][i], ps_trafo=import_xlsx['ps_trafo'][i], bbm=import_xlsx['bbm'][i], batubara=import_xlsx['batubara'][i], po=import_xlsx['po'][i], mo=import_xlsx['mo'][i], fo=import_xlsx['fo'][i], fo_omc=import_xlsx['fo_omc'][i], sh=import_xlsx['sh'][i], ph=import_xlsx['ph'][i], epdh=import_xlsx['epdh'][i], eudh=import_xlsx['eudh'][i], esdh=import_xlsx['esdh'][i], efdhrs=import_xlsx['efdhrs'][i], trip_internal=import_xlsx['trip_internal'][i], trip_eksternal=import_xlsx['trip_eksternal'][i], spesifikasi_id=import_xlsx['spesifikasi_id'][i])
                    conn.cur.execute(insert_db)
                    conn.conn.commit()
                conn.cur.close()
            
        except Exception as error:
            print(error)

    return render_template('index.html', title="Input Kinerja")


@app.route('/kinerja')
def kinerja():
    querystring = request.args.get('spesifikasi_id')
    querystring2 = request.args.get('periode')
    data = Kinerja().eaf_bulanan(querystring, querystring2)
    return data
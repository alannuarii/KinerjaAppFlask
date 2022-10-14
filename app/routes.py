from app import app
from flask import render_template, request, redirect
from app.conn import conn, cur
from app.kinerja import Kinerja
from app.utils import get_month, months
import pandas as pd

@app.route('/', methods=['GET','POST'])
def index():
    units = Kinerja().nama_unit()
    mesins = Kinerja().spesifikasi()
    years = Kinerja().get_years()
    result_mesin = None
    result_unit = None
    data1 = None
    satuan = None
    active_mesin = 'active'
    active_unit = None

    if 'id_mesin' in request.args:
        keys = request.args.keys()
        query1 = request.args.get('id_mesin')
        query2 = request.args.get('month')
        query3 = request.args.get('year')
        query4 = request.args.get('kpi')
        periode = f'{query3}-{get_month(query2)}'

        result_kpi = Kinerja().select_kpi_mesin(query4, query1, periode, list(keys)[3])
        result_mesin = round(result_kpi[0], 2)
        data1 = int(query1) - 1
        satuan = Kinerja().satuan(query4)
        active_mesin = 'active'

    if 'id_unit' in request.args:
        keys = request.args.keys()
        query1 = request.args.get('id_unit')
        query2 = request.args.get('month')
        query3 = request.args.get('year')
        query4 = request.args.get('kpi')
        periode = f'{query3}-{get_month(query2)}'

        result_kpi = Kinerja().select_kpi_mesin(query4, query1, periode, list(keys)[3])
        result_unit = round(result_kpi[0], 2)
        data1 = int(query1) - 1
        satuan = Kinerja().satuan(query4)
        active_unit = 'active'
        active_mesin = None
        
    return render_template('pages/index.html', title='Kinerja Pembangkit', units=units, mesins=mesins, result_mesin=result_mesin, result_unit=result_unit, months=months, years=years, all_kpi=Kinerja().kpi, data1=data1, satuan=satuan,active_mesin=active_mesin, active_unit=active_unit)

@app.route('/input', methods=['GET','POST'])
def input():
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
                    cur.execute(insert_db)
                    conn.commit()
                cur.close()

            elif 'spesifikasi' in request.files:
                spesifikasi = request.files['spesifikasi']
                if spesifikasi.filename != 'spesifikasi.xlsx':
                    print('File tidak sesuai')

                import_xlsx = pd.read_excel(spesifikasi)
                for i in range(len(import_xlsx)):
                    base_command = ("INSERT INTO spesifikasi(unit, nama_mesin, tipe_mesin, serial_number, tahun_operasi, dtp, unit_id) VALUES('{unit}', '{nama_mesin}', '{tipe_mesin}', '{serial_number}', '{tahun_operasi}', {dtp}, {unit_id})")
                    insert_db = base_command.format(unit=import_xlsx['unit'][i], nama_mesin=import_xlsx['nama_mesin'][i], tipe_mesin=import_xlsx['tipe_mesin'][i], serial_number=import_xlsx['serial_number'][i], tahun_operasi=import_xlsx['tahun_operasi'][i], dtp=import_xlsx['dtp'][i], unit_id=import_xlsx['unit_id'][i])
                    cur.execute(insert_db)
                    conn.commit()
                cur.close()                

            elif 'pengusahaan' in request.files:
                pengusahaan = request.files['pengusahaan']
                if pengusahaan.filename != 'pengusahaan.xlsx':
                    print('File tidak sesuai')

                import_xlsx = pd.read_excel(pengusahaan)
                for i in range(len(import_xlsx)):
                    base_command = ("INSERT INTO pengusahaan(periode, produksi, ps_sentral, ps_trafo, bbm, batubara, po, mo, fo, fo_omc, sh, ph, epdh, eudh, esdh, efdhrs, trip_internal, trip_eksternal, spesifikasi_id, dtp, dmn) VALUES('{periode}', {produksi}, {ps_sentral}, {ps_trafo}, {bbm}, {batubara}, {po}, {mo}, {fo}, {fo_omc}, {sh}, {ph}, {epdh}, {eudh}, {esdh}, {efdhrs}, {trip_internal}, {trip_eksternal}, {spesifikasi_id}, {dtp}, {dmn})")
                    insert_db = base_command.format(periode=import_xlsx['periode'][i], produksi=import_xlsx['produksi'][i], ps_sentral=import_xlsx['ps_sentral'][i], ps_trafo=import_xlsx['ps_trafo'][i], bbm=import_xlsx['bbm'][i], batubara=import_xlsx['batubara'][i], po=import_xlsx['po'][i], mo=import_xlsx['mo'][i], fo=import_xlsx['fo'][i], fo_omc=import_xlsx['fo_omc'][i], sh=import_xlsx['sh'][i], ph=import_xlsx['ph'][i], epdh=import_xlsx['epdh'][i], eudh=import_xlsx['eudh'][i], esdh=import_xlsx['esdh'][i], efdhrs=import_xlsx['efdhrs'][i], trip_internal=import_xlsx['trip_internal'][i], trip_eksternal=import_xlsx['trip_eksternal'][i], spesifikasi_id=import_xlsx['spesifikasi_id'][i], dtp=import_xlsx['dtp'][i], dmn=import_xlsx['dmn'][i])
                    cur.execute(insert_db)
                    conn.commit()
                cur.close()

            elif 'kalori' in request.files:
                kalori = request.files['kalori']
                if kalori.filename != 'kalori.xlsx':
                    print('File tidak sesuai')

                import_xlsx = pd.read_excel(kalori)
                for i in range(len(import_xlsx)):
                    base_command = ("INSERT INTO kalori(kalori_bb, kalori_bbm, kalori_fame, pengusahaan_id) VALUES('{kalori_bb}', {kalori_bbm}, {kalori_fame}, {pengusahaan_id})")
                    insert_db = base_command.format(kalori_bb=import_xlsx['kalori_bb'][i], kalori_bbm=import_xlsx['kalori_bbm'][i], kalori_fame=import_xlsx['kalori_fame'][i], pengusahaan_id=import_xlsx['pengusahaan_id'][i])
                    cur.execute(insert_db)
                    conn.commit()
                cur.close()
            
        except Exception as error:
            print(error)

    return render_template('pages/input.html', title="Input Kinerja")



import mysql.connector

conn = mysql.connector.connect(host='localhost',
                               database='kinerja_kit',
                               user='root',
                               password='1sampai8')
cur = conn.cursor()


# CREATE TABLE spesifikasi
# (
#     id INT NOT NULL AUTO_INCREMENT,
#     unit VARCHAR(2) NOT NULL,
#     nama_mesin VARCHAR(50) NOT NULL,
#     tipe_mesin VARCHAR(50),
#     serial_number VARCHAR(50),
#     tahun_operasi VARCHAR(4),
#     dtp INT NOT NULL,
#     unit_id INT NOT NULL,
#     PRIMARY KEY (id),
#     CONSTRAINT fk_spesifikasi_unit FOREIGN KEY (unit_id) REFERENCES unit (id)
# );

# CREATE TABLE pengusahaan
# (
#     id INT NOT NULL AUTO_INCREMENT,
#     periode VARCHAR(7) NOT NULL,
#     dtp INT NOT NULL,
#     dmn INT NOT NULL,
#     produksi FLOAT,
#     ps_sentral FLOAT,
#     ps_trafo FLOAT,
#     bbm FLOAT,
#     batubara FLOAT,
#     po FLOAT NOT NULL,
#     mo FLOAT NOT NULL,
#     fo FLOAT NOT NULL,
#     fo_omc FLOAT NOT NULL,
#     sh FLOAT NOT NULL,
#     ph FLOAT NOT NULL,
#     epdh FLOAT,
#     eudh FLOAT,
#     esdh FLOAT,
#     efdhrs FLOAT,
#     trip_internal INT,
#     trip_eksternal INT,
#     spesifikasi_id INT NOT NULL,
#     PRIMARY KEY (id),
#     CONSTRAINT fk_pengusahaan_spesifikasi FOREIGN KEY (spesifikasi_id) REFERENCES spesifikasi (id)
# );

# CREATE TABLE kalori
# (
#     id INT NOT NULL AUTO_INCREMENT,
#     kalori_bb FLOAT,
#     kalori_bbm FLOAT,
#     kalori_fame FLOAT,
#     pengusahaan_id INT NOT NULL,
#     PRIMARY KEY (id),
#     CONSTRAINT fk_kalori_pengusahaan FOREIGN KEY (pengusahaan_id) REFERENCES pengusahaan (id)
# );
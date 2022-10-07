from app.conn import cur

class Kinerja:
    def nama_unit(self):
        cur.execute("SELECT * FROM unit;")
        result = cur.fetchall()
        return result

    def spesifikasi(self):
        cur.execute("SELECT * FROM spesifikasi;")
        result = cur.fetchall()
        return result

    def eaf_bulanan(sefl, spesifikasi_id, periode):
        query = "SELECT ((sh + (ph - ((po + mo + fo) + sh)) - (epdh + eudh + esdh)) / ph * 100) AS 'EAF' FROM pengusahaan WHERE spesifikasi_id = {spesifikasi_id} AND periode = {periode}"
        cur.execute(query.format(spesifikasi_id=spesifikasi_id, periode=periode))
        result = cur.fetchall()
        return result

    def efor_bulanan(self):
        pass
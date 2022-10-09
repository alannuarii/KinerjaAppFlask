from app.conn import cur

class Kinerja:
    kpi = ['EAF', 'EFOR', 'SOF', 'CF', 'SdOF', 'PS', 'SFC']
    rsh = '(ph - ((po + mo + fo) + sh))'
    total_derating = '(epdh + eudh + esdh)'
    total_ps = '(ps_sentral + ps_trafo)'
    produksi_netto = f'(produksi - {total_ps})'
    dtp_ph = '(dtp * ph)'
    dmn_ph = '(dmn * ph)'
    dmn_ph_der = f'(dmn * (sh + {rsh} - {total_derating}))'
    dmn_fo_eudh = '(dmn * (fo + eudh))'
    dmn_fo_sh_efdhrs = '(dmn * (fo + sh + efdhrs))'
    dmn_har = '(dmn * (po + mo))'
    sdof = 'trip_internal'

    def select_kpi_mesin(self, kpi, id, periode, key):
        if kpi == 'EAF':
            if key == 'id_mesin':
                return self.eaf_mesin(id, periode)
            if key == 'id_unit':
                return self.eaf_unit(id, periode)
        elif kpi == 'EFOR':
            if key == 'id_mesin':
                return self.efor_mesin(id, periode)
            if key == 'id_unit':
                return self.efor_unit(id, periode)
        elif kpi == 'SOF':
            if key == 'id_mesin':
                return self.sof_mesin(id, periode)
            if key == 'id_unit':
                return self.sof_unit(id, periode)
        elif kpi == 'CF':
            if key == 'id_mesin':
                return self.cf_mesin(id, periode)
            if key == 'id_unit':
                return self.cf_unit(id, periode)
        elif kpi == 'SdOF':
            if key == 'id_mesin':
                return self.sdof_mesin(id, periode)
            if key == 'id_unit':
                return self.sdof_unit(id, periode)
        elif kpi == 'PS':
            if key == 'id_mesin':
                return self.ps_mesin(id, periode)
            if key == 'id_unit':
                return self.ps_unit(id, periode)
        elif kpi == 'SFC':
            if key == 'id_mesin':
                return self.sfc_mesin(id, periode)
            if key == 'id_unit':
                return self.sfc_unit(id, periode)

    def satuan(self, kpi):
        if kpi in ['EAF', 'EFOR', 'SOF', 'CF', 'PS']:
            return '%'
        elif kpi == 'SdOF':
            return 'Kali'
        elif kpi == 'SFC':
            return 'Liter/kWh'

    def get_years(self):
        cur.execute("SELECT DISTINCT(periode) FROM pengusahaan;")
        query_result = cur.fetchall()
        list_result = []
        for i in range(len(query_result)):
            result = query_result[i][0][:-3]
            list_result.append(result)
        return list(set(list_result))

    def nama_unit(self):
        cur.execute("SELECT * FROM unit;")
        result = cur.fetchall()
        return result

    def spesifikasi(self):
        cur.execute("SELECT * FROM spesifikasi JOIN unit ON spesifikasi.unit_id = unit.id;")
        result = cur.fetchall()
        return result

    def eaf(self):
        rumus = '((sh + {rsh} - {total_derating}) / ph * 100)'
        return rumus.format(rsh = self.rsh, total_derating=self.total_derating)

    def efor(self):
        rumus = '((fo + eudh) / (fo + sh + efdhrs) * 100)'
        return rumus

    def sof(self):
        rumus = '((po + mo) / ph * 100)'
        return rumus

    def cf(self):
        rumus = '(produksi / {dtp_ph} * 100)'
        return rumus.format(dtp_ph=self.dtp_ph)

    def ps(self):
        rumus = '({total_ps} / produksi * 100)'
        return rumus.format(total_ps=self.total_ps)

    def sfc(self):
        rumus = '(bbm / produksi)'
        return rumus

    def eaf_mesin(self, spesifikasi_id, periode):
        query = "SELECT {eaf} FROM pengusahaan WHERE spesifikasi_id = {spesifikasi_id} AND periode = '{periode}'"
        cur.execute(query.format(eaf=self.eaf(), spesifikasi_id=spesifikasi_id, periode=periode))
        result = cur.fetchone()
        return result

    def efor_mesin(self, spesifikasi_id, periode):
        query = "SELECT {efor} FROM pengusahaan WHERE spesifikasi_id = {spesifikasi_id} AND periode = '{periode}'"
        cur.execute(query.format(efor=self.efor(), spesifikasi_id=spesifikasi_id, periode=periode))
        result = cur.fetchone()
        return result

    def sof_mesin(self, spesifikasi_id, periode):
        query = "SELECT {sof} FROM pengusahaan WHERE spesifikasi_id = {spesifikasi_id} AND periode = '{periode}'"
        cur.execute(query.format(sof=self.sof(), spesifikasi_id=spesifikasi_id, periode=periode))
        result = cur.fetchone()
        return result

    def cf_mesin(self, spesifikasi_id, periode):
        query = "SELECT {cf} FROM pengusahaan WHERE spesifikasi_id = {spesifikasi_id} AND periode = '{periode}'"
        cur.execute(query.format(cf=self.cf(), spesifikasi_id=spesifikasi_id, periode=periode))
        result = cur.fetchone()
        return result

    def sdof_mesin(self, spesifikasi_id, periode):
        query = "SELECT {sdof} FROM pengusahaan WHERE spesifikasi_id = {spesifikasi_id} AND periode = '{periode}'"
        cur.execute(query.format(sdof=self.sdof, spesifikasi_id=spesifikasi_id, periode=periode))
        result = cur.fetchone()
        return result

    def ps_mesin(self, spesifikasi_id, periode):
        query = "SELECT {ps} FROM pengusahaan WHERE spesifikasi_id = {spesifikasi_id} AND periode = '{periode}'"
        cur.execute(query.format(ps=self.ps(), spesifikasi_id=spesifikasi_id, periode=periode))
        result = cur.fetchone()
        return result

    def sfc_mesin(self, spesifikasi_id, periode):
        query = "SELECT {sfc} FROM pengusahaan WHERE spesifikasi_id = {spesifikasi_id} AND periode = '{periode}'"
        cur.execute(query.format(sfc=self.sfc(), spesifikasi_id=spesifikasi_id, periode=periode))
        result = cur.fetchone()
        return result

    def eaf_unit(self, unit_id, periode):
        query = "SELECT (SUM({dmn_ph_der}) / SUM({dmn_ph}) * 100) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE unit_id = {unit_id} AND periode = '{periode}';"
        cur.execute(query.format(dmn_ph_der=self.dmn_ph_der, dmn_ph=self.dmn_ph, unit_id=unit_id, periode=periode))
        result = cur.fetchone()
        return result

    def efor_unit(self, unit_id, periode):
        query = "SELECT (SUM({dmn_fo_eudh}) / SUM({dmn_fo_sh_efdhrs}) * 100) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE unit_id = {unit_id} AND periode = '{periode}';"
        cur.execute(query.format(dmn_fo_eudh=self.dmn_fo_eudh, dmn_fo_sh_efdhrs=self.dmn_fo_sh_efdhrs, unit_id=unit_id, periode=periode))
        result = cur.fetchone()
        return result

    def sof_unit(self, unit_id, periode):
        query = "SELECT (SUM({dmn_har}) / SUM({dmn_ph}) * 100) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE unit_id = {unit_id} AND periode = '{periode}';"
        cur.execute(query.format(dmn_har=self.dmn_har, dmn_ph=self.dmn_ph, unit_id=unit_id, periode=periode))
        result = cur.fetchone()
        return result

    def cf_unit(self, unit_id, periode):
        query = "SELECT (SUM(produksi) / SUM({dtp_ph}) * 100) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE unit_id = {unit_id} AND periode = '{periode}';"
        cur.execute(query.format(dtp_ph=self.dtp_ph, unit_id=unit_id, periode=periode))
        result = cur.fetchone()
        return result

    def sdof_unit(self, unit_id, periode):
        query = "SELECT (SUM({sdof}) / COUNT(*)) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE unit_id = {unit_id} AND periode = '{periode}';"
        cur.execute(query.format(sdof=self.sdof, unit_id=unit_id, periode=periode))
        result = cur.fetchone()
        return result

    def ps_unit(self, unit_id, periode):
        query = "SELECT (SUM({total_ps}) / SUM(produksi) * 100) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE unit_id = {unit_id} AND periode = '{periode}';"
        cur.execute(query.format(total_ps=self.total_ps, unit_id=unit_id, periode=periode))
        result = cur.fetchone()
        return result

    def sfc_unit(self, unit_id, periode):
        query = "SELECT (SUM(bbm) / SUM(produksi)) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE unit_id = {unit_id} AND periode = '{periode}';"
        cur.execute(query.format(unit_id=unit_id, periode=periode))
        result = cur.fetchone()
        return result

    def eaf_bulanan(self, periode):
        query = "SELECT (SUM({dmn_ph_der}) / SUM({dmn_ph}) * 100) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE periode = '{periode}';"
        cur.execute(query.format(dmn_ph_der=self.dmn_ph_der, dmn_ph=self.dmn_ph, periode=periode))
        result = cur.fetchone()
        return result

    def efor_bulanan(self, periode):
        query = "SELECT (SUM({dmn_fo_eudh}) / SUM({dmn_fo_sh_efdhrs}) * 100) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE periode = '{periode}';"
        cur.execute(query.format(dmn_fo_eudh=self.dmn_fo_eudh, dmn_fo_sh_efdhrs=self.dmn_fo_sh_efdhrs, periode=periode))
        result = cur.fetchone()
        return result

    def sof_bulanan(self, periode):
        query = "SELECT (SUM({dmn_har}) / SUM({dmn_ph}) * 100) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE periode = '{periode}';"
        cur.execute(query.format(dmn_har=self.dmn_har, dmn_ph=self.dmn_ph, periode=periode))
        result = cur.fetchone()
        return result

    def cf_bulanan(self, periode):
        query = "SELECT (SUM(produksi) / SUM({dtp_ph}) * 100) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE periode = '{periode}';"
        cur.execute(query.format(dtp_ph=self.dtp_ph, periode=periode))
        result = cur.fetchone()
        return result

    def sdof_bulanan(self, periode):
        query = "SELECT (SUM({sdof}) / COUNT(*)) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE periode = '{periode}';"
        cur.execute(query.format(sdof=self.sdof, periode=periode))
        result = cur.fetchone()
        return result

    def ps_bulanan(self, periode):
        query = "SELECT (SUM({total_ps}) / SUM(produksi) * 100) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE periode = '{periode}';"
        cur.execute(query.format(total_ps=self.total_ps, periode=periode))
        result = cur.fetchone()
        return result

    def sfc_bulanan(self, periode):
        query = "SELECT (SUM(bbm) / SUM(produksi)) FROM pengusahaan JOIN spesifikasi ON pengusahaan.spesifikasi_id = spesifikasi.id JOIN unit ON spesifikasi.unit_id = unit.id WHERE periode = '{periode}';"
        cur.execute(query.format(periode=periode))
        result = cur.fetchone()
        return result
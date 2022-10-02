from db.engine import Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

class Unit(Base):
    __tablename__ = 'unit'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nama_unit = Column(String(20), nullable=False)
    spesifikasis = relationship('Spesifikasi', backref='unit_kit', cascade="all, delete-orphan")

    def __repr__(self):
        return self.nama_unit


class Spesifikasi(Base):
    __tablename__ = 'spesifikasi'
    id = Column(Integer, primary_key=True, autoincrement=True)
    unit = Column(String(2), nullable=False)
    nama_mesin = Column(String(30), nullable=False)
    tipe_mesin = Column(String(30))
    serial_number = Column(String(30))
    tahun_operasi = Column(String(4))
    dtp = Column(Integer, nullable=False)
    dmn = Column(Integer, nullable=False)
    unit_id = Column(Integer, ForeignKey('unit.id'))
    pengusahaans = relationship('Pengusahaan', backref='spesifikasi', cascade="all, delete-orphan")

    def __repr__(self):
        return f"Unit {self.unit} {self.nama_mesin}"


class Pengusahaan(Base):
    __tablename__ = 'pengusahaan'
    id = Column(Integer, primary_key=True, autoincrement=True)
    periode = Column(String(10), nullable=False)
    produksi = Column(Float, default=0)
    ps_sentral = Column(Float, default=0)
    ps_trafo = Column(Float, default=0)
    bbm = Column(Float, default=0)
    batubara = Column(Float, default=0)
    po = Column(Float, default=0)
    mo = Column(Float, default=0)
    fo = Column(Float, default=0)
    fo_omc = Column(Float, default=0)
    sh = Column(Float, default=0)
    rsh = Column(Float, default=0)
    ph = Column(Float, default=0)
    epdh = Column(Float, default=0)
    eudh = Column(Float, default=0)
    esdh = Column(Float, default=0)
    efdhrs = Column(Float, default=0)
    trip_internal = Column(Integer, default=0)
    trip_eksternal = Column(Integer, default=0)
    spesifikasi_id = Column(Integer, ForeignKey('spesifikasi.id'))

    def __repr__(self):
        return self.periode


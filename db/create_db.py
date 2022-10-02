from db.engine import Base, engine
from app.models import Unit, Spesifikasi, Pengusahaan


print('Creating database')

Base.metadata.create_all(engine)

print('Success')
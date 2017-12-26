from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import MetaData

metadata = MetaData(schema="gigsvc")
db = SQLAlchemy(metadata=metadata)
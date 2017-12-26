from structlog import get_logger
from sqlalchemy.exc import SQLAlchemyError

from gigdb.models.bands import Band
from gigdb.models import db

logger = get_logger()


def get_bands():
    bands = db.session.query(Band).all()

    if bands:
        return [band.to_dict() for band in bands]

    logger.info('Attempted to retrieve bands when none in database')


def _get_band(band_name):
    try:
        return db.session.query(Band).filter(Band.name == band_name).first()
    except SQLAlchemyError:
        logger.exception('Unable to retrieve band', band_name=band_name)
        raise DatabaseError(f'Unable to retrieve band: {band_name}', status_code=500)


def create_band(band_name):    
    logger.info(f'Creating band: {band_name}')

    existing_band = _get_band(band_name)

    if existing_band:
        logger.info('Creating a band with an existing name',
                    band_name=band_name)

    band = Band(name=band_name)

    db.session.add(band)

    logger.info('Created new band', band_name=band_name)

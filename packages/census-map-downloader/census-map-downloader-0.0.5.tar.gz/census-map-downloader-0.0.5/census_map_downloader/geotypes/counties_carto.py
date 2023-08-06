#! /usr/bin/env python
# -*- coding: utf-8 -*-
import collections
from census_map_downloader.base import BaseDownloader

# Logging
import logging
logger = logging.getLogger(__name__)


class CountiesCartoDownloader2018(BaseDownloader):
    """
    Download 2018 cartographic counties.
    """
    PROCESSED_NAME = "counties_carto_2018"
    # Docs (https://www2.census.gov/geo/tiger/GENZ2018/2018_file_name_def.pdf?#)
    FIELD_CROSSWALK = collections.OrderedDict({
        "STATEFP": "state_fips",
        "COUNTYFP": "county_fips",
        "GEOID": "geoid",
        "NAME": "county_name",
        "geometry": "geometry",
        "ALAND": "land_area",
        "AWATER": "water_area"
    })

    @property
    def url(self):
        return "https://www2.census.gov/geo/tiger/GENZ2018/shp/cb_2018_us_county_500k.zip"

    @property
    def zip_name(self):
        return f"cb_2018_us_county_500k.zip"

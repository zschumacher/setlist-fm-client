import datetime
import typing
from decimal import Decimal

import humps
from pydantic import BaseModel
from pydantic import HttpUrl
from pydantic import validator


class SetlistFmBaseModel(BaseModel):
    class Config:
        alias_generator = humps.camelize


class Artist(SetlistFmBaseModel):
    mbid: str
    name: str
    sort_name: str
    disambiguation: typing.Optional[str]
    url: HttpUrl


class Coordinates(SetlistFmBaseModel):
    lat: Decimal
    long: Decimal


class Country(SetlistFmBaseModel):
    code: str
    name: str


class City(SetlistFmBaseModel):
    id: str
    name: str
    state: str
    state_code: str
    coords: Coordinates
    country: Country


class Venue(SetlistFmBaseModel):
    id: str
    name: str
    city: City
    url: HttpUrl


class Tour(SetlistFmBaseModel):
    name: str


class Song(SetlistFmBaseModel):
    name: str
    info: typing.Optional[str]
    cover: typing.Optional[Artist]


class Set(SetlistFmBaseModel):
    song: typing.List[Song]
    encore: typing.Optional[int]


class SetList(SetlistFmBaseModel):
    set: typing.List[Set]


class User(SetlistFmBaseModel):
    user_id: str
    full_name: typing.Optional[str]
    last_fm: typing.Optional[int]
    my_space: typing.Optional[str]
    twitter: typing.Optional[str]
    flickr: typing.Optional[str]
    website: typing.Optional[str]
    about: typing.Optional[str]
    url: HttpUrl


class ArtistSetList(SetlistFmBaseModel):
    id: str
    version_id: str
    event_date: datetime.date
    last_updated: datetime.datetime
    artist: Artist
    venue: Venue
    tour: typing.Optional[Tour]
    info: typing.Optional[str]
    url: HttpUrl
    sets: SetList

    @validator("event_date", pre=True)
    def parse_event_date(cls, value):
        return datetime.datetime.strptime(value, "%d-%m-%Y").date()


class PagedResponseBaseModel(SetlistFmBaseModel):
    type: str
    items_per_page: int
    page: int
    total: int


class ArtistSetListResponse(PagedResponseBaseModel):
    setlist: typing.List[ArtistSetList]


class ArtistSearchResponse(PagedResponseBaseModel):
    artist: typing.List[Artist]


class CitiesSearchResponse(PagedResponseBaseModel):
    cities: typing.List[City]


class CountrySearchResponse(PagedResponseBaseModel):
    country: typing.List[Country]


class VenueSearchResponse(PagedResponseBaseModel):
    venue: typing.List[Venue]

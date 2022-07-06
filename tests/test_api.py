import datetime

import pytest

from setlist_fm_client import api, async_api, enums, models


@pytest.fixture(scope="module")
def vcr_config():
    return {
        "filter_headers": [("x-api-key", "DUMMY")],
        "record_mode": "once",
    }


@pytest.mark.vcr
class TestGetArtist:
    MBID = "0bfba3d3-6a04-4779-bb0a-df07df5b0558"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.get_artist(self.MBID, accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    def test_serialize(self):
        response = api.get_artist(self.MBID, serialize=True)
        assert isinstance(response, models.Artist)

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_get_artist(self.MBID, accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_get_artist(self.MBID, serialize=True)
        assert isinstance(response, models.Artist)


@pytest.mark.vcr
class TestGetArtistSetlists:
    MBID = "0bfba3d3-6a04-4779-bb0a-df07df5b0558"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.get_artist_setlists(self.MBID, accept=accept, p=2)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "2"

    def test_serialize(self):
        response = api.get_artist_setlists(self.MBID, serialize=True)
        assert isinstance(response, models.ArtistSetListResponse)

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_get_artist_setlists(self.MBID, accept=accept, p=2)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "2"

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_get_artist_setlists(self.MBID, serialize=True)
        assert isinstance(response, models.ArtistSetListResponse)


@pytest.mark.vcr
class TestGetCity:
    GEO_ID = "4930956"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.get_city(self.GEO_ID, accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    def test_serialize(self):
        response = api.get_city(self.GEO_ID, serialize=True)
        assert isinstance(response, models.City)

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_get_city(self.GEO_ID, accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_get_city(self.GEO_ID, serialize=True)
        assert isinstance(response, models.City)


@pytest.mark.vcr
class TestGetUser:
    USER_ID = "michi"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.get_user(self.USER_ID, accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    def test_serialize(self):
        response = api.get_user(self.USER_ID, serialize=True)
        assert isinstance(response, models.User)

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_get_user(self.USER_ID, accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_get_user(self.USER_ID, serialize=True)
        assert isinstance(response, models.User)


@pytest.mark.vcr
class TestGetSetlistsAtVenue:
    VENUE_ID = "6bd6ca6e"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.get_setlists_at_venue(self.VENUE_ID, accept=accept, p=2)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "2"

    def test_serialize(self):
        response = api.get_setlists_at_venue(self.VENUE_ID, serialize=True)
        assert isinstance(response, models.ArtistSetListResponse)

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_get_setlists_at_venue(self.VENUE_ID, accept=accept, p=2)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "2"

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_get_setlists_at_venue(self.VENUE_ID, serialize=True)
        assert isinstance(response, models.ArtistSetListResponse)


@pytest.mark.vcr
class TestGetSetlistOfConcertsAttendedByUser:
    USER_ID = "michi"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.get_setlists_of_concerts_attended_by_user(self.USER_ID, accept=accept, p=2)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "2"

    def test_serialize(self):
        response = api.get_setlists_of_concerts_attended_by_user(self.USER_ID, serialize=True)
        assert isinstance(response, models.ArtistSetListResponse)

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_get_setlists_of_concerts_attended_by_user(self.USER_ID, accept=accept, p=2)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "2"

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_get_setlists_of_concerts_attended_by_user(self.USER_ID, serialize=True)
        assert isinstance(response, models.ArtistSetListResponse)


@pytest.mark.vcr
class TestGetSetlistOfConcertsEditeddByUser:
    USER_ID = "michi"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.get_setlists_edited_by_user(self.USER_ID, accept=accept, p=2)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "2"

    def test_serialize(self):
        response = api.get_setlists_edited_by_user(self.USER_ID, serialize=True)
        assert isinstance(response, models.ArtistSetListResponse)

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_get_setlists_edited_by_user(self.USER_ID, accept=accept, p=2)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "2"

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_get_setlists_edited_by_user(self.USER_ID, serialize=True)
        assert isinstance(response, models.ArtistSetListResponse)


@pytest.mark.vcr
class TestSearchArtists:
    MBID = "0bfba3d3-6a04-4779-bb0a-df07df5b0558"
    NAME = "Stereophonics"
    SORT = enums.Sort.relevance

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.search_artists(accept=accept, mbid=self.MBID, name=self.NAME, sort=self.SORT)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "1"
        assert response.url.params["artistMbid"] == self.MBID
        assert response.url.params["artistName"] == self.NAME
        assert response.url.params["sort"] == self.SORT.value

    def test_serialize(self):
        response = api.search_artists(mbid=self.MBID, name=self.NAME, sort=self.SORT, serialize=True)
        assert isinstance(response, models.ArtistSearchResponse)
        assert len(response.artist) == 1

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_search_artists(mbid=self.MBID, name=self.NAME, sort=self.SORT, accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "1"
        assert response.url.params["artistMbid"] == self.MBID
        assert response.url.params["artistName"] == self.NAME
        assert response.url.params["sort"] == self.SORT.value

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_search_artists(mbid=self.MBID, name=self.NAME, sort=self.SORT, serialize=True)
        assert isinstance(response, models.ArtistSearchResponse)
        assert len(response.artist) == 1


@pytest.mark.vcr
class TestGetSetlistOfConcertsEditeddByUser:
    USER_ID = "michi"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.get_setlists_edited_by_user(self.USER_ID, accept=accept, p=2)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "2"

    def test_serialize(self):
        response = api.get_setlists_edited_by_user(self.USER_ID, serialize=True)
        assert isinstance(response, models.ArtistSetListResponse)

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_get_setlists_edited_by_user(self.USER_ID, accept=accept, p=2)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "2"

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_get_setlists_edited_by_user(self.USER_ID, serialize=True)
        assert isinstance(response, models.ArtistSetListResponse)


@pytest.mark.vcr
class TestSearchCities:
    COUNTRY = "US"
    NAME = "Hollywood"
    STATE = "California"
    STATE_CODE = "CA"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.search_cities(
            accept=accept, country=self.COUNTRY, name=self.NAME, state=self.STATE, state_code=self.STATE_CODE
        )
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "1"
        assert response.url.params["country"] == self.COUNTRY
        assert response.url.params["name"] == self.NAME
        assert response.url.params["state"] == self.STATE
        assert response.url.params["stateCode"] == self.STATE_CODE

    def test_serialize(self):
        response = api.search_cities(
            country=self.COUNTRY, name=self.NAME, state=self.STATE, state_code=self.STATE_CODE, serialize=True
        )
        assert isinstance(response, models.CitiesSearchResponse)
        assert len(response.cities) == 1

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_search_cities(
            country=self.COUNTRY, name=self.NAME, state=self.STATE, state_code=self.STATE_CODE, accept=accept
        )
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "1"
        assert response.url.params["country"] == self.COUNTRY
        assert response.url.params["name"] == self.NAME
        assert response.url.params["state"] == self.STATE
        assert response.url.params["stateCode"] == self.STATE_CODE

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_search_cities(
            country=self.COUNTRY, name=self.NAME, state=self.STATE, state_code=self.STATE_CODE, serialize=True
        )
        assert isinstance(response, models.CitiesSearchResponse)
        assert len(response.cities) == 1


@pytest.mark.vcr
class TestSearchCountries:
    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.search_countries(accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    def test_serialize(self):
        response = api.search_countries(serialize=True)
        assert isinstance(response, models.CountrySearchResponse)

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_search_countries()
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_search_countries(serialize=True)
        assert isinstance(response, models.CountrySearchResponse)


@pytest.mark.vcr
class TestSearchVenues:
    CITY_ID = "5128581"
    CITY_NAME = "New York"
    COUNTRY = "US"
    STATE = "New York"
    STATE_CODE = "NY"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.search_venues(
            city_id=self.CITY_ID,
            city_name=self.CITY_NAME,
            country=self.COUNTRY,
            state=self.STATE,
            state_code=self.STATE_CODE,
            accept=accept,
        )
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "1"
        assert response.url.params["country"] == self.COUNTRY
        assert response.url.params["cityName"] == self.CITY_NAME
        assert response.url.params["state"] == self.STATE
        assert response.url.params["stateCode"] == self.STATE_CODE

    def test_serialize(self):
        response = api.search_venues(
            city_id=self.CITY_ID,
            city_name=self.CITY_NAME,
            country=self.COUNTRY,
            state=self.STATE,
            state_code=self.STATE_CODE,
            serialize=True,
        )
        assert isinstance(response, models.VenueSearchResponse)
        assert len(response.venue) >= 1

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_search_venues(
            city_id=self.CITY_ID,
            city_name=self.CITY_NAME,
            country=self.COUNTRY,
            state=self.STATE,
            state_code=self.STATE_CODE,
            accept=accept,
        )
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value
        assert response.url.params["p"] == "1"
        assert response.url.params["country"] == self.COUNTRY
        assert response.url.params["cityName"] == self.CITY_NAME
        assert response.url.params["state"] == self.STATE
        assert response.url.params["stateCode"] == self.STATE_CODE

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_search_venues(
            city_id=self.CITY_ID,
            city_name=self.CITY_NAME,
            country=self.COUNTRY,
            state=self.STATE,
            state_code=self.STATE_CODE,
            serialize=True,
        )
        assert isinstance(response, models.VenueSearchResponse)
        assert len(response.venue) >= 1


@pytest.mark.vcr
class TestSearchSetlists:
    ARTIST_MBID = "67f66c07-6e61-4026-ade5-7e782fad3a5d"
    ARIST_NAME = "Foo Fighters"
    CITY_ID = "5140405"
    CITY_NAME = "Syracuse"
    COUNTRY_CODE = "US"
    STATE = "New York"
    STATE_CODE = "NY"
    DATE = datetime.date(2021, 9, 15)
    LAST_UPDATED = datetime.datetime(2021, 11, 4, 15, 39, 55, tzinfo=datetime.timezone.utc)
    STATE = "New York"
    CITY = "New York"
    TOUR_NAME = "26th Anniversary Tour"
    VENUE_ID = "43d23f0f"
    VENUE_NAME = "St. Joseph's Health Amphitheater at Lakeview"
    YEAR = "2021"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.search_setlists(
            artist_mbid=self.ARTIST_MBID,
            artist_name=self.ARIST_NAME,
            city_id=self.CITY_ID,
            city_name=self.CITY_NAME,
            country_code=self.COUNTRY_CODE,
            state=self.STATE,
            state_code=self.STATE_CODE,
            date=self.DATE,
            last_updated=self.LAST_UPDATED,
            tour_name=self.TOUR_NAME,
            venue_id=self.VENUE_ID,
            venue_name=self.VENUE_NAME,
            year=self.YEAR,
            p=1,
        )
        assert response.status_code == 200
        assert response.url.params["artistMbid"] == self.ARTIST_MBID
        assert response.url.params["artistName"] == self.ARIST_NAME
        assert response.url.params["cityId"] == self.CITY_ID
        assert response.url.params["cityName"] == self.CITY_NAME
        assert response.url.params["countryCode"] == self.COUNTRY_CODE
        assert response.url.params["state"] == self.STATE
        assert response.url.params["stateCode"] == self.STATE_CODE
        assert response.url.params["date"] == self.DATE.strftime("%d-%m-%Y")
        assert response.url.params["lastUpdated"] == self.LAST_UPDATED.strftime("%Y%m%d%H%M%S")
        assert response.url.params["tourName"] == self.TOUR_NAME
        assert response.url.params["venueId"] == self.VENUE_ID
        assert response.url.params["venueName"] == self.VENUE_NAME
        assert response.url.params["year"] == self.YEAR
        assert response.url.params["p"] == "1"
        assert response.request.headers["Accept"] == accept.value

    def test_serialize(self):
        response = api.search_setlists(
            artist_mbid=self.ARTIST_MBID,
            artist_name=self.ARIST_NAME,
            city_id=self.CITY_ID,
            city_name=self.CITY_NAME,
            country_code=self.COUNTRY_CODE,
            state=self.STATE,
            state_code=self.STATE_CODE,
            date=self.DATE,
            last_updated=self.LAST_UPDATED,
            tour_name=self.TOUR_NAME,
            venue_id=self.VENUE_ID,
            venue_name=self.VENUE_NAME,
            year=self.YEAR,
            p=1,
            serialize=True,
        )
        assert isinstance(response, models.ArtistSetListResponse)
        assert len(response.setlist) == 1

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_search_setlists(
            artist_mbid=self.ARTIST_MBID,
            artist_name=self.ARIST_NAME,
            city_id=self.CITY_ID,
            city_name=self.CITY_NAME,
            country_code=self.COUNTRY_CODE,
            state=self.STATE,
            state_code=self.STATE_CODE,
            date=self.DATE,
            last_updated=self.LAST_UPDATED,
            tour_name=self.TOUR_NAME,
            venue_id=self.VENUE_ID,
            venue_name=self.VENUE_NAME,
            year=self.YEAR,
            p=1,
            accept=accept,
        )
        assert response.status_code == 200
        assert response.url.params["artistMbid"] == self.ARTIST_MBID
        assert response.url.params["artistName"] == self.ARIST_NAME
        assert response.url.params["cityId"] == self.CITY_ID
        assert response.url.params["cityName"] == self.CITY_NAME
        assert response.url.params["countryCode"] == self.COUNTRY_CODE
        assert response.url.params["state"] == self.STATE
        assert response.url.params["stateCode"] == self.STATE_CODE
        assert response.url.params["date"] == self.DATE.strftime("%d-%m-%Y")
        assert response.url.params["lastUpdated"] == self.LAST_UPDATED.strftime("%Y%m%d%H%M%S")
        assert response.url.params["tourName"] == self.TOUR_NAME
        assert response.url.params["venueId"] == self.VENUE_ID
        assert response.url.params["venueName"] == self.VENUE_NAME
        assert response.url.params["year"] == self.YEAR
        assert response.url.params["p"] == "1"
        assert response.request.headers["Accept"] == accept.value

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_search_setlists(
            artist_mbid=self.ARTIST_MBID,
            artist_name=self.ARIST_NAME,
            city_id=self.CITY_ID,
            city_name=self.CITY_NAME,
            country_code=self.COUNTRY_CODE,
            state=self.STATE,
            state_code=self.STATE_CODE,
            date=self.DATE,
            last_updated=self.LAST_UPDATED,
            tour_name=self.TOUR_NAME,
            venue_id=self.VENUE_ID,
            venue_name=self.VENUE_NAME,
            year=self.YEAR,
            p=1,
            serialize=True,
        )
        assert isinstance(response, models.ArtistSetListResponse)
        assert len(response.setlist) == 1


@pytest.mark.vcr
class TestGetSetlist:
    SETLIST_ID = "63de4613"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.get_setlist(self.SETLIST_ID, accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    def test_serialize(self):
        response = api.get_setlist(self.SETLIST_ID, serialize=True)
        assert isinstance(response, models.ArtistSetList)

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_get_setlist(self.SETLIST_ID, accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_get_setlist(self.SETLIST_ID, serialize=True)
        assert isinstance(response, models.ArtistSetList)


@pytest.mark.vcr
class TestGetVenue:
    VENUE_ID = "6bd6ca6e"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.get_venue(self.VENUE_ID, accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    def test_serialize(self):
        response = api.get_venue(self.VENUE_ID, serialize=True)
        assert isinstance(response, models.Venue)

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_get_venue(self.VENUE_ID, accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_get_venue(self.VENUE_ID, serialize=True)
        assert isinstance(response, models.Venue)


@pytest.mark.vcr
class TestGetSetlistByVersion:
    VERSION_ID = "be1aaa0"

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    def test(self, accept):
        response = api.get_setlist_by_version(self.VERSION_ID, accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    def test_serialize(self):
        response = api.get_setlist_by_version(self.VERSION_ID, serialize=True)
        assert isinstance(response, models.ArtistSetList)

    @pytest.mark.parametrize("accept", [enums.Accept.json, enums.Accept.json])
    @pytest.mark.asyncio
    async def test_async(self, accept):
        response = await async_api.async_get_setlist_by_version(self.VERSION_ID, accept=accept)
        assert response.status_code == 200
        assert response.request.headers["Accept"] == accept.value

    @pytest.mark.asyncio
    async def test_async_serialize(self):
        response = await async_api.async_get_setlist_by_version(self.VERSION_ID, serialize=True)
        assert isinstance(response, models.ArtistSetList)

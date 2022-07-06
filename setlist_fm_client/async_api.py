import datetime
import typing

import httpx

from setlist_fm_client import models
from setlist_fm_client.core import async_get
from setlist_fm_client.core import build_params
from setlist_fm_client.enums import Accept
from setlist_fm_client.enums import Sort

__all__ = [
    "async_get_artist",
    "async_get_artist_setlists",
    "async_get_city",
    "async_get_user",
    "async_get_setlists_edited_by_user",
    "async_get_setlists_of_concerts_attended_by_user",
    "async_search_artists",
    "async_search_cities",
    "async_search_countries",
    "async_search_venues",
    "async_search_setlists",
    "async_get_setlist",
    "async_get_setlist_by_version",
]


async def async_get_artist(
    mbid: str, *, api_key: str = None, accept: Accept = Accept.json, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, models.Artist]:
    """Returns an artist for a given Musicbrainz MBID

    https://api.setlist.fm/docs/1.0/resource__1.0_artist__mbid_.html

    Args:
        mbid: a Musicbrainz MBID, e.g. 0bfba3d3-6a04-4779-bb0a-df07df5b0558
        api_key: the setlist.fm api key
        accept: content type for response
        serialize: defaults to False. if True, returns an `Artist` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`
        **kwargs:

    Returns:
        `Artist` if serialize is True, else `httpx.Response`
    """
    return await async_get(
        f"/artist/{mbid}", api_key=api_key, model=models.Artist if serialize else None, accept=accept.value, **kwargs
    )


async def async_get_artist_setlists(
    mbid: str, *, p: int = 1, api_key: str = None, accept: Accept = Accept.json, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, models.ArtistSetListResponse]:
    """Get a list of an artist's setlists

    https://api.setlist.fm/docs/1.0/resource__1.0_artist__mbid__setlists.html

    Args:
        mbid: a Musicbrainz MBID, e.g. 0bfba3d3-6a04-4779-bb0a-df07df5b0558
        p: the number of the result page
        api_key: the setlist.fm api key
        accept: content type for response
        serialize: defaults to False. if True, returns an `ArtistSetListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`
        **kwargs:

    Returns:
        `ArtistSetListResponse` if serialize is True, else `httpx.Response`
    """
    kwargs["params"] = build_params(p=p)
    return await async_get(
        f"/artist/{mbid}/setlists",
        api_key=api_key,
        model=models.ArtistSetListResponse if serialize else None,
        accept=accept.value,
        **kwargs,
    )


async def async_get_city(
    geoid: str, *, api_key: str = None, accept: Accept = Accept.json, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, models.City]:
    """Get a city by its unique geoid

    https://api.setlist.fm/docs/1.0/resource__1.0_city__geoId_.html

    Args:
        geoid: the geoid of the city, e.g. 4930956
        api_key: the setlist.fm api key
        accept: content type for response
        serialize: defaults to False. if True, returns a `City` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`

    Returns:
        `City` if serialize is True, else `httpx.Response`
    """
    return await async_get(
        f"/city/{geoid}", api_key=api_key, accept=accept.value, model=models.City if serialize else None, **kwargs
    )


async def async_get_user(
    user_id: str, *, api_key: str = None, accept: Accept = Accept.json, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, models.User]:
    """Get a user by their userId

    https://api.setlist.fm/docs/1.0/resource__1.0_user__userId_.html

    Args:
        user_id: the user's userId
        api_key: the setlist.fm api key
        accept: content type for response
        serialize: defaults to False. if True, returns a `User` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`

    Returns:
        `User` if serialize is True, else `httpx.Response`
    """
    return await async_get(
        f"/user/{user_id}", api_key=api_key, accept=accept.value, model=models.User if serialize else None, **kwargs
    )


async def async_get_venue(
    venue_id: str, *, api_key: str = None, accept: Accept = Accept.json, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, models.Venue]:
    """Get a venue by its venueId

    https://api.setlist.fm/docs/1.0/resource__1.0_venue__venueId_.html

    Args:
        venue_id: the venue's venueId, e.g. '6bd6ca6e'
        api_key: the setlist.fm api key
        accept: content type for response
        serialize: defaults to False. if True, returns a `Venue` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`

    Returns:
        `Venue` if serialize is True, else `httpx.Response`
    """
    return await async_get(
        f"/venue/{venue_id}", api_key=api_key, accept=accept.value, model=models.Venue if serialize else None, **kwargs
    )


async def async_get_setlists_at_venue(
    venue_id: str,
    *,
    p: int = None,
    api_key: str = None,
    accept: Accept = Accept.json,
    serialize: bool = False,
    **kwargs,
) -> typing.Union[httpx.Response, models.ArtistSetListResponse]:
    """Get setlists for a specific venue

    https://api.setlist.fm/docs/1.0/resource__1.0_venue__venueId__setlists.html

    Args:
        venue_id: the venue's venueId, e.g. '6bd6ca6e'
        p: the number of the result page
        api_key: the setlist.fm api key
        accept: content type for response
        serialize: defaults to False. if True, returns a `ArtistSetListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`

    Returns:
        `ArtistSetListResponse` if serialize is True, else `httpx.Response`
    """
    kwargs["params"] = build_params(p=p)
    return await async_get(
        f"/venue/{venue_id}/setlists",
        api_key=api_key,
        accept=accept.value,
        model=models.ArtistSetListResponse if serialize else None,
        **kwargs,
    )


async def async_get_setlists_of_concerts_attended_by_user(
    user_id: str, *, p: int = 1, api_key: str = None, accept: Accept = Accept.json, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, models.ArtistSetListResponse]:
    """Get a list of setlists of concerts attended by a user

    https://api.setlist.fm/docs/1.0/resource__1.0_user__userId__attended.html

    Args:
        user_id: the user's userId
        p: the number of the result page
        api_key: the setlist.fm api key
        accept: content type for response
        serialize: defaults to False. if True, returns a `ArtistSetListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`

    Returns:
        `ArtistSetListResponse` if serialize is True, else `httpx.Response`
    """
    kwargs["params"] = build_params(p=p)
    return await async_get(
        f"/user/{user_id}/attended",
        api_key=api_key,
        accept=accept.value,
        model=models.ArtistSetListResponse if serialize else None,
        **kwargs,
    )


async def async_get_setlists_edited_by_user(
    user_id: str, *, p: int = 1, api_key: str = None, accept: Accept = Accept.json, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, models.ArtistSetListResponse]:
    """Get a list of setlists of concerts edited by a user

    The list contains the current version, not the version edited.

    https://api.setlist.fm/docs/1.0/resource__1.0_user__userId__attended.html

    Args:
        user_id: the user's userId
        p: the number of the result page
        api_key: the setlist.fm api key
        accept: content type for response
        serialize: defaults to False. if True, returns a `ArtistSetListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`

    Returns:
        `ArtistSetListResponse` if serialize is True, else `httpx.Response`
    """
    kwargs["params"] = build_params(p=p)
    return await async_get(
        f"/user/{user_id}/edited",
        api_key=api_key,
        accept=accept.value,
        model=models.ArtistSetListResponse if serialize else None,
        **kwargs,
    )


async def async_search_artists(
    *,
    mbid: str = None,
    name: str = None,
    p: int = 1,
    sort: Sort = Sort.sort_name,
    accept: Accept = Accept.json,
    api_key: str = None,
    serialize: bool = False,
    **kwargs,
) -> typing.Union[httpx.Response, models.ArtistSearchResponse]:
    """Search for artists using their mbid or their name.

    https://api.setlist.fm/docs/1.0/resource__1.0_async_searchartists.html

    Args:
        mbid: mbid: a Musicbrainz MBID, e.g. 0bfba3d3-6a04-4779-bb0a-df07df5b0558
        name: the artist's name
        p: the number of the result page
        sort: the method in which to sort the result set
        accept: content type for response
        api_key: the setlist.fm api key
        serialize: defaults to False. if True, returns a `ArtistSearchResponse` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`

    Returns:
        'ArtistSearchResponse` if serialize is True, else `httpx.Response`
    """
    kwargs["params"] = build_params(p=p, sort=sort.value, artistMbid=mbid, artistName=name)

    return await async_get(
        f"/search/artists",
        api_key=api_key,
        accept=accept.value,
        model=models.ArtistSearchResponse if serialize else None,
        **kwargs,
    )


async def async_search_cities(
    *,
    country: str = None,
    name: str = None,
    state: str = None,
    state_code: str = None,
    p: int = 1,
    accept: Accept = Accept.json,
    api_key: str = None,
    serialize: bool = False,
    **kwargs,
) -> typing.Union[httpx.Response, models.CitiesSearchResponse]:
    """Search for a city using various parameters

    https://api.setlist.fm/docs/1.0/resource__1.0_async_searchcities.html

    Args:
        country: the city's country
        name: the city's name
        state: the city's state
        state_code: the city's state code
        p: the number of the result page
        accept: content type for response
        api_key: the setlist.fm api key
        serialize: defaults to False. if True, returns a `CitySearchResponse` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`

    Returns:
        'CitySearchResponse` if serialize is True, else `httpx.Response`
    """
    kwargs["params"] = build_params(p=p, country=country, name=name, state=state, stateCode=state_code)
    return await async_get(
        f"/search/cities",
        api_key=api_key,
        accept=accept.value,
        model=models.CitiesSearchResponse if serialize else None,
        **kwargs,
    )


async def async_search_countries(
    *, accept: Accept = Accept.json, api_key: str = None, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, models.CountrySearchResponse]:
    """Get a list of all supported countries

    https://api.setlist.fm/docs/1.0/resource__1.0_async_searchcountries.html

    Args:
        accept: content type for response
        api_key: the setlist.fm api key
        serialize: defaults to False. if True, returns a `CountrySearchResponse` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`

    Returns:
        'CountrySearchResponse` if serialize is True, else `httpx.Response`
    """
    return await async_get(
        f"/search/countries",
        api_key=api_key,
        accept=accept.value,
        model=models.CountrySearchResponse if serialize else None,
        **kwargs,
    )


async def async_search_venues(
    *,
    city_id: str = None,
    city_name: str = None,
    country: str = None,
    state: str = None,
    state_code: str = None,
    p: int = 1,
    accept: Accept = Accept.json,
    api_key: str = None,
    serialize: bool = False,
    **kwargs,
) -> typing.Union[httpx.Response, models.VenueSearchResponse]:
    """Search for a venue using various parameters

    https://api.setlist.fm/docs/1.0/resource__1.0_async_searchvenues.html

    Args:
        city_id: the city's geoId, , e.g. '5128581'
        city_name: the name of the city where the venue is located
        country: the name of the country where the venue is located
        state: the name of the state where the venue is located
        state_code: the state code of the state where the venue is located
        p: the number of the result page
        accept: content type for response
        api_key: the setlist.fm api key
        serialize: defaults to False. if True, returns a `VenueSearchResponse` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`

    Returns:
        'VenueSearchResponse` if serialize is True, else `httpx.Response`
    """
    kwargs["params"] = build_params(
        cityId=city_id, cityName=city_name, country=country, state=state, stateCode=state_code, p=p
    )
    return await async_get(
        f"/search/venues",
        api_key=api_key,
        accept=accept.value,
        model=models.VenueSearchResponse if serialize else None,
        **kwargs,
    )


async def async_search_setlists(
    *,
    artist_mbid: str = None,
    artist_name: str = None,
    city_id: str = None,
    city_name: str = None,
    country_code: str = None,
    date: datetime.date = None,
    last_updated: datetime.datetime = None,
    state: str = None,
    state_code: str = None,
    tour_name: str = None,
    venue_id: str = None,
    venue_name: str = None,
    year: typing.Union[int, str] = None,
    p: int = 1,
    accept: Accept = Accept.json,
    api_key: str = None,
    serialize: bool = False,
    **kwargs,
) -> typing.Union[httpx.Response, models.ArtistSetListResponse]:
    """Search for setlists using a variety of query params

    https://api.setlist.fm/docs/1.0/resource__1.0_async_searchsetlists.html

    Args:
        artist_mbid: the artist's Musicbrainz Identifier
        artist_name: the artist's name
        city_id: the city's geoId
        city_name: the name of the city
        country_code: the country code
        date: the date of the event
        last_updated: the datetime (UTC) when this setlist was last updated - either edited or reverted.
        state: the state
        state_code: the state code
        tour_name: the name of the tour
        venue_id: the venue id
        venue_name: the name of the venue
        year: the year of the event
        p: the number of the result page
        accept: content type for response
        api_key: the setlist.fm api key
        serialize: defaults to False. if True, returns a `ArtistSetListResponse` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`

    Returns:
        'ArtistSetListResponse` if serialize is True, else `httpx.Response`
    """
    kwargs["params"] = build_params(
        artistMbid=artist_mbid,
        artistName=artist_name,
        cityId=city_id,
        cityName=city_name,
        countryCode=country_code,
        date=date.strftime("%d-%m-%Y") if date else None,
        lastUpdated=last_updated.strftime("%Y%m%d%H%M%S") if last_updated else None,
        state=state,
        stateCode=state_code,
        tourName=tour_name,
        venueId=venue_id,
        venueName=venue_name,
        year=year,
        p=p,
    )
    return await async_get(
        f"/search/setlists",
        api_key=api_key,
        accept=accept.value,
        model=models.ArtistSetListResponse if serialize else None,
        **kwargs,
    )


async def async_get_setlist(
    setlist_id: str, *, accept: Accept = Accept.json, api_key: str = None, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, models.ArtistSetList]:
    """Returns the current version of a setlist

    If you pass the id of a setlist that got edited since you last accessed it, you'll get the current version.

    https://api.setlist.fm/docs/1.0/resource__1.0_setlist__setlistId_.html

    Args:
        setlist_id: the setlist's selistId, e.g. '63de4613'
        accept: content type for response
        api_key: the setlist.fm api key
        serialize: defaults to False. if True, returns a `ArtistSetList` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`

    Returns:
        'ArtistSetList` if serialize is True, else `httpx.Response`
    """
    return await async_get(
        f"/setlist/{setlist_id}",
        accept=accept.value,
        api_key=api_key,
        model=models.ArtistSetList if serialize else None,
        **kwargs,
    )


async def async_get_setlist_by_version(
    version_id: str, *, accept: Accept = Accept.json, api_key: str = None, serialize: bool = False, **kwargs
) -> typing.Union[httpx.Response, models.ArtistSetList]:
    """Returns a setlist for the given versionId.

    The setlist returned isn't necessarily the most recent version. E.g. if you pass the versionId of a setlist that
    got edited since you last accessed it, you'll get the same version as last time.

    https://api.setlist.fm/docs/1.0/resource__1.0_setlist_version__versionId_.html

    Args:
        version_id: the setlist's versionId, e.g. 'be1aaa0'
        accept: content type for response
        api_key: the setlist.fm api key
        serialize: defaults to False. if True, returns a `ArtistSetList` object
        **kwargs: additional kwargs to pass down to `httpx.Client.get`

    Returns:
        'ArtistSetList` if serialize is True, else `httpx.Response`
    """
    return await async_get(
        f"/setlist/version/{version_id}",
        accept=accept.value,
        api_key=api_key,
        model=models.ArtistSetList if serialize else None,
        **kwargs,
    )

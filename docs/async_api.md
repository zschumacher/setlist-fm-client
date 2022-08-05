
<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L0"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

# <kbd>module</kbd> `async_api.py`





---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L29"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_get_artist`

```python
async_get_artist(
    mbid: str,
    api_key: str = None,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.Artist]
```

Returns an artist for a given Musicbrainz MBID 

https://api.setlist.fm/docs/1.0/resource__1.0_artist__mbid_.html 



**Args:**
 
 - <b>`mbid`</b>:  a Musicbrainz MBID, e.g. 0bfba3d3-6a04-4779-bb0a-df07df5b0558 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`accept`</b>:  content type for response 
 - <b>`serialize`</b>:  defaults to False. if True, returns an `Artist` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` **kwargs: 



**Returns:**
 `Artist` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L52"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_get_artist_setlists`

```python
async_get_artist_setlists(
    mbid: str,
    p: int = 1,
    api_key: str = None,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.ArtistSetListResponse]
```

Get a list of an artist's setlists 

https://api.setlist.fm/docs/1.0/resource__1.0_artist__mbid__setlists.html 



**Args:**
 
 - <b>`mbid`</b>:  a Musicbrainz MBID, e.g. 0bfba3d3-6a04-4779-bb0a-df07df5b0558 
 - <b>`p`</b>:  the number of the result page 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`accept`</b>:  content type for response 
 - <b>`serialize`</b>:  defaults to False. if True, returns an `ArtistSetListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` **kwargs: 



**Returns:**
 `ArtistSetListResponse` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L81"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_get_city`

```python
async_get_city(
    geoid: str,
    api_key: str = None,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.City]
```

Get a city by its unique geoid 

https://api.setlist.fm/docs/1.0/resource__1.0_city__geoId_.html 



**Args:**
 
 - <b>`geoid`</b>:  the geoid of the city, e.g. 4930956 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`accept`</b>:  content type for response 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `City` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `City` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L103"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_get_user`

```python
async_get_user(
    user_id: str,
    api_key: str = None,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.User]
```

Get a user by their userId 

https://api.setlist.fm/docs/1.0/resource__1.0_user__userId_.html 



**Args:**
 
 - <b>`user_id`</b>:  the user's userId 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`accept`</b>:  content type for response 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `User` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `User` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L125"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_get_venue`

```python
async_get_venue(
    venue_id: str,
    api_key: str = None,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.Venue]
```

Get a venue by its venueId 

https://api.setlist.fm/docs/1.0/resource__1.0_venue__venueId_.html 



**Args:**
 
 - <b>`venue_id`</b>:  the venue's venueId, e.g. '6bd6ca6e' 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`accept`</b>:  content type for response 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `Venue` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `Venue` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L147"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_get_setlists_at_venue`

```python
async_get_setlists_at_venue(
    venue_id: str,
    p: int = None,
    api_key: str = None,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.ArtistSetListResponse]
```

Get setlists for a specific venue 

https://api.setlist.fm/docs/1.0/resource__1.0_venue__venueId__setlists.html 



**Args:**
 
 - <b>`venue_id`</b>:  the venue's venueId, e.g. '6bd6ca6e' 
 - <b>`p`</b>:  the number of the result page 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`accept`</b>:  content type for response 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `ArtistSetListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `ArtistSetListResponse` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L181"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_get_setlists_of_concerts_attended_by_user`

```python
async_get_setlists_of_concerts_attended_by_user(
    user_id: str,
    p: int = 1,
    api_key: str = None,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.ArtistSetListResponse]
```

Get a list of setlists of concerts attended by a user 

https://api.setlist.fm/docs/1.0/resource__1.0_user__userId__attended.html 



**Args:**
 
 - <b>`user_id`</b>:  the user's userId 
 - <b>`p`</b>:  the number of the result page 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`accept`</b>:  content type for response 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `ArtistSetListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `ArtistSetListResponse` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L209"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_get_setlists_edited_by_user`

```python
async_get_setlists_edited_by_user(
    user_id: str,
    p: int = 1,
    api_key: str = None,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.ArtistSetListResponse]
```

Get a list of setlists of concerts edited by a user 

The list contains the current version, not the version edited. 

https://api.setlist.fm/docs/1.0/resource__1.0_user__userId__attended.html 



**Args:**
 
 - <b>`user_id`</b>:  the user's userId 
 - <b>`p`</b>:  the number of the result page 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`accept`</b>:  content type for response 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `ArtistSetListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 `ArtistSetListResponse` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L239"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_search_artists`

```python
async_search_artists(
    mbid: str = None,
    name: str = None,
    p: int = 1,
    sort: setlist_fm_client.enums.Sort = <Sort.sort_name: 'sortName'>,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.ArtistSearchResponse]
```

Search for artists using their mbid or their name. 

https://api.setlist.fm/docs/1.0/resource__1.0_async_searchartists.html 



**Args:**
 
 - <b>`mbid`</b>:  mbid: a Musicbrainz MBID, e.g. 0bfba3d3-6a04-4779-bb0a-df07df5b0558 
 - <b>`name`</b>:  the artist's name 
 - <b>`p`</b>:  the number of the result page 
 - <b>`sort`</b>:  the method in which to sort the result set 
 - <b>`accept`</b>:  content type for response 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `ArtistSearchResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 'ArtistSearchResponse` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L278"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_search_cities`

```python
async_search_cities(
    country: str = None,
    name: str = None,
    state: str = None,
    state_code: str = None,
    p: int = 1,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.CitiesSearchResponse]
```

Search for a city using various parameters 

https://api.setlist.fm/docs/1.0/resource__1.0_async_searchcities.html 



**Args:**
 
 - <b>`country`</b>:  the city's country 
 - <b>`name`</b>:  the city's name 
 - <b>`state`</b>:  the city's state 
 - <b>`state_code`</b>:  the city's state code 
 - <b>`p`</b>:  the number of the result page 
 - <b>`accept`</b>:  content type for response 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `CitySearchResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 'CitySearchResponse` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L318"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_search_countries`

```python
async_search_countries(
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.CountrySearchResponse]
```

Get a list of all supported countries 

https://api.setlist.fm/docs/1.0/resource__1.0_async_searchcountries.html 



**Args:**
 
 - <b>`accept`</b>:  content type for response 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `CountrySearchResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 'CountrySearchResponse` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L343"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_search_venues`

```python
async_search_venues(
    city_id: str = None,
    city_name: str = None,
    country: str = None,
    state: str = None,
    state_code: str = None,
    p: int = 1,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.VenueSearchResponse]
```

Search for a venue using various parameters 

https://api.setlist.fm/docs/1.0/resource__1.0_async_searchvenues.html 



**Args:**
 
 - <b>`city_id`</b>:  the city's geoId, , e.g. '5128581' 
 - <b>`city_name`</b>:  the name of the city where the venue is located 
 - <b>`country`</b>:  the name of the country where the venue is located 
 - <b>`state`</b>:  the name of the state where the venue is located 
 - <b>`state_code`</b>:  the state code of the state where the venue is located 
 - <b>`p`</b>:  the number of the result page 
 - <b>`accept`</b>:  content type for response 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `VenueSearchResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 'VenueSearchResponse` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L387"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_search_setlists`

```python
async_search_setlists(
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
    year: Union[int, str] = None,
    p: int = 1,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.ArtistSetListResponse]
```

Search for setlists using a variety of query params 

https://api.setlist.fm/docs/1.0/resource__1.0_async_searchsetlists.html 



**Args:**
 
 - <b>`artist_mbid`</b>:  the artist's Musicbrainz Identifier 
 - <b>`artist_name`</b>:  the artist's name 
 - <b>`city_id`</b>:  the city's geoId 
 - <b>`city_name`</b>:  the name of the city 
 - <b>`country_code`</b>:  the country code 
 - <b>`date`</b>:  the date of the event 
 - <b>`last_updated`</b>:  the datetime (UTC) when this setlist was last updated - either edited or reverted. 
 - <b>`state`</b>:  the state 
 - <b>`state_code`</b>:  the state code 
 - <b>`tour_name`</b>:  the name of the tour 
 - <b>`venue_id`</b>:  the venue id 
 - <b>`venue_name`</b>:  the name of the venue 
 - <b>`year`</b>:  the year of the event 
 - <b>`p`</b>:  the number of the result page 
 - <b>`accept`</b>:  content type for response 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `ArtistSetListResponse` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 'ArtistSetListResponse` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L460"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_get_setlist`

```python
async_get_setlist(
    setlist_id: str,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.ArtistSetList]
```

Returns the current version of a setlist 

If you pass the id of a setlist that got edited since you last accessed it, you'll get the current version. 

https://api.setlist.fm/docs/1.0/resource__1.0_setlist__setlistId_.html 



**Args:**
 
 - <b>`setlist_id`</b>:  the setlist's selistId, e.g. '63de4613' 
 - <b>`accept`</b>:  content type for response 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `ArtistSetList` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 'ArtistSetList` if serialize is True, else `httpx.Response` 


---

<a href="https://github.com/zschumacher/setlist-fm-client/blob/main/setlist_fm_client/async_api.py#L488"><img align="right" style="float:right;" src="https://img.shields.io/badge/-source-cccccc?style=flat-square"></a>

## <kbd>function</kbd> `async_get_setlist_by_version`

```python
async_get_setlist_by_version(
    version_id: str,
    accept: setlist_fm_client.enums.Accept = <Accept.json: 'application/json'>,
    api_key: str = None,
    serialize: bool = False,
    **kwargs
) → Union[httpx.Response, setlist_fm_client.models.ArtistSetList]
```

Returns a setlist for the given versionId. 

The setlist returned isn't necessarily the most recent version. E.g. if you pass the versionId of a setlist that got edited since you last accessed it, you'll get the same version as last time. 

https://api.setlist.fm/docs/1.0/resource__1.0_setlist_version__versionId_.html 



**Args:**
 
 - <b>`version_id`</b>:  the setlist's versionId, e.g. 'be1aaa0' 
 - <b>`accept`</b>:  content type for response 
 - <b>`api_key`</b>:  the setlist.fm api key 
 - <b>`serialize`</b>:  defaults to False. if True, returns a `ArtistSetList` object 
 - <b>`**kwargs`</b>:  additional kwargs to pass down to `httpx.Client.get` 



**Returns:**
 'ArtistSetList` if serialize is True, else `httpx.Response` 




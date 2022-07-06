from setlist_fm_client.core import _build_headers, SetlistFmClient, AsyncSetlistFmClient, SETLIST_FM_API_KEY_VAR_NAME
from setlist_fm_client.enums import Accept
import pytest


class TestBuildHeaders:

    def test_when_accept_is_none_value_error_raises(self):
        with pytest.raises(ValueError):
            _build_headers(
                None,
                None,
                SetlistFmClient()
            )

    @pytest.mark.parametrize(
        "headers", [
            {"hello": "world"},
            None
        ]
    )
    def test_different_header_kwargs(self, headers):
        headers = _build_headers(
            Accept.json,
            None,
            SetlistFmClient(),
            headers=headers
        )
        assert isinstance(headers, dict)

    @pytest.mark.parametrize("client", [SetlistFmClient, AsyncSetlistFmClient])
    def test_passed_api_key(self, client, monkeypatch):
        monkeypatch.delenv(SETLIST_FM_API_KEY_VAR_NAME)
        headers = _build_headers(
            Accept.json,
            "super-secret-key",
            client()
        )
        assert headers["x-api-key"] == "super-secret-key"

    @pytest.mark.parametrize("client", [SetlistFmClient, AsyncSetlistFmClient])
    def test_instance_api_key(self, client, monkeypatch):
        monkeypatch.setenv(SETLIST_FM_API_KEY_VAR_NAME, "super-secret-key")
        headers = _build_headers(
            Accept.json,
            None,
            client()
        )
        assert headers["x-api-key"] == "super-secret-key"

    @pytest.mark.parametrize("client", [SetlistFmClient, AsyncSetlistFmClient])
    def test_missing_api_key_raises(self, client, monkeypatch):
        monkeypatch.delenv(SETLIST_FM_API_KEY_VAR_NAME)
        with pytest.raises(ValueError):
            headers = _build_headers(
                Accept.json,
                None,
                client()
            )
            print(headers)

    @pytest.mark.parametrize("accept", [Accept.json, Accept.xml])
    def test_accept_header_is_set(self, accept):
        headers = _build_headers(
            accept.value,
            "super-secret-key",
            SetlistFmClient()
        )
        assert headers["Accept"] == accept.value

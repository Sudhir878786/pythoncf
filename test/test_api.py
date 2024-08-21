import cf
import pytest


class TestCall(object):
    def test_undefined_method(self):
        with pytest.raises(cf.error.CodeforcesAPIError):
            method = "undefined.method"
            cf.api.call(method)

    def test_unauth_method(self):
        method = "user.info"
        handles = "cf"

        cf.api.call(method, handles=handles)

        key = "0d905168ea10217dd91472e861bf8c80932f060e"
        secret = "3d3872085b0255159381a1884e9f66d5213ba796"
        cf.api.call(method, key=key, secret=secret, handles=handles)

    def test_auth_method(self):
        method = "user.friends"

        key = "0d905168ea10217dd91472e861bf8c80932f060e"
        secret = "3d3872085b0255159381a1884e9f66d5213ba796"
        cf.api.call(method, key=key, secret=secret)

        with pytest.raises(cf.error.CodeforcesAPIError):
            cf.api.call(method)

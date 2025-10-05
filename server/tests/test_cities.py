import pytest
import server.cities as cities


class TestIsValidId:
    def test_valid(self):
        assert cities.is_valid_id('1') == True

    def test_non_str(self):
        assert cities.is_valid_id(1) == False

    def test_empty_str(self):
        assert cities.is_valid_id('') == False


class TestCreate:
    def test_valid(self):
        old_length = cities.length()
        _id = cities.create({cities.NAME: 'New York'})
        assert cities.is_valid_id(_id)
        assert cities.length() > old_length

    def test_non_dict(self):
        with pytest.raises(ValueError):
            cities.create(10)

    def test_missing_name(self):
        with pytest.raises(ValueError):
            cities.create({})

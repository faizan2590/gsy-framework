import unittest
from datetime import datetime

from d3a_interface.utils import (
    HomeRepresentationUtils, scenario_representation_traversal,
    sort_list_of_dicts_by_attribute, convert_datetime_to_ui_str_format)


class TestUtils(unittest.TestCase):

    def setUp(self):
        self.scenario_repr = {
            "name": "grid",
            "children": [
                {"name": "S1 House", "children": [
                    {"name": "Load", "type": "Load"},
                    {"name": "Home Battery", "type": "Storage"}
                ]},
                {"name": "S2 House", "children": [
                    {"name": "Load", "type": "Load"},
                    {"name": "Home Battery", "type": "Storage"},
                    {"name": "Home PV", "type": "PV"}
                ]}
            ]
        }

    def test_scenario_representation_traversal(self):
        areas = list(scenario_representation_traversal(self.scenario_repr))
        assert len(areas) == 8
        assert all(type(obj) == tuple for obj in areas)

    def test_calculate_home_area_stats_from_repr_dict(self):
        home_count, avg_devices_per_home = \
            HomeRepresentationUtils.calculate_home_area_stats_from_repr_dict(self.scenario_repr)
        assert home_count == 2
        assert avg_devices_per_home == 2.5

    def test_sort_list_of_dicts_by_attribute(self):
        input_list = [
            {"id": 1, "energy": 15, "energy_rate": 1, "price": 30},
            {"id": 2, "energy": 20, "energy_rate": 4, "price": 25},
            {"id": 3, "energy": 12, "energy_rate": 3, "price": 77},
            {"id": 4, "energy": 13, "energy_rate": 2, "price": 12},
        ]
        output_list = sort_list_of_dicts_by_attribute(input_list, "price")
        assert [4, 2, 1, 3] == [data["id"] for data in output_list]
        output_list = sort_list_of_dicts_by_attribute(input_list, "price", reverse_order=True)
        assert [3, 1, 2, 4] == [data["id"] for data in output_list]

    def test_convert_datetime_to_ui_str_format(self):
        current_time = datetime(year=2021, month=8, day=30, hour=15, minute=30, second=45)
        current_time_str = convert_datetime_to_ui_str_format(current_time)
        assert current_time_str == "August 30 2021, 15:30 h"

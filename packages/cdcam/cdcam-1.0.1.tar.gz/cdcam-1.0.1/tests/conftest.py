import pytest
from pytest import fixture

from cdcam.model import NetworkManager


@fixture(scope='function')
def setup_lad():
    return [
        {
            "id": 1,
            "name": "Cambridge",
        }
    ]


@fixture(scope='function')
def setup_pcd_sector():
    return [
        {
            "id": "CB11",
            "lad_id": 1,
            "population": 500,
            "area_km2": 2,
            "user_throughput": 2,
        },
        {
            "id": "CB12",
            "lad_id": 1,
            "population": 200,
            "area_km2": 2,
            "user_throughput": 2,
        }
    ]


@fixture(scope='function')
def setup_pcd_sectors2():
    return [
        {
            "id": "CB11",
            "lad_id": 1,
            "population": 100000,
            "area_km2": 2,
            "user_throughput": 2,
        },
        {
            "id": "CB12",
            "lad_id": 1,
            "population": 100000,
            "area_km2": 2,
            "user_throughput": 2,
        }
    ]


@fixture(scope='function')
def setup_non_4g_assets():
    return [
        {
            "pcd_sector": "CB11",
            "site_ngr": "site_100",
            "technology": "",
            "type": "macrocell_site",
            "frequency": [],
            "bandwidth": "",
            "build_date": 2012,
            "sectors": 3,
            'opex': 10000,
        },
        {
            "pcd_sector": "CB12",
            "site_ngr": "site_200",
            "technology": "",
            "type": "macrocell_site",
            "frequency": [],
            "bandwidth": "",
            "build_date": 2012,
            "sectors": 3,
            'opex': 10000,
        }
    ]


@fixture(scope='function')
def setup_assets():
    return [
        {
            "pcd_sector": "CB11",
            "site_ngr": "site_100",
            "technology": "LTE",
            "type": "macrocell_site",
            "frequency": ["800", "2600"],
            "bandwidth": "10",
            "build_date": 2017,
            "sectors": 3,
            'opex': 10000,
        },
        {
            "pcd_sector": "CB12",
            "site_ngr": "site_200",
            "technology": "LTE",
            "type": "macrocell_site",
            "frequency": ["800", "2600"],
            "bandwidth": "10",
            "build_date": 2017,
            "sectors": 3,
            'opex': 10000,
        },
    ]


@fixture(scope='function')
def setup_mixed_assets():
    return [
        {
            "pcd_sector": "CB11",
            "site_ngr": "site_100",
            "technology": "LTE",
            "type": "macrocell_site",
            "frequency": ["800", "2600"],
            "bandwidth": "10",
            "build_date": 2017,
            "sectors": 3,
            'opex': 10000,
        },
        {
            "pcd_sector": "CB12",
            "site_ngr": "site_200",
            "technology": "LTE",
            "type": "macrocell_site",
            "frequency": ["800", "2600"],
            "bandwidth": "10",
            "build_date": 2017,
            "sectors": 3,
            'opex': 10000,
        },
        {
            'pcd_sector': "CB11",
            'site_ngr': 'small_cell_site',
            'frequency': '3700',
            'technology': 'same',
            'type': 'small_cell',
            'bandwidth': '25',
            'sectors': 1,
            'build_date': None,
            'opex': 2000,
        },
        {
            'pcd_sector': "CB11",
            'site_ngr': 'small_cell_site',
            'frequency': '3700',
            'technology': 'same',
            'type': 'small_cell',
            'bandwidth': '25',
            'sectors': 1,
            'build_date': None,
            'opex': 2000,
        },
        {
            'pcd_sector': "CB12",
            'site_ngr': 'small_cell_site',
            'frequency': '3700',
            'technology': 'same',
            'type': 'small_cell',
            'bandwidth': '25',
            'sectors': 1,
            'build_date': None,
            'opex': 2000,
        },
        {
            'pcd_sector': "CB12",
            'site_ngr': 'small_cell_site',
            'frequency': '3700',
            'technology': 'same',
            'type': 'small_cell',
            'bandwidth': '25',
            'sectors': 1,
            'build_date': None,
            'opex': 2000,
        },
    ]


@fixture(scope='function')
def setup_capacity_lookup():
    return {
        ("urban", "macro", "700", "10", "5G"): [
            (0, 0),
            (1, 2),
        ],
        ("urban", "macro", "800", "10", "4G"): [
            (0, 0),
            (1, 2),
        ],
        ("urban", "macro", "2600", "10", "4G"): [
            (0, 0),
            (3, 5),
        ],
        ("urban", "macro", "3500", "80", "5G"): [
            (0, 0),
            (3, 5),
        ],
        ('rural', 'micro', '3700', '25', "5G"): [
            (0, 0),
            (3, 10),
        ],
        ("rural", "macro", "700", "10", "5G"): [
            (0, 0),
            (1, 2),
        ],
        ("rural", "macro", "800", "10", "4G"): [
            (0, 0),
            (0.25, 0.5),
            (0.5, 1),
            (0.75, 1.5),
            (1, 2),
            (2, 4),
        ],
        ("rural", "macro", "2600", "10", "4G"): [
            (0, 0),
            (1, 2),
            (2, 4),
            (3, 5),
        ],
        ("rural", "macro", "3500", "40", "5G"): [
            (0, 0),
            (3, 5),
        ],
        ("rural", "macro", "1800", "10", "4G"): [
            (0, 0),
            (0, 0),
        ],
        ("urban", "macro", "700", "10", "5G"): [
            (0, 0),
            (2, 4),
        ],
        ("rural", "macro", "26000", "200", "5G"): [
            (0, 0),
            (0.1, 10),
            (2, 100),
            (4, 200),
        ],
        ("urban", "micro", "700", "10", "5G"): [
            (0, 0),
            (1, 2),
        ],
        ("urban", "micro", "800", "10", "4G"): [
            (0, 0),
            (1, 2),
        ],
        ("urban", "micro", "2600", "10", "4G"): [
            (0, 0),
            (3, 5),
        ],
        ("urban", "micro", "3500", "80", "5G"): [
            (0, 0),
            (3, 5),
        ],
        ('rural', 'micro', '3700', '40', "5G"): [
            (0, 0),
            (3, 10),
        ],
        ("rural", "micro", "700", "10", "5G"): [
            (0, 0),
            (1, 2),
        ],
        ("rural", "micro", "800", "10", "4G"): [
            (0, 0),
            (0.25, 0.5),
            (0.5, 1),
            (0.75, 1.5),
            (1, 2),
            (2, 4),
        ],
        ("rural", "micro", "2600", "10", "4G"): [
            (0, 0),
            (1, 2),
            (2, 4),
            (3, 5),
        ],
        ("rural", "micro", "3500", "40", "5G"): [
            (0, 0),
            (3, 5),
        ],
        ("rural", "micro", "1800", "10", "4G"): [
            (0, 0),
            (0, 0),
        ],
        ("urban", "micro", "700", "10", "5G"): [
            (0, 0),
            (2, 4),
        ],
        ("rural", "micro", "26000", "200", "5G"): [
            (0, 0),
            (0.1, 10),
            (2, 100),
            (4, 200),
        ],
    }

@fixture(scope='function')
def setup_capacity_lookup_table2():
    return {
    ('urban', 'macro', '800', '10', '4G'): [
        (0.01, 1), (0.1, 10), (1, 100), (2, 200)
    ],
    ('urban', 'macro', '2600', '10', '4G'): [
        (0.01, 1), (0.1, 10), (1, 100), (2, 200)
    ],
    ('urban', 'macro', '700', '10', '5G'): [
        (0.01, 1), (0.1, 10), (1, 100), (2, 200)
    ],
    ('urban', 'macro', '3500', '40', '5G'): [
        (0.01, 1), (0.1, 10), (1, 100), (2, 200)
    ],
    ('urban', 'macro', '26000', '200', '5G'): [
        (0.01, 1), (0.1, 10), (1, 100), (2, 200)
    ],
    ('urban', 'micro', '800', '10', '4G'): [
        (0.01, 1), (0.1, 10), (1, 100), (2, 200)
    ],
    ('urban', 'micro', '2600', '10', '4G'): [
        (0.01, 1), (0.1, 10), (1, 100), (2, 200)
    ],
    ('urban', 'micro', '3700', '40', '5G'): [
        (0.01, 1), (0.1, 10), (1, 100), (2, 200)
    ],
    ('urban', 'micro', '26000', '200', '5G'): [
        (0.01, 1), (0.1, 10), (1, 100), (2, 200)
    ],
    ('urban', 'micro', '26000', '200', '5G'): [
        (0.01, 1), (0.1, 10), (1, 100), (2, 200)
    ],
}

@fixture(scope='function')
def setup_clutter_lookup():
    return  [
        (0.0, 'rural'),
        (782.0, 'Suburban'),
        (7959.0, 'urban'),
    ]


@pytest.fixture
def setup_simulation_parameters():
    return {
        'market_share': 0.25,
        'annual_budget': 500000000,
        'service_obligation_capacity': 100,
        'busy_hour_traffic_percentage': 15,
        'coverage_threshold': 2,
        'penetration': 80,
        'channel_bandwidth_700': '10',
        'channel_bandwidth_800': '10',
        'channel_bandwidth_1800': '10',
        'channel_bandwidth_2600': '10',
        'channel_bandwidth_3500': '40',
        'channel_bandwidth_3700': '40',
        'channel_bandwidth_26000': '200',
        'macro_sectors': 3,
        'small_cell_sectors': 1,
        'mast_height': 30,
    }


@pytest.fixture
def setup_simulation_parameters2():
    return {
        'market_share': 0.3,
        'annual_budget': 1e6,
        'service_obligation_capacity': 10,
        'busy_hour_traffic_percentage': 20,
        'coverage_threshold': 100,
        'penetration': 80,
        'channel_bandwidth_700': '10',
        'channel_bandwidth_800': '10',
        'channel_bandwidth_1800': '10',
        'channel_bandwidth_2600': '10',
        'channel_bandwidth_3500': '40',
        'channel_bandwidth_3700': '40',
        'channel_bandwidth_26000': '200',
        'macro_sectors': 3,
        'small-cell_sectors': 1,
        'mast_height': 30,
    }

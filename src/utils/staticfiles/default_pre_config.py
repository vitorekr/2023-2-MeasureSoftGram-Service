# flake8: noqa
# pylint: skip-file
DEFAULT_PRE_CONFIG = {
    "characteristics": [
        {
            "key": "reliability",
            "weight": 50,
            "subcharacteristics": [
                {
                    "key": "testing_status",
                    "weight": 100,
                    "measures": [
                        {
                            "key": "passed_tests",
                            "weight": 33,
                            "min_threshold": 0,
                            "max_threshold": 1,
                        },
                        {
                            "key": "test_builds",
                            "weight": 33,
                            "min_threshold": 0,
                            "max_threshold": 300000,
                        },
                        {
                            "key": "test_coverage",
                            "weight": 34,
                            "min_threshold": 60,
                            "max_threshold": 100,
                        },
                    ],
                }
            ],
        },
        {
            "key": "maintainability",
            "weight": 50,
            "subcharacteristics": [
                {
                    "key": "modifiability",
                    "weight": 100,
                    "measures": [
                        {
                            "key": "non_complex_file_density",
                            "weight": 33,
                            "min_threshold": 0,
                            "max_threshold": 10,
                        },
                        {
                            "key": "commented_file_density",
                            "weight": 33,
                            "min_threshold": 10,
                            "max_threshold": 30,
                        },
                        {
                            "key": "duplication_absense",
                            "weight": 34,
                            "min_threshold": 0,
                            "max_threshold": 5,
                        },
                    ],
                }
            ],
        },
    ]
}

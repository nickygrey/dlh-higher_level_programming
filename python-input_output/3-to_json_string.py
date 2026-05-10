#!/usr/bin/python3
"""Module that returns JSON representation."""

import json


def to_json_string(my_obj):
    """Return JSON string of an object."""
    return json.dumps(my_obj)

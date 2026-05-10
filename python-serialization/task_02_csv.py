#!/usr/bin/env python3
"""Module for converting CSV data to JSON."""

import csv
import json


def convert_csv_to_json(filename):
    """Convert CSV file to JSON file."""
    try:
        data = []

        with open(filename, encoding="utf-8") as f:
            csv_reader = csv.DictReader(f)

            for row in csv_reader:
                data.append(row)

        with open("data.json", "w", encoding="utf-8") as json_file:
            json.dump(data, json_file)

        return True

    except Exception:
        return False

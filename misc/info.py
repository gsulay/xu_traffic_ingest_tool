from pathlib import Path


class EssentialData:
    TypeProperties = {
    "TVC: 4-Leg Intersection": {
        "template": Path(r"bin/essential data/4-Leg Template.xlsx"),
        "type": "4LI",
        "schema": Path(r"bin/database_format/tvc_schema.json")
    },
    "TVC: 3-Leg Intersection": {
        "template": Path(r"bin/essential data/3-Leg Template.xlsx"),
        "type": "3LI",
        "schema": Path(r"bin/database_format/tvc_schema.json")
    },
    "TVC: Midblock": {
        "template": Path(r"bin/essential data/Midblock Template.xlsx"),
        "type": "MB",
        "schema": Path(r"bin/database_format/tvc_schema.json")
    },
    "Spot Speed": {
        "template": Path(r"bin\essential data\SSS Template.xlsx"),
        "type": "SSS",
        "schema": Path(r"bin/database_format/SSS_schema.json")
    }
}




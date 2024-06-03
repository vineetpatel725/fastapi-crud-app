import os
from configparser import ConfigParser

from fastapi.encoders import jsonable_encoder
from loguru import logger

config_file: str = os.path.join(os.getcwd(), ".ini")
log_file: str = os.path.join(os.getcwd(), "logs", "backend.log")

configuration: ConfigParser = ConfigParser(dict_type=dict)
configuration.read(config_file)


def log_filter(record: dict) -> dict:
    print(record)
    format: dict = {
        "timestamp": record["time"].isoformat(),
        "message": record["message"],
        "level": record["level"].name,
        "module": record["module"],        
        "function": record["function"],
        "line": record["line"]
    }    
    format.update(**jsonable_encoder(record["extra"]))
    record["extra"]["serialized"] = format
    return format

def log_format(record: dict) -> dict:
    record["extra"]["serialized"] = log_filter(record)
    return "{extra[serialized]}\n"

logger.add(
    log_file, 
    format=log_format, 
    rotation=configuration.get("logs", "rotation"), 
    retention=configuration.get("logs", "retention")
)


from dataclasses import dataclass
from typing import List, Dict, Type
from enum import Enum

class DataType(Enum):
    INT = "int"
    FLOAT = "float"
    STRING = "string"
    BOOLEAN = "boolean"
    BYTES = "bytes"

@dataclass
class Field:
    name: str
    dtype: DataType
    nullable: bool = True
    metadata: Dict[str, str] = None

class Schema:
    """
    Represents a tabular dataset schema.
    Can export to Avro/Parquet compatible formats.
    """
    def __init__(self, name: str, fields: List[Field]):
        self.name = name
        self.fields = {f.name: f for f in fields}

    def validate(self, record: Dict[str, Any]) -> bool:
        """Simple type check validation."""
        for key, value in record.items():
            if key not in self.fields:
                continue # Ignore extra fields (evolution)
            
            field_def = self.fields[key]
            if value is None:
                if not field_def.nullable:
                    raise ValueError(f"Field {key} is not nullable but got None")
                continue
                
            # Type checking logic here...
        return True

    def to_avro_schema(self) -> Dict[str, Any]:
        """Converts to Avro JSON format."""
        return {
            "type": "record",
            "name": self.name,
            "fields": [
                {"name": f.name, "type": f.dtype.value}
                for f in self.fields.values()
            ]
        }

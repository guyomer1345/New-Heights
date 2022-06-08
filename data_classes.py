import json
from typing import Dict
from dataclasses import dataclass
from constants import SUCCESS, MSG, JSON_CONTENT_TYPE

@dataclass
class Response:
    success_status: bool
    msg: str
    status_code: int
    content_type: Dict[str, str]

    def build(self):
        return  json.dumps({SUCCESS: self.success_status, MSG: self.msg}), \
                    self.status_code, self.content_type

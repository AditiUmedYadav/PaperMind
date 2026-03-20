from dataclasses import dataclass
from typing import Optional
from datetime import datetime

@dataclass
class DocumentRecord:
    id: str
    user_id: str
    name: str
    original_filename: str
    file_type: str
    domain: str
    chroma_collection: str
    created_at: Optional[datetime] = None

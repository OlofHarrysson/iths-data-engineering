from datetime import date, datetime

import pydantic


class BlogInfo(pydantic.BaseModel):
    unique_id: str
    title: str
    description: str
    link: str
    blog_text: str
    published: date
    timestamp: datetime

    @property
    def filename(self) -> str:
        return f'{self.title.replace(" ", "_")}.json'

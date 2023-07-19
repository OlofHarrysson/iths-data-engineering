from datetime import date, datetime

import pydantic


class BlogInfo(pydantic.BaseModel):
    id: str
    title: str
    description: str
    link: str
    blog_text: str
    published: date
    timestamp: datetime

    class Config:
        frozen = True

    @property
    def filename(self) -> str:
        return f'{self.title.replace(" ", "_")}.json'


class BlogSummary(pydantic.BaseModel):
    title: str
    text: str

    @property
    def filename(self) -> str:
        return f'{self.title.replace(" ", "_")}.json'

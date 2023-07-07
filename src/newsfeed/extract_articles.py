from pathlib import Path

import jsonargparse
import pandas as pd
from bs4 import BeautifulSoup
from loguru import logger

from newsfeed import log_utils
from newsfeed.datatypes import BlogInfo


def load_metadata(blog_name: str) -> BeautifulSoup:
    metadata_path = Path("data/datasets") / blog_name / "metadata.xml"
    with open(metadata_path) as f:
        xml_text = f.read()

    parsed_xml = BeautifulSoup(xml_text, "xml")
    return parsed_xml


def extract_articles(parsed_xml: BeautifulSoup) -> list[BlogInfo]:
    articles = []
    for item in parsed_xml.find_all("item"):
        raw_blog_text = item.find("content:encoded").text
        soup = BeautifulSoup(raw_blog_text, "html.parser")
        blog_text = soup.get_text()
        article_info = BlogInfo(
            title=item.title.text,
            description=item.description.text,
            published=pd.to_datetime(item.pubDate.text).date(),
            link=item.link.text,
            blog_text=blog_text,
        )
        articles.append(article_info)

    return articles


def save_articles(articles: list[BlogInfo], blog_name: str) -> None:
    save_dir = Path("data/datasets", blog_name, "articles")
    save_dir.mkdir(exist_ok=True, parents=True)
    for article in articles:
        save_path = save_dir / article.filename
        with open(save_path, "w") as f:
            f.write(article.json(indent=2))


def main(blog_name: str) -> None:
    logger.info(f"Processing {blog_name}")
    parsed_xml = load_metadata(blog_name)
    articles = extract_articles(parsed_xml)
    save_articles(articles, blog_name)
    logger.info(f"Done processing {blog_name}")


def parse_args() -> jsonargparse.Namespace:
    parser = jsonargparse.ArgumentParser()
    parser.add_function_arguments(main)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    log_utils.configure_logger(log_level="DEBUG")
    main(**args)

import argparse
import requests
from datetime import datetime
from bs4 import BeautifulSoup
from bibtexparser.bwriter import BibTexWriter
from bibtexparser.bibdatabase import BibDatabase

BASE_URL = "http://export.arxiv.org/api/query?"


def search_papers(query, start=0, max_results=100):
    url = f"{BASE_URL}search_query={query}&start={start}&max_results={max_results}"
    data = requests.get(url).text
    return data


def convert_to_bib(content, save_fpath):
    papers = parse_api_response(content)
    db = BibDatabase()

    db.entries = papers
    writer = BibTexWriter()
    writer.indent = "    "
    writer.comma_first = True
    with open(save_fpath, "w+") as bibfile:
        bibfile.write(writer.write(db))


def parse_api_response(content):
    bs = BeautifulSoup(content)
    papers = list()

    entries = bs.find_all("entry")
    for entry in entries:
        paper_id = entry.find("id").text
        title = entry.find("title").text
        abstract = entry.find("summary").text
        entry_type = "article"
        published = entry.find("published").text
        published_date = datetime.strptime(published, "%Y-%m-%dT%H:%M:%SZ")
        year = str(published_date.year)
        month = str(published_date.month)
        authors = list()
        author_tags = entry.find_all("author")
        for tag in author_tags:
            authors.append(tag.find("name").text)

        papers.append(
            dict(
                title=title,
                abstract=abstract,
                year=year,
                month=month,
                author=", ".join(authors),
                ENTRYTYPE=entry_type,
                ID=paper_id,
            )
        )

    return papers


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--query", help="search query", required=True)
    parser.add_argument("--out", help="out bib file", required=True)
    parser.add_argument("--start", help="start index of the search", default=0)
    parser.add_argument("--max", help="max results", default=100)

    args = parser.parse_args()
    data = search_papers(args.query, args.start, args.max)
    convert_to_bib(data, args.out)

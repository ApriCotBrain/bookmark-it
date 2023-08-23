import requests
from bs4 import BeautifulSoup


def get_link_info(url):
    response = requests.get(url)
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    og_title = (
        soup.find("meta", property="og:title")["content"][:100]
        if soup.find("meta", property="og:title")
        else None
    )
    og_description = (
        soup.find("meta", property="og:description")["content"][:300]
        if soup.find("meta", property="og:description")
        else None
    )
    og_image = (
        soup.find("meta", property="og:image")["content"][:100]
        if soup.find("meta", property="og:image")
        else None
    )
    og_type = (
        soup.find("meta", property="og:type")["content"]
        if soup.find("meta", property="og:type")
        else None
    )

    if not og_title:
        og_title = soup.title.string if soup.title else None
    if not og_description:
        meta_description = soup.find("meta", attrs={"name": "description"})
        og_description = (
            meta_description["content"] if meta_description else None
        )

    data = {
        "title": og_title,
        "description": og_description,
        "image": og_image,
        "url_type": og_type,
    }
    return data

from deviantart_python_api import deviant_art
import requests

da = deviant_art.DeviantArt("24178", "7b472c20aea66646e9f9219c6c3da2c9")


def get_image_links_by_tag(tag, cursor=None, offset=None, limit=None, with_session: bool = False,
                           mature_content: bool = False) -> list:
    response = da.browse_tag(tag, cursor, offset, limit, with_session, mature_content)
    links = list(map(lambda x: x["content"]["src"], response["results"]))
    return links

def download_image(url, name):
    response = requests.get(url).content
    with open(name, "wb") as file:
        file.write(response)

if __name__ == "__main__":
    print(get_image_links_by_tag("anime"))
    download_image(get_image_links_by_tag("anime")[1], "aboba.png")
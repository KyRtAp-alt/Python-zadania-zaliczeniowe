import requests
import xml.etree.ElementTree as ET

def fetch_and_parse_xml(url):
    """Pobiera dane XML z podanego URL i zwraca korzeń drzewa XML."""
    response = requests.get(url)
    response.raise_for_status()
    return ET.fromstring(response.content)

def get_cd_tracks_and_artists(xml_root):
    """Zwraca liste par (wykonawca, tytul) dla każdego CD w kolekcji."""
    tracks_and_artists = []
    for cd in xml_root.findall('CD'):
        artist = cd.find('ARTIST').text
        title = cd.find('TITLE').text
        tracks_and_artists.append((artist, title))
    return tracks_and_artists

def main():
    url = "https://www.w3schools.com/xml/cd_catalog.xml"
    xml_root = fetch_and_parse_xml(url)
    tracks_and_artists = get_cd_tracks_and_artists(xml_root)

    for artist, title in tracks_and_artists:
        print(f"Artist: {artist}, Title: {title}")

if __name__ == "__main__":
    main()

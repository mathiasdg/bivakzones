"""
plaats een marker op de map voor elke bivakzone die GPS coordinaten op zijn pagina heeft
"""

import urllib.request
import re
from bs4 import BeautifulSoup as bs
import folium

# globals
ROOT_URL = "https://bivakzone.be"
# REGEX_LATLNG = "\s?(\d+)\s?(\d+)\.(\d{3})"
REGEX_DEC = "\d{1,2}\.\d{2,6}"
coords_belgium = [50.5 , 4.2]

# init map object
m = folium.Map(location=coords_belgium, zoom_start=8)

# open main page and get all the links to bivakzones
page = urllib.request.urlopen(ROOT_URL)
soup = bs(page, 'html.parser')
side_menu = soup.body.find('div', 'art-sidebar1')
links = side_menu.select("li a")

# go through all the links, visit the page, get the coords and add marker to the map
for link in links:
    bivak_url = ROOT_URL + link.get('href')
    page = urllib.request.urlopen(bivak_url)
    soup = bs(page, 'html.parser')

    coord_zoup = soup.body.find_all(string=re.compile(REGEX_DEC) )

    if len(coord_zoup) == 2:
        coords = coord_zoup[1].string.strip().split()
        folium.Marker(coords).add_to(m) 

        print(link.get('href'), coords)
        print('marker geplaatst')
    # , popup=popup, tooltip=tooltip, icon=icon
    else:
        print(link.get('href'))
        print(coord_zoup)
        print(len(coord_zoup))

    print(' ')


# for link in links:
#     bivak_url = ROOT_URL + link.get('href')
#     page = urllib.request.urlopen(bivak_url)
#     soup = bs(page, 'html.parser')

#     lat = soup.body.find(id='lat_dec')
#     lng = soup.body.find(id='long_dec')

#     if lat is None or lng is None:
#         coord_table = soup.body.find(string=re.compile(TEXT_TO_FIND))
#         coords = coord_table.parent.parent.parent.find_next_sibling().findChildren()
#         coords = coords[0].text
#         coords = coords.replace(u'\xa0', u' ').split(' ')
#         bivak_coords = [x for x in coords if x]
#     else:
#         bivak_coords = [lat.text.replace(u'\xa0', u' ').strip(), lng.text.replace(u'\xa0', u' ').strip()]

#     print(link.get('href'), bivak_coords, 'gelukt')

#     popup = f"Helaaaaaa bivakske"
#     # icon = folium.DivIcon(html=f"""""")
#     try:
#         folium.Marker(bivak_coords, popup=popup).add_to(m) # , popup=popup, tooltip=tooltip, icon=icon
#         print('geplaatst')
#     except:
#         print('geen marker voor deze plek')

# save the map as a html page
m.save('index.html')

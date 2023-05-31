import folium
import time

# functies
def get_direction(heading):

    if heading == 0:
        direction = "north"
    elif heading < 90:
        direction = "NE"
    elif heading == 90:
        direction = "east"
    elif 90 < heading < 180:
        direction = "SE"
    elif heading == 180:
        direction = "south"
    elif 180 < heading < 270:
        direction = "SW"
    elif heading == 270:
        direction = "west"
    elif 270 < heading <= 359:
        direction = "NW"
    else:
        direction = "foutje"

    return direction

# inits
start = time.perf_counter()

# popup = f"{fl.origin_airport_name} => {fl.destination_airport_name}\n{fl.status_text}"
# icon = folium.DivIcon(icon_anchor=[11,11], html=f"""<div style="transform: rotate({fl.heading}deg)"><svg width="22px" height="22px" viewBox="0 0 22 22" fill="none" xmlns="http://www.w3.org/2000/svg"><g id="SVGRepo_bgCarrier" stroke-width="0"></g><g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"></g><g id="SVGRepo_iconCarrier"> <path d="M20.0486 10.6286L15.3786 8.61859L14.3386 8.17859C14.1786 8.09859 14.0386 7.88859 14.0386 7.70859V4.64859C14.0386 3.68859 13.3286 2.54859 12.4686 2.10859C12.1686 1.95859 11.8086 1.95859 11.5086 2.10859C10.6586 2.54859 9.94859 3.69859 9.94859 4.65859V7.71859C9.94859 7.89859 9.80859 8.10859 9.64859 8.18859L3.94859 10.6386C3.31859 10.8986 2.80859 11.6886 2.80859 12.3686V13.6886C2.80859 14.5386 3.44859 14.9586 4.23859 14.6186L9.24859 12.4586C9.63859 12.2886 9.95859 12.4986 9.95859 12.9286V14.0386V15.8386C9.95859 16.0686 9.82859 16.3986 9.66859 16.5586L7.34859 18.8886C7.10859 19.1286 6.99859 19.5986 7.10859 19.9386L7.55859 21.2986C7.73859 21.8886 8.40859 22.1686 8.95859 21.8886L11.3386 19.8886C11.6986 19.5786 12.2886 19.5786 12.6486 19.8886L15.0286 21.8886C15.5786 22.1586 16.2486 21.8886 16.4486 21.2986L16.8986 19.9386C17.0086 19.6086 16.8986 19.1286 16.6586 18.8886L14.3386 16.5586C14.1686 16.3986 14.0386 16.0686 14.0386 15.8386V12.9286C14.0386 12.4986 14.3486 12.2986 14.7486 12.4586L19.7586 14.6186C20.5486 14.9586 21.1886 14.5386 21.1886 13.6886V12.3686C21.1886 11.6886 20.6786 10.8986 20.0486 10.6286Z" fill="#292D32"></path> </g></svg></div>""")
m = folium.Map(png_enabled=True, location=[50.5 , 4.2], zoom_start=8)
# folium.Marker(current_location, popup=popup, tooltip=tooltip, icon=icon).add_to(m)
m.save('map.html')

eind = time.perf_counter()
exec_time = (eind-start)

print(f"script klaar in {exec_time:0.3f} sec")
import json
import requests


def get_transport_duration_by_2_points(lat1, lon1, lat2, lon2):
    request_url = 'https://catalog.api.2gis.ru/ctx/2.0/moscow?key=rurbbn3446'
    payload = '{"locale":"ru","enable_schedule":false,"source":{"point":{"lon":37.719988,"lat":55.670641},"name":"Source"},"target":{"point":{"lat":55.759649,"lon":37.618869},"name":"Target"},"transport":["bus","trolleybus","tram","shuttle_bus","metro","suburban_train","funicular_railway","monorail","river_transport","cable_car","light_rail","premetro","light_metro","aeroexpress","pedestrian"],"purpose":"routeSearch","viewport":{"topLeft":{"x":37.61085909966919,"y":55.77371213472362},"bottomRight":{"x":37.72428990033081,"y":55.66302221564866},"zoom":11.953896721887604}}'
    payload2 = json.loads(payload)
    payload2["source"]["point"]["lon"] = lon1
    payload2["target"]["point"]["lon"] = lon2
    payload2["source"]["point"]["lat"] = lat1
    payload2["target"]["point"]["lat"] = lat2
    payload = json.dumps(payload2)
    data = requests.post(url=request_url, data=payload)
    print(data)
    response = json.loads(data.text)
    return json.dumps(response[1]['total_duration'], ensure_ascii=False)

# print(get_transport_duration_by_2_points(55.798268, 37.515227, 55.750045, 37.594422))

def get_pedestrian_duration_by_2_points(lat1, lon1, lat2, lon2):
    request_url = 'https://catalog.api.2gis.ru/pedestrian/4.0.0/moscow?key=rurbbn3446'
    payload = '{"locale":"ru","point_a_name":"Source","point_b_name":"Target","points":[{"type":"pedo","x":37.596729,"y":55.772405},{"type":"pedo","x":37.597138,"y":55.745815}],"type":"pedestrian","purpose":"autoSearch","viewport":{"topLeft":{"x":37.55657446863869,"y":55.78302312035535},"bottomRight":{"x":37.6426189622759,"y":55.729359960736176},"zoom":13.329834021667944}}'
    payload2 = json.loads(payload)
    payload2["points"][0]["x"] = lon1
    payload2["points"][1]["x"] = lon2
    payload2["points"][0]["y"] = lat1
    payload2["points"][1]["y"] = lat2
    payload = json.dumps(payload2)
    data = requests.post(url=request_url, data=payload)
    print(data)
    response = json.loads(data.text)
    return json.dumps(response["result"][0]["total_duration"], ensure_ascii=False)

# print(get_pedestrian_duration_by_2_points(55.772405, 37.596729, 55.745815, 37.597138))

def get_pedestrian_length_by_2_points(lat1, lon1, lat2, lon2):
    request_url = 'https://catalog.api.2gis.ru/pedestrian/4.0.0/moscow?key=rurbbn3446'
    payload = '{"locale":"ru","point_a_name":"Source","point_b_name":"Target","points":[{"type":"pedo","x":37.596729,"y":55.772405},{"type":"pedo","x":37.597138,"y":55.745815}],"type":"pedestrian","purpose":"autoSearch","viewport":{"topLeft":{"x":37.55657446863869,"y":55.78302312035535},"bottomRight":{"x":37.6426189622759,"y":55.729359960736176},"zoom":13.329834021667944}}'
    payload2 = json.loads(payload)
    payload2["points"][0]["x"] = lon1
    payload2["points"][1]["x"] = lon2
    payload2["points"][0]["y"] = lat1
    payload2["points"][1]["y"] = lat2
    payload = json.dumps(payload2)
    data = requests.post(url=request_url, data=payload)
    print(data)
    response = json.loads(data.text)
    return json.dumps(response["result"][0]["total_distance"], ensure_ascii=False)

# print(get_pedestrian_length_by_2_points(55.772405, 37.596729, 55.745815, 37.597138))

from yaweather import Russia, YaWeather

y = YaWeather(api_key='46f12ab0-64f7-4b95-8c20-6c4820c182b3')


def dump_request():
    dump_list = []
    city_list = [
        Russia.Moscow,
        Russia.SaintPetersburg,
        Russia.Novosibirsk,
        Russia.Yekaterinburg,
        Russia.NizhniyNovgorod
    ]

    for i in city_list:
        res = y.forecast(i)
        city = res.geo_object['locality']['name']

        dump_list.append({'city': city,
                          'temp': res.fact.temp,
                          'feels_like': res.fact.feels_like,
                          'condition': res.fact.condition
                          })
    return dump_list

from typing import List, AnyStr
import cnvrg.helpers.apis_helper as apis_helper
from cnvrg.helpers.url_builder_helper import url_join
try:
    import pandas as pd
    imported = True
except Exception as e:
    imported = False

class ChartsMixin(object):
    def __check_pandas(self):
        if not imported:
            raise Exception("Can't create chart without pandas, please run pip install pandas or add it to your requirements.txt")

    def catplot(self, key: AnyStr, data: pd.DataFrame, x: AnyStr, y: AnyStr, hue: AnyStr, title: AnyStr=None, x_axis: AnyStr=None, y_axis: AnyStr=None, y_ticks: List=None):
        group = list(filter(None, [hue, x]))
        data = data[data[y] == True].groupby(group).size()
        if hue:
            series = data.keys().levels[0]
            serieses = [{"name": s,"data": data[s].values.tolist()} for s in series]
            categories = data[series[0]].index.tolist()
        else:
            serieses = [{"name": "default", "data": data.values.tolist()}]
            categories = data.index.tolist()

        self.__create_chart(key, serieses=serieses, chart_type="bar", title=title, x_axis=x_axis, y_axis=y_axis, x_ticks=categories, y_ticks=y_ticks)


    def __list_to_series(self, x, name):
        return {
            "name": name,
            "data": x
        }


    def barplot(self, key: AnyStr, x: List, y: List, title: AnyStr=None, x_axis: AnyStr=None, y_axis: AnyStr=None):
        if isinstance(y[0], List):
            serieses = [self.__list_to_series(ys, "Series {}".format(idx)) for idx, ys in enumerate(y)]
        else:
            serieses = [self.__list_to_series(y, 'Series')]
        self.__create_chart(key, serieses=serieses, chart_type="bar", title=title, x_axis=x_axis, y_axis=y_axis,
                            x_ticks=x, y_ticks=None)











    def __create_chart(self, key, chart_type, serieses, title, x_axis, y_axis, x_ticks, y_ticks):
        data = {"chart": {"chart_type": chart_type, "title": title, "key": key, "serieses": serieses, "x_axis": x_axis, "y_axis": y_axis, "x_ticks": x_ticks, "y_ticks": y_ticks}}
        print(self._base_url())
        resp = apis_helper.post(url_join(self._base_url(), 'charts'), data=data)
        print(resp)
        return resp.get("chart")
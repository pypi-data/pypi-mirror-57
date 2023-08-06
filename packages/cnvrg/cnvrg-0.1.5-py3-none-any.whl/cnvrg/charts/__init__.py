from typing import List, AnyStr
import math

class BasicChart(object):
    def __init__(self, name="default"):
        self.__name = name

    def _sanitize_list(self, l):
        if hasattr(l, 'tolist'):
            return l.tolist()
        return l

    def set_series_index(self, idx):
        self.__name = self.__name or "Series {}".format(idx)


    @property
    def x_ticks(self):
        return None

    @property
    def y_ticks(self):
        return None

    @property
    def data(self):
        return []

    def as_series(self):
        return {
            "name": self.__name,
            "data": self.data
        }


class Barchart(BasicChart):
    def __init__(self, x: List, y: List, name: AnyStr=None):
        super(Barchart, self).__init__(name=name)
        self.__x = self._sanitize_list(x)
        self.__y = self._sanitize_list(y)


    @classmethod
    def chart_type(cls):
        return "bar"

    @property
    def x_ticks(self):
        return self.__x

    @property
    def data(self):
        return self.__y


class Heatmap(BasicChart):
    def __init__(self, z: List, name: AnyStr=None):
        super(Heatmap, self).__init__(name=name)
        self.__x = []
        self.__y = []
        self.__z = []
        self.__tokenize_list(self._sanitize_list(z))


    def __tokenize_list(self, l):
        for q in l:
            if(len(q) == 2):
                (x,y),z = q
            elif(len(q) == 3):
                x,y,z = q
            else:
                raise ValueError("Heatmap only support in values in type of ((x,y),z) or (x,y,z)")
            if math.isnan(z): continue
            if x not in self.__x:
                self.__x.append(x)
            if y not in self.__y:
                self.__y.append(y)
            self.__z.append((x, y, z))
        self.__x = sorted(self.__x)
        self.__y = sorted(self.__y)
        self.__z = [(self.__x.index(x), self.__y.index(y), z) for x,y,z in self.__z]

    @classmethod
    def chart_type(cls):
        return "heatmap"

    @property
    def x_ticks(self):
        return self.__x

    @property
    def y_ticks(self):
        return self.__y

    @property
    def data(self):
        return self.__z


class Scatterplot(BasicChart):
    def __init__(self, x: List, y: List, name: AnyStr=None):
        super(Scatterplot, self).__init__(name=name)
        self.__x = self._sanitize_list(x)
        self.__y = self._sanitize_list(y)

    @classmethod
    def chart_type(cls):
        return "scatter"

    @property
    def data(self):
        return list(zip(self.__x, self.__y))


class CategoricalScatterplot(Scatterplot):

    @property
    def x_axis(self):
        return sorted(list(set(self.__x)))

    @property
    def y_axis(self):
        return sorted(list(set(self.__y)))


    @property
    def data(self):
        x_ax = self.x_axis
        y_ax = self.y_axis
        x_i = list(map(lambda x: x_ax.index(x), self.__x))
        y_i = list(map(lambda y: y_ax.index(y), self.__y))
        return list(zip(x_i, y_i))



import collections
import math
import abc
import plotly.graph_objects as go


# Common variation series calculations
class VariationSeries:
    """Abstacrt"""
    def __init__(self, values: [dict, list], precision=5):
        self.precision = precision
        # User passes list of raw values
        if isinstance(values, list):
            self.vals = sorted(values)
            self.vs = self.build_vs_from_list(values)
        # User passes dict with a ready variation series
        elif isinstance(values, dict):
            self.vs = self.build_vs_from_dict(values)
            self.vals = []
            for x, n in self.vs.items():
                self.vals.extend([x]*n)

    def draw_cumulate(
            self, title='Кумулянта (заголовок)', name='Кумулянта (легенда)',
            x_label='Варианты', y_label='Накопленные частоты'
        ):
        """Draw cumulate: variants..closest_x => accumulated_frequencies"""
        x = self.variants + [self.closest_x]
        y = self.acc_frequencies
        VariationSeries._prepare_figure(x, y, title, name, x_label, y_label).show()
        return self

    def draw_empiric_dist_func(
            self, title='Эмпирическая функция распределения (заголовок)',
            name='Эмпирическая функция распределения (легенда)',
            x_label='Варианты', y_label='Частости'
        ):
        """Draw empiric distribution function: variants..closest_x => accumulated_relative_frequencies"""
        x = self.variants + [self.closest_x]
        y = self.acc_rel_frequencies
        VariationSeries._prepare_figure(x, y, title, name, x_label, y_label).show()
        return self

    @property
    def n(self) -> int:
        """Number of elements in the variation series"""
        return len(self.vals)

    @property
    def x_max(self) -> [float, int]:
        if isinstance(self.vals[0], tuple):
            return self.vals[-1][1]
        return max(self.vals)

    @property
    def x_min(self) -> [float, int]:
        if isinstance(self.vals[0], tuple):
            return self.vals[0][0]
        return min(self.vals)

    # Different for discrete and continuous vs
    @property
    @abc.abstractmethod
    def variants(self) -> list:
        """Variants x"""
        pass

    @property
    def acc_frequencies(self) -> list:
        """Accumulated frequencies m(x(i))"""

        def gen_acc_frequencies(values):
            """Generator of accumulated sum"""
            accumulated_sum = 0
            for m_i in values:
                yield accumulated_sum
                accumulated_sum += m_i
            yield accumulated_sum

        return list(gen_acc_frequencies(self.var_frequencies))

    @property
    def acc_rel_frequencies(self) -> list:
        """Accumulated relative frequencies w(x)"""
        n = self.n
        p = self.precision
        return [round(m_x / n, p) for m_x in self.acc_frequencies]

    @property
    def var_frequencies(self) -> list:
        """Variants frequencies m(i)"""
        return list(self.vs.values())

    @property
    def median(self) -> [int, float]:
        """Return median of the variation series"""
        n = self.n

        idx = n // 2
        if n % 2 == 0:
            idx -= 1
        return self.vals[idx]

    @property
    def mode(self) -> [int, float]:
        """Return mode of the variation series"""
        items = list(self.vs.items())
        mode_val, mode_reps = items[0]
        for val, reps in items:
            if mode_reps < reps:
                mode_val = val
                mode_reps = reps
        return mode_val

    @property
    @abc.abstractmethod
    def closest_x(self) -> [int, float]:
        """Return closests x value for accumulated functions"""
        pass

    @abc.abstractmethod
    def build_vs_from_list(self, values: list) -> 'collections.OrderedDict':
        """Build variation series from raw values"""
        pass

    @staticmethod
    def build_vs_from_dict(values: dict) -> 'collections.OrderedDict':
        """Build variation series from dict"""
        # User shoud be consient about values he passes
        vs = collections.OrderedDict(sorted(values.items()))
        return vs
    
    @staticmethod
    def _prepare_figure(x, y, title, name, x_label, y_label) -> 'go.Figure':
        fig = go.Figure()
        scatter = go.Scatter(x=x, y=y, mode='lines', name=name)
        fig.add_trace(scatter)
        fig.update_layout(title=title, xaxis_title=x_label, yaxis_title=y_label)
        return fig


# Discrete variation series
class DiscreteVS(VariationSeries):
    def draw_polygon(
        self, title='Полигон (заголовок)', name='Полигон (легенда)',
        x_label='Варианты', y_label='Частоты'
        ):
        """Draw polygon: variants => variants frequencies"""
        x = self.variants
        y = self.var_frequencies
        VariationSeries._prepare_figure(x, y, title, name, x_label, y_label).show()
        return self

    @property
    def variants(self) -> list:
        return list(self.vs.keys())

    @property
    def closest_x(self) -> [float, int]:
        """The closests x for accumulated values"""
        variants = self.variants
        penult, last = variants[-2:]
        diff = last - penult
        return last + diff

    def build_vs_from_list(self, values: list) -> 'collections.OrderedDict':
        vs = collections.OrderedDict()
        for val in sorted(values):
            vs[val] = vs.get(val, 0) + 1
        return vs


# Continuous variation series
class ContinuousVS(VariationSeries):
    def draw_hist(self, title='Гистограмма'):
        x = self.vals
        if isinstance(x[0], tuple):
            x = [x[0][0]] + [right for _, right in x]

        xbins = {
            'start': self.x_min, 'end': self.x_max,
            'size': self.delta,
        }
        trace = go.Histogram(x=x, xbins=xbins, autobinx=False)
        fig = go.Figure()
        fig.add_trace(trace)
        fig.show()
        return self

    @property
    def k(self) -> int:
        """Number of intervals"""
        return math.ceil(1 + 1.4*math.log(self.n))

    @property
    def delta(self) -> [float, int]:
        """Interval length"""
        return (self.x_max - self.x_min) / self.k

    @property
    def intervals(self) -> list:
        return list(self.vs.keys())

    @property
    def variants(self) -> list:
        return [left for left, right in self.intervals]

    @property
    def closest_x(self) -> [int, float]:
        return self.intervals[-1][1]

    def build_vs_from_list(self, values: list) -> 'collections.OrderedDict':
        """Build variation series from raw values"""
        # There are raw values
        p = self.precision
        delta = self.delta
        x_min = self.x_min
        x_max = self.x_max + delta/2

        intervals = []
        for i in range(self.k):
            bias = i * delta
            left = round(x_min + bias, p)
            right = round(x_min + bias + delta, p)
            intervals += [(left, right)]
        # Move the last interval for capturing
        last_interval = intervals[-1]
        new_last_interval = (last_interval[0], x_max)
        intervals[-1] = new_last_interval
        
        vs = collections.OrderedDict()  # Frequncies
        for val in sorted(self.vals):
            # Choose the correct interval
            for interval in intervals:
                left, right = interval
                if left <= val < right or val == x_max:
                    vs[interval] = vs.get(interval, 0) + 1
                    break
        return vs

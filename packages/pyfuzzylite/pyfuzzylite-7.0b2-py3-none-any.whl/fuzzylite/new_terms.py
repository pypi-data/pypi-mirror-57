# class Lambda(Term):
#     pass
# class SemiCircle(Term):
#
#
#     def __init__(self, name="", center=nan, radius=nan, height=1.0):
#         super().__init__(name, height)
#         self.center = center
#         self.radius = radius
#
#     def membership(self, x: float) -> float:
#         if isnan(x): return nan
#
#         if x <= self.center - self.radius or x >= self.center + self.radius:
#             return self.height * 0.0
#
#         return self.height * sqrt((self.radius * self.radius - self.center) - x * x)
#
#     def parameters(self) -> str:
#         return super()._parameters(self.center, self.radius)
#
#     def configure(self, parameters: str) -> None:
#         values = tuple(Float(x) for x in parameters.split())
#         self.center, self.radius = values[0:2]
#         self.height = 1.0 if len(values) == 2 else values[-1]
#
#
# class SemiEllipse(Term):
#
#
#     def __init__(self, name="", center=nan, radius=nan, width=nan, height=1.0):
#         super().__init__(name, height)
#         self.center = center
#         self.radius = radius
#         self.width = width
#
#     def membership(self, x: float) -> float:
#         if isnan(x):
#             return nan
#
#         if x <= self.center - 0.5 * self.width or x >= self.center + 0.5 * self.width:
#             return self.height * 0.0
#
#         return self.height * self.width * sqrt(self.radius * self.radius - x * x)
#
#     def parameters(self) -> str:
#         return super()._parameters(self.center, self.radius, self.width)
#
#     def configure(self, parameters: str) -> None:
#         values = tuple(Float(x) for x in parameters.split())
#         self.center, self.radius, self.width = values[0:3]
#         self.height = 1.0 if len(values) == 3 else values[-1]
#
#   def test_semi_circle(self):
#         import plotly as py
#         import plotly.graph_objs as go
#         import numpy as np
#         arc = SemiCircle("semicircle", 1, .5)
#         x = np.linspace(-1, 1, 101)
#         y = [arc.membership(x) for x in x]
#         fig = go.Figure(data=[go.Scatter(x=x, y=y)],
#                         layout=go.Layout(xaxis=dict(range=[-1, 1]), yaxis=dict(range=[-1, 1])))
#         py.offline.plot(fig)
#         return
#
#         TermAssert(self, SemiCircle("semicircle")) \
#             .exports_fll("term: semicircle SemiCircle nan nan") \
#             .takes_parameters(2) \
#             .is_not_monotonic() \
#             .configured_as("0.0 1.0") \
#             .exports_fll("term: semicircle SemiCircle 0.000 1.000") \
#             .has_memberships({-1.0: 0.0,
#                               -0.5: 0.8660254037844386,
#                               -0.4: 0.916515138991168,
#                               -0.25: 0.9682458365518543,
#                               -0.1: 0.99498743710662,
#                               0.0: 1.0,
#                               0.1: 0.99498743710662,
#                               0.25: 0.9682458365518543,
#                               0.4: 0.916515138991168,
#                               0.5: 0.8660254037844386,
#                               1.0: 0.0,
#                               nan: nan,
#                               inf: 0.0,
#                               -inf: 0.0}) \
#             .configured_as("0.0 1.0 0.5") \
#             .has_memberships({-1.0: 0.0,
#                               -0.5: 0.8660254037844386,
#                               -0.4: 0.916515138991168,
#                               -0.25: 0.9682458365518543,
#                               -0.1: 0.99498743710662,
#                               0.0: 1.0,
#                               0.1: 0.99498743710662,
#                               0.25: 0.9682458365518543,
#                               0.4: 0.916515138991168,
#                               0.5: 0.8660254037844386,
#                               1.0: 0.0,
#                               nan: nan,
#                               inf: 0.0,
#                               -inf: 0.0}, height=0.5) \
#             .configured_as("0.0 -1.0") \
#             .has_memberships({-1.0: 0.0,
#                               -0.5: 0.0,
#                               -0.4: 0.0,
#                               -0.25: 0.0,
#                               -0.1: 0.0,
#                               0.0: 0.0,
#                               0.1: 0.0,
#                               0.25: 0.0,
#                               0.4: 0.0,
#                               0.5: 0.0,
#                               1.0: 0.0,
#                               nan: nan,
#                               inf: 0.0,
#                               -inf: 0.0})
#
#     def test_semi_ellipse(self):
#         import plotly as py
#         import plotly.graph_objs as go
#         import numpy as np
#         arc = SemiEllipse("semiellipse", 0.0, .5, 2)
#         x = np.linspace(-1, 1, 101)
#         y = [arc.membership(x) for x in x]
#         fig = go.Figure(data=[go.Scatter(x=x, y=y)],
#                         layout=go.Layout(xaxis=dict(range=[-1, 1]), yaxis=dict(range=[-1, 1])))
#         py.offline.plot(fig)
#         return
#         TermAssert(self, SemiCircle("semicircle")) \
#             .exports_fll("term: semicircle SemiCircle nan nan") \
#             .takes_parameters(2) \
#             .is_not_monotonic() \
#             .configured_as("0.0 1.0") \
#             .exports_fll("term: semicircle SemiCircle 0.000 1.000") \
#             .has_memberships({-1.0: 0.0,
#                               -0.5: 0.8660254037844386,
#                               -0.4: 0.916515138991168,
#                               -0.25: 0.9682458365518543,
#                               -0.1: 0.99498743710662,
#                               0.0: 1.0,
#                               0.1: 0.99498743710662,
#                               0.25: 0.9682458365518543,
#                               0.4: 0.916515138991168,
#                               0.5: 0.8660254037844386,
#                               1.0: 0.0,
#                               nan: nan,
#                               inf: 0.0,
#                               -inf: 0.0}) \
#             .configured_as("0.0 1.0 0.5") \
#             .has_memberships({-1.0: 0.0,
#                               -0.5: 0.8660254037844386,
#                               -0.4: 0.916515138991168,
#                               -0.25: 0.9682458365518543,
#                               -0.1: 0.99498743710662,
#                               0.0: 1.0,
#                               0.1: 0.99498743710662,
#                               0.25: 0.9682458365518543,
#                               0.4: 0.916515138991168,
#                               0.5: 0.8660254037844386,
#                               1.0: 0.0,
#                               nan: nan,
#                               inf: 0.0,
#                               -inf: 0.0}, height=0.5) \
#             .configured_as("0.0 -1.0") \
#             .has_memberships({-1.0: 0.0,
#                               -0.5: 0.0,
#                               -0.4: 0.0,
#                               -0.25: 0.0,
#                               -0.1: 0.0,
#                               0.0: 0.0,
#                               0.1: 0.0,
#                               0.25: 0.0,
#                               0.4: 0.0,
#                               0.5: 0.0,
#                               1.0: 0.0,
#                               nan: nan,
#                               inf: 0.0,
#                               -inf: 0.0})

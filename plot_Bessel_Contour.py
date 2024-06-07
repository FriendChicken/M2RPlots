from manim import *

class CombineCurves(Scene):
    def construct(self):
        # Define two curves
        axes = Axes(
            x_range=[-2.3, 2.3,2.3],
            y_range=[-4, 4,4],
            x_axis_config={"numbers_to_include": np.zeros(1,)},
            y_axis_config={"numbers_to_include": np.zeros(1,)},
        )
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        a=2
        curve1 = [ParametricFunction(lambda t: np.array([np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[0, 1], color=BLUE),
        ParametricFunction(lambda t: np.array([-np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[1, 1.99], color=BLUE)]
        a=-2
        curve2 = [ParametricFunction(lambda t: np.array([np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[-1, 0], color=ORANGE),
        ParametricFunction(lambda t: np.array([-np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[-1.99, -1], color=ORANGE)]
        a=-3
        curve3 = ParametricFunction(lambda t:  np.array([t, np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[-3.25, -3.01], color=RED)

        # Find intersection point
        #intersection_point = curve1.get_end()

        # Create combined curve up to the intersection point
        """
        combined_curve = ParametricFunction(lambda t: np.array([t, np.sin(t) + np.cos(t), 0]), t_range=[-TAU, intersection_point[0]], color=GREEN)

        # Erase parts of original curves after intersection point
        curve1_erased = curve1.copy().pointwise_become_partial(curve1, 0, curve1.t_from_x(intersection_point[0]))
        curve3_erased = curve3.copy().pointwise_become_partial(curve3, 0, curve3.t_from_x(intersection_point[0]))"""
        self.add(
            *curve1,
            *curve2,
            curve3
        )
        self.wait()
        """
        self.play(
            ReplacementTransform(curve1, curve1_erased),
            ReplacementTransform(curve2, curve2_erased),
            Create(combined_curve)
        )
        self.wait()"""

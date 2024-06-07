from manim import *

class CombineCurves(Scene):
    def construct(self):
        # Define two curves
        curve1 = ParametricFunction(lambda t: np.array([t, np.sin(t), 0]), t_range=[-TAU, TAU], color=BLUE)
        curve2 = ParametricFunction(lambda t: np.array([t, np.cos(t), 0]), t_range=[-TAU, TAU], color=RED)

        # Find intersection point
        intersection_point = curve1.get_end()

        # Create combined curve up to the intersection point
        combined_curve = ParametricFunction(lambda t: np.array([t, np.sin(t) + np.cos(t), 0]), t_range=[-TAU, intersection_point[0]], color=GREEN)

        # Erase parts of original curves after intersection point
        curve1_erased = curve1.copy().pointwise_become_partial(curve1, 0, curve1.t_from_x(intersection_point[0]))
        curve2_erased = curve2.copy().pointwise_become_partial(curve2, 0, curve2.t_from_x(intersection_point[0]))

        self.play(
            Create(curve1),
            Create(curve2)
        )
        self.wait()

        self.play(
            ReplacementTransform(curve1, curve1_erased),
            ReplacementTransform(curve2, curve2_erased),
            Create(combined_curve)
        )
        self.wait()

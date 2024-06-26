from manim import *
epsilon = 0.5
class GraphExample(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-0.2, 3.3],
            y_range=[-1.5, 0.2],
            x_axis_config={"numbers_to_include": np.arange(0, 4, 1)},
            y_axis_config={"numbers_to_include": np.arange(-1, 1, 1)},
        )
        labels = axes.get_axis_labels(
            x_label=Tex("$t$"), y_label=Tex("$y$")
        )
        self.play(Write(axes, lag_ratio=0.01, run_time=1))

        # Axes.get_graph will return the graph of a function
        def h_func(x):
            return np.log(x)-x+1
        sin_graph = axes.plot(
            h_func,
            x_range=[0.01,4,0.01],
            color=BLUE,
            use_smoothing = True
        )
        dot_1 = Dot(color=WHITE)
        dot_1.move_to(axes.c2p(1-epsilon, h_func(1-epsilon)))
        dot_2 = Dot(color=WHITE)
        dot_2.move_to(axes.c2p(1+epsilon, h_func(1+epsilon)))
        self.play(FadeIn(dot_1, scale=0.5))
        self.play(FadeIn(dot_2, scale=0.5))
        Ldot_1 = Dot(color=WHITE)
        Ldot_1.move_to(axes.c2p(1-epsilon, 0))
        Ldot_2 = Dot(color=WHITE)
        Ldot_2.move_to(axes.c2p(1+epsilon, 0))
        line_1 = axes.get_vertical_line(axes.input_to_graph_point(1-epsilon, sin_graph), color=YELLOW)
        line_2 = axes.get_vertical_line(axes.i2gp(1+epsilon, sin_graph), color=YELLOW)
        self.play(FadeIn(Ldot_1, scale=0.5))
        self.play(FadeIn(Ldot_2, scale=0.5))
        dot1_labelText=MathTex('1-\epsilon').next_to(Ldot_1, UP)
        dot2_labelText=MathTex('1+\epsilon').next_to(Ldot_2, UP)
        """bound_labels = [Tex("a"),Tex("b")]
        bound_labels[0].add_updater(lambda m: m.move_to(line_1, DOWN).shift(0.5 * DOWN))
        bound_labels[1].add_updater(lambda m: m.move_to(line_2, DOWN).shift(0.5 * DOWN))
        line_1 = axes.plot_line_graph(x_values=[1-epsilon], y_values=[0,h_func(1-epsilon)])
        line_2 = axes.plot_line_graph(x_values=[1+epsilon], y_values=[0,h_func(1+epsilon)])"""
        sin_label = axes.get_graph_label(sin_graph, "h(t)", x_val=2.5)
        self.add(sin_graph,sin_label,labels,line_1,line_2,dot1_labelText,dot2_labelText)
from manim import *
class GraphExample(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-3.3, 3.3],
            y_range=[-0.5, 3,3],
            x_axis_config={"numbers_to_include": np.arange(-3, 4, 1)},
            y_axis_config={"numbers_to_include": np.arange(-1, 4, 1)},
        )
        labels = axes.get_axis_labels(
            x_label=Tex("$t$"), y_label=Tex("$y$")
        )
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        for i in [1,5,10,20,100,200]:
            def integrand_func(x):
                return np.exp(i*(np.log(x)-x+1)
            integrand_graph = axes.plot(
            integrand_func,
            x_range=[-4,4,0.01],
            color=RED,
            use_smoothing = True
            )
            integrand_func.set_opacity(0.99-1/i)
            label = axes.get_graph_label(integrand_graph, "x = "+ str(i))
            self.play(Create(integrand_graph),label)
        self.wait()
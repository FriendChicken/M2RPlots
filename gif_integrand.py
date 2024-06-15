from manim import *
MAX_X=1000
class GraphExample(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            x_range=[-0.3, 3.3],
            y_range=[-0.5, 1.3],
            axis_config={"color": BLACK},
            x_axis_config={"numbers_to_include": np.arange(0, 4, 1)},
            y_axis_config={"numbers_to_include": np.arange(-1, 2, 1)},
        )
        labels = axes.get_axis_labels(
            x_label=Tex("$t$", fill_color=BLACK), y_label=Tex("$y$", fill_color=BLACK)
        )
        x_axes = axes.get_x_axis()
        y_axes = axes.get_y_axis()
        x_axes.numbers.set_color(BLACK)
        y_axes.numbers.set_color(BLACK)
        self.add(axes)

        big_x = ValueTracker(1)
        
        start_color = DARK_BLUE
        end_color = RED
        plot_color = lambda : interpolate_color(start_color, end_color, big_x.get_value() / 200)
        
        def integrand_func(x):
            if not x:
                return 0
            return np.exp(big_x.get_value()*(np.log(x)-x+1))
        label = always_redraw(
            lambda : MathTex("x = " + str(round(big_x.get_value())), color = plot_color()).next_to(axes.c2p(2.7,1)))

        integrand_graph = always_redraw(
            lambda : axes.plot(
            integrand_func,
            x_range=[0,4,0.01],
            color=plot_color(),
            use_smoothing = True
            )
        )
        self.add(label, integrand_graph)
        title = Text("Graph of integrands as x increases", font_size=30)
        title.to_edge(UP)
        self.add(title)
        self.play(big_x.animate.set_value(MAX_X), rate_func = rate_functions.ease_in_quint, run_time = 3)
        self.wait(1)
        self.play(big_x.animate.set_value(1), rate_func = rate_functions.ease_out_quint, run_time = 3)
        self.wait(1)
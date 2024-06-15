from manim import *
MAX_X=1000
epsilon = 0.2
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
            x_label=Tex("$t$", fill_color=BLACK), y_label=Tex("$h(t)$", fill_color=BLACK)
        )
        x_axes = axes.get_x_axis()
        y_axes = axes.get_y_axis()
        x_axes.numbers.set_color(BLACK)
        y_axes.numbers.set_color(BLACK)
        self.add(axes,labels)

        big_x = ValueTracker(100)
        
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
        dot_1 = Dot(color=BLACK)
        dot_1.move_to(axes.c2p(1-epsilon, integrand_func(1-epsilon)))
        dot_2 = Dot(color=BLACK)
        dot_2.move_to(axes.c2p(1+epsilon, integrand_func(1+epsilon)))
        #self.play(FadeIn(dot_1, scale=0.5))
        #self.play(FadeIn(dot_2, scale=0.5))
        Ldot_1 = Dot(color=BLACK)
        Ldot_1.move_to(axes.c2p(1-epsilon, 0))
        Ldot_2 = Dot(color=BLACK)
        Ldot_2.move_to(axes.c2p(1+epsilon, 0))
        """line_1 = axes.get_vertical_line(axes.input_to_graph_point(1-epsilon, integrand_graph), color=BLACK)
        line_2 = axes.get_vertical_line(axes.i2gp(1+epsilon, integrand_graph), color=BLACK)"""
        line_1 = DashedLine(dash_length=0.2,
                start = axes.c2p(1-epsilon, config.bottom[1], 0),
                end = axes.c2p(1-epsilon, config.top[1], 0),
                color = BLACK
            )
        line_2 = DashedLine(dash_length=0.2,
                start = axes.c2p(1+epsilon, config.bottom[1]),
                end = axes.c2p(1+epsilon, config.top[1]),
                color = BLACK
            )
        self.play(FadeIn(Ldot_1, scale=0.5))
        self.play(FadeIn(Ldot_2, scale=0.5))
        dot1_labelText=MathTex('1-\delta', fill_color=BLACK, font_size = 36).next_to(Ldot_1, DOWN + LEFT)
        dot2_labelText=MathTex('1+\delta', fill_color=BLACK, font_size = 36).next_to(Ldot_2, DOWN + RIGHT)
        #area = axes.get_area(integrand_graph, [1-epsilon, 1+epsilon], color=YELLOW, opacity=0.5)
        area_1 = axes.get_area(integrand_graph, [0.1, 1-epsilon], color=BLUE, opacity=0.5)
        area_2 = axes.get_area(integrand_graph, [1+epsilon,100], color=BLUE, opacity=0.5)
        self.add(line_1,line_2,dot1_labelText,dot2_labelText,area_1, area_2)
        """title = Text("Graph of integrands as x increases", font_size=30)
        title.to_edge(UP)
        self.add(title)"""
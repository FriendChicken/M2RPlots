from manim import *
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
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        x_list=[1,5,25,125,625,3125]
        all_labels = []
        all_x = [-1,-0.7,-0.4,0,0.4,0.9]
        all_x_val = [3,2,1.35,1.11,1.03,1]
        all_graph = []
        start_color = DARK_BLUE
        end_color = RED
        for i in range(len(x_list)):
            def integrand_func(x):
                if not x:
                    return 0
                return np.exp(x_list[i]*(np.log(x)-x+1))
            integrand_graph = axes.plot(
            integrand_func,
            x_range=[0,4,0.01],
            color=interpolate_color(start_color, end_color, i / len(x_list)),
            use_smoothing = True
            )
            #integrand_graph.set_stroke(opacity = 1/3 + i*(2/3) / len(x_list))
            label = axes.get_graph_label(integrand_graph, label =MathTex("x = "+ str(x_list[i])),x_val=all_x_val[i])
            all_labels.append(label)
            all_graph.append(integrand_graph)
        all_labels[0].shift(DOWN)
        arrow = Arrow(start=[3.5, 0.5,0], end=[-1, 0.5,0], color=BLACK)
        self.add(labels,arrow,*all_graph, *all_labels)
        title = Text("Graph of integrands as x increases", font_size=30)
        title.to_edge(UP)
        self.add(title)
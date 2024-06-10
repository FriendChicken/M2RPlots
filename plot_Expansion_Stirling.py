from manim import *
epsilon = 0.5
class GraphExample(Scene):
    def construct(self):
        axes = Axes(
            [0,5],
            [0,13],
            10,
            7,
            x_axis_config={"numbers_to_include": np.arange(0, 5, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 13, 1)}
        )
        labels = axes.get_axis_labels(
            x_label=Tex("$n$")
        )
        self.add(axes, labels)
        """plane = NumberPlane(
            x_range = (0, 5),
            y_range = (0, 14),
            x_length = 7,
            y_length = 7,
            axis_config={"include_numbers": True},
        )
        self.add(plane)
        Stirling_graph = ParametricFunction(lambda t: np.array([t,St_func(t),0]), t_range=[0,4], color=WHITE)
        Stirling_label = plane.get_graph_label(Stirling_graph, "Stirling Aprox.")
        """

        # Axes.get_graph will return the graph of a function
        def St_func(x):
            return np.sqrt(2*np.pi)*np.power((x+1),(x+0.5))*np.exp(-x-1)*np.exp(1/(12*(x+1)))
        Stirling_graph = axes.plot(
            St_func, 
            x_range=[0,4],
            color = WHITE
        )
        Stirling_label = axes.get_graph_label(Stirling_graph, Tex("Stirling Aprox."))
        self.add(Stirling_graph,Stirling_label)
        ans =1
        for i in range(1,4):
            ans*=i
            dot = Dot(color=WHITE)
            pos = axes.c2p(i,ans)
            dot.move_to(pos)
            line_v = axes.get_vertical_line(pos,color=BLUE)
            line_h = axes.get_horizontal_line(pos,color=BLUE)
            self.add(line_v,line_h,dot)
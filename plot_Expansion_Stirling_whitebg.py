from manim import *
from math import gamma
epsilon = 0.5
class GraphExample(Scene):
    def construct(self):
        self.camera.background_color = WHITE
        axes = Axes(
            [0,4],
            [0,7],
            10,
            7,
            axis_config={"color":BLACK},
            x_axis_config={"numbers_to_include": np.arange(0, 4, 1)},
            y_axis_config={"numbers_to_include": np.arange(0, 7, 1)}
        )
        x_axes = axes.get_x_axis()
        y_axes = axes.get_y_axis()
        x_axes.numbers.set_color(BLACK)
        y_axes.numbers.set_color(BLACK)
        labels = axes.get_axis_labels(
            x_label=Tex("$n$",color=BLACK),
            y_label=Tex("$y$",color=BLACK)
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
            color = BLACK
        )
        Stirling_label = axes.get_graph_label(Stirling_graph, Tex("Stirling Aprox."),x_val=2.5,direction=UP+LEFT)
        self.add(Stirling_graph,Stirling_label)
        
        gamma_graph = axes.plot(
            lambda t:gamma(t+1), 
            x_range=[0,4],
            color = BLACK
        )
        gamma_label = axes.get_graph_label(gamma_graph, MathTex("Gamma(n)"),x_val=2.5,direction=UP+LEFT)
        self.add(gamma_graph,gamma_label)
        ans =1
        for i in range(1,4):
            ans*=i
            dot = Dot(color=BLACK)
            pos = axes.c2p(i,ans)
            dot.move_to(pos)
            line_v = axes.get_vertical_line(pos,color=BLACK)
            line_h = axes.get_horizontal_line(pos,color=BLACK)
            self.add(line_v,line_h,dot)
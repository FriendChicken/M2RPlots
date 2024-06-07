from manim import *

class CombinedGraphs(Scene):
    def construct(self):
        # Create axes
        axes = Axes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            axis_config={"color": BLUE}
        )

        # Define two functions
        def func1(x):
            return np.sin(x)

        def func2(x):
            return 0.5 * x ** 2

        # Create graphs for the functions
        graph1 = axes.plot(func1, color=YELLOW)
        graph2 = axes.plot(func2, color=GREEN)

        # Define a smooth transition function
        def smooth_transition(x, alpha=0.5):
            return alpha * func1(x) + (1 - alpha) * func2(x)

        # Create the combined graph with smooth transition
        combined_graph = axes.plot(lambda x: smooth_transition(x), color=RED)

        # Add labels for the graphs
        label1 = axes.get_graph_label(graph1, label="sin(x)", x_val=2, direction=UP)
        label2 = axes.get_graph_label(graph2, label="0.5x^2", x_val=-2, direction=UP)
        combined_label = axes.get_graph_label(combined_graph, label="Combined", x_val=0, direction=UP)

        # Add axes and graphs to the scene
        self.play(Create(axes))
        self.play(Create(graph1), Write(label1))
        self.play(Create(graph2), Write(label2))
        self.play(Create(combined_graph), Write(combined_label))

        # Hold the final frame
        self.wait(2)

if __name__ == "__main__":
    scene = CombinedGraphs()
    scene.render()

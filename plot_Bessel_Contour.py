from manim import *
little_e=0.000001
R_length=5
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
        curve = Circle(radius=1.0, color = WHITE)
        #ParametricFunction(lambda t: np.array([np.cos(t), np.sin(t), 0]), t_range=[-1, 1], color = GREEN)
        a=2
        curve1 = [ParametricFunction(lambda t: np.array([np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[0, 1], color=BLUE),
        ParametricFunction(lambda t: np.array([-np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[1, 1.99], color=BLUE)]
        a=-2
        curve2 = [ParametricFunction(lambda t: np.array([np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[-1, 0], color=BLUE),
        ParametricFunction(lambda t: np.array([-np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[-1.99, -1], color=BLUE)]
        a=-R_length
        curve3 = [ParametricFunction(lambda t:  np.array([t, np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[-np.sqrt(1+(a/2)**2)+a/2+little_e, a-0.01], color=RED),
        ParametricFunction(lambda t:  np.array([t, -np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[-np.sqrt(1+(a/2)**2)+a/2+little_e, a-0.01], color=RED)]
        curve4 = [ParametricFunction(lambda t:  np.array([t, np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[little_e,np.sqrt(1+(a/2)**2)+a/2-little_e], color=RED),
        ParametricFunction(lambda t:  np.array([t, -np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[little_e,np.sqrt(1+(a/2)**2)+a/2-little_e], color=RED)]
        # Find intersection point
        #intersection_point = curve1.get_end()

        intersection_2_3=Intersection(curve2[1],curve3[1]).get_start()
        intersection_1_3=intersection_2_3.copy()
        intersection_1_3[1]=-intersection_1_3[1]
        intersection_1_4=Intersection(curve1[0],curve4[0]).get_start()
        intersection_2_4=intersection_1_4.copy()
        intersection_2_4[1]=-intersection_2_4[1]

        modified_curve=[[None,None],[None,None],[None,None],[None,None]]
        print(modified_curve)

        a=2
        modified_curve[0][1]=ParametricFunction(lambda t: np.array([-np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[1, intersection_1_3[1]], color=BLUE)
        a=-R_length
        modified_curve[2][0]=ParametricFunction(lambda t:  np.array([t, np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[-np.sqrt(1+(a/2)**2)+a/2+little_e, intersection_1_3[0]], color=RED)
        
        print(intersection_1_4)
        a=2
        modified_curve[0][0]=ParametricFunction(lambda t: np.array([np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[intersection_1_4[1], 1], color=BLUE)
        a=-R_length
        modified_curve[3][0]=ParametricFunction(lambda t:  np.array([t, np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[intersection_1_4[0],np.sqrt(1+(a/2)**2)+a/2-little_e], color=RED)
        
        intersection_2_3=Intersection(curve2[1],curve3[1]).get_start()
        a=-2
        modified_curve[1][1]=ParametricFunction(lambda t: np.array([-np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[intersection_2_3[1], -1], color=BLUE)
        a=-R_length
        modified_curve[2][1]=ParametricFunction(lambda t:  np.array([t, -np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[-np.sqrt(1+(a/2)**2)+a/2+little_e, intersection_2_3[0]], color=RED)

        a=-2
        modified_curve[1][0]=ParametricFunction(lambda t: np.array([np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[-1, intersection_2_4[1]], color=BLUE)
        a=-R_length
        modified_curve[3][1]=ParametricFunction(lambda t:  np.array([t, -np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[intersection_2_4[0],np.sqrt(1+(a/2)**2)+a/2-little_e], color=RED)

        labels=[]
        for i in range(4):
            c = modified_curve[i][1]
            tr = c.t_range
            if i>1:
                x_val = (tr[0] + tr[1]) / 2
            else:
                a=2
                f = lambda t: -np.sqrt((a*t**2-t**3-t)/(t-a))
                x_val = (f(tr[0])+f(tr[1]))/2
            labels.append(axes.get_graph_label(c, MathTex("C_"+str(i+1)),xval=x_val))
        self.add(
            curve,
            *sum(modified_curve,[]),
            *labels
        )
        self.wait()

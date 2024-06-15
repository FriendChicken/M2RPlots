from manim import *
little_e=0.000001
R_length=2
class CombineCurves(ZoomedScene):
    def __init__(self, **kwargs):
        ZoomedScene.__init__(
            self,
            zoom_factor=0.2,
            zoomed_display_height=2,
            zoomed_display_width=2,
            image_frame_stroke_width=0,
            zoomed_camera_config={
                "default_frame_stroke_width": 3,
                },
            **kwargs
        )
    def construct(self):
        # Define two curves
        self.camera.background_color = WHITE
        self.zoomed_camera.background_color = WHITE
        axes = Axes(
            x_range=[-4, 4,4],
            y_range=[-3, 3,3],
            x_length=7,
            axis_config={"color": BLACK, "include_numbers":False},
        )
        ax_labels = axes.get_axis_labels(
            x_label=Tex("$Re$",color = BLACK), y_label=Tex("$Im$",color = BLACK)
        )
        """x_axes = axes.get_x_axis()
        y_axes = axes.get_y_axis()
        x_axes.numbers.set_color(BLACK)
        y_axes.numbers.set_color(BLACK)"""
        self.play(Write(axes, lag_ratio=0.01, run_time=1))
        curve = Circle(radius=axes.c2p(0,1)[1], color = GRAY)
        self.add(curve)
        
        #ParametricFunction(lambda t: np.array([np.cos(t), np.sin(t), 0]), t_range=[-1, 1], color = GREEN)
        a=2
        curve1 = [ParametricFunction(lambda t: np.array([np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[0, 1], color=BLUE),
        ParametricFunction(lambda t: np.array([-np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[1, 1.99], color=BLUE),
        ParametricFunction(lambda t: np.array([-np.sqrt((a*t**2-t**3-t)/(t-a)), -t, 0]), t_range=[0, 1.99], color=BLUE),
        ParametricFunction(lambda t: np.array([np.sqrt((a*t**2-t**3-t)/(t-a)), -t, 0]), t_range=[0, 1.99], color=BLUE)]
        a=-2
        curve2 = [ParametricFunction(lambda t: np.array([np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[-1, 0], color=BLUE),
        ParametricFunction(lambda t: np.array([-np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[-1.99, -1], color=BLUE),
        ParametricFunction(lambda t: np.array([-np.sqrt((a*t**2-t**3-t)/(t-a)), -t, 0]), t_range=[-1.99, 0], color=BLUE),
        ParametricFunction(lambda t: np.array([np.sqrt((a*t**2-t**3-t)/(t-a)), -t, 0]), t_range=[-1.99, 0], color=BLUE)]
        a=-R_length
        curve3 = [ParametricFunction(lambda t:  np.array([t, np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[-np.sqrt(1+(a/2)**2)+a/2+little_e, a-0.01], color=RED),
        ParametricFunction(lambda t:  np.array([t, -np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[-np.sqrt(1+(a/2)**2)+a/2+little_e, a-0.01], color=RED)]
        curve4 = [ParametricFunction(lambda t:  np.array([t, np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[little_e,np.sqrt(1+(a/2)**2)+a/2-little_e], color=RED),
        ParametricFunction(lambda t:  np.array([t, -np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[little_e,np.sqrt(1+(a/2)**2)+a/2-little_e], color=RED)]
        

        # Find intersection point
        intersection_2_3=Intersection(curve2[1],curve3[1]).get_start()
        intersection_1_3=intersection_2_3.copy()
        intersection_1_3[1]=-intersection_1_3[1]
        intersection_1_4=Intersection(curve1[0],curve4[0]).get_start()
        intersection_2_4=intersection_1_4.copy()
        intersection_2_4[1]=-intersection_2_4[1]

        modified_curve=[[None,None],[None,None],[None,None],[None,None]]

        a=2
        tr=[None]*4
        tr[0]=[1, intersection_1_3[1]]
        modified_curve[0][1]=ParametricFunction(lambda t: np.array([-np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=tr[0], color=BLUE)
        a=-R_length
        modified_curve[2][0]=ParametricFunction(lambda t: np.array([t, np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[-np.sqrt(1+(a/2)**2)+a/2+little_e, intersection_1_3[0]], color=RED)
        
        a=2
        modified_curve[0][0]=ParametricFunction(lambda t: np.array([np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[intersection_1_4[1], 1], color=BLUE)
        a=-R_length
        modified_curve[3][0]=ParametricFunction(lambda t: np.array([t, np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=[intersection_1_4[0],np.sqrt(1+(a/2)**2)+a/2-little_e], color=RED)
        
        intersection_2_3=Intersection(curve2[1],curve3[1]).get_start()
        a=-2
        tr[1]=[intersection_2_3[1], -1]
        modified_curve[1][1]=ParametricFunction(lambda t: np.array([-np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=tr[1], color=BLUE)
        a=-R_length
        tr[2]=[-np.sqrt(1+(a/2)**2)+a/2+little_e, intersection_2_3[0]]
        modified_curve[2][1]=ParametricFunction(lambda t: np.array([t, -np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=tr[2], color=RED)

        a=-2
        modified_curve[1][0]=ParametricFunction(lambda t: np.array([np.sqrt((a*t**2-t**3-t)/(t-a)), t, 0]), t_range=[-1, intersection_2_4[1]], color=BLUE)
        a=-R_length
        tr[3]=[intersection_2_4[0],np.sqrt(1+(a/2)**2)+a/2-little_e]
        modified_curve[3][1]=ParametricFunction(lambda t: np.array([t, -np.sqrt((a*t**2-t**3+t)/(t-a)), 0]), t_range=tr[3], color=RED)

        labels=[]
        print(tr)
        """
        for i in range(4):
            c = modified_curve[i][1]
            x_val = (axes.p2c(c.get_start())[0]+ axes.p2c(c.get_end())[0])/2
            print(x_val)
            labels.append(axes.get_graph_label(c, MathTex("C_"+str(i+1)),x_val=x_val,direction=UP+LEFT))
        labels.append(axes.get_graph_label(curve, MathTex("C"), x_val=axes.p2c(curve.get_start())[0],direction=UP+RIGHT))
        """
        c = modified_curve[0][1]
        x_val = (axes.p2c(c.get_start())[0]+ axes.p2c(c.get_end())[0])/2
        print(x_val)
        labels.append(axes.get_graph_label(c, MathTex("Im(f)=2"),x_val=x_val,direction=UP*2+LEFT))
        c = modified_curve[1][1]
        x_val = (axes.p2c(c.get_start())[0]+ axes.p2c(c.get_end())[0])/2
        print(x_val)
        labels.append(axes.get_graph_label(c, MathTex("Im(f)=-2"),x_val=x_val,direction=DOWN*2+LEFT))
        labels.append(axes.get_graph_label(curve, MathTex("C"), x_val=axes.p2c(curve.get_start())[0],direction=UP+RIGHT))
        linep_labelText=MathTex('z=2i', fill_color=BLACK)
        linen_labelText=MathTex('z=-2i', fill_color=BLACK)
        linep_labelText.move_to(axes.c2p(2,2.5))
        linen_labelText.move_to(axes.c2p(2,-2.5))
        """
        self.add(
            ax_labels,
            curve,
            *sum(modified_curve,[]),
            *labels
        )"""
        line_1 = TangentLine(curve1[1], alpha=0, length=1, color=GREEN) # right
        line_2 = TangentLine(curve2[1], alpha=1, length=1, color=GREEN) # top left
        #self.add(line_1, line_2)
        
        saddle = [Dot(color=BLACK),Dot(color=BLACK)]
        saddle[0].move_to(axes.c2p(0,1))
        saddle[1].move_to(axes.c2p(0,-1))
        saddle_label=[MathTex('i', color=BLACK).next_to(saddle[0], UP+RIGHT),MathTex('-i', color=BLACK).next_to(saddle[1], DOWN+RIGHT)]
        
        linep = DashedLine(dash_length=0.2,
                start = axes.c2p(config.left_side[0], 2),
                end = axes.c2p(config.right_side[0], 2),
                color = BLACK
            )

        linen = DashedLine(dash_length=0.2,
                start = axes.c2p(config.left_side[0], -2),
                end = axes.c2p(config.right_side[0], -2),
                color = BLACK
            )

        self.add(
            ax_labels,
            *curve1,
            *curve2,
            linep,
            linen,
            *saddle,
            *saddle_label,
            *labels,
            linep_labelText,
            linen_labelText
        )
        """
        zoomed_camera = self.zoomed_camera
        zoomed_display = self.zoomed_display
        frame = zoomed_camera.frame
        zoomed_display_frame = zoomed_display.display_frame
        frame.move_to(axes.c2p(0,1))
        frame.set_color(BLACK)
        zoomed_display_frame.set_color(BLACK)
        zoomed_display.shift(LEFT*2)

        zd_rect = BackgroundRectangle(zoomed_display, fill_opacity=0, buff=MED_SMALL_BUFF)
        self.add_foreground_mobject(zd_rect)
        
        unfold_camera = UpdateFromFunc(zd_rect, lambda rect: rect.replace(zoomed_display))

        connect_line= always_redraw(
            lambda : Line(
                frame.get_right(),
                zoomed_display.get_left(),
                color = BLACK
            )
        )
        self.play(Create(frame))
        self.activate_zooming()
        self.play(self.get_zoomed_display_pop_out_animation(), unfold_camera)
        self.add(connect_line)"""

        """# Scale in        x   y  z
        scale_factor = [2, 2, 0]
        self.play(
            frame.animate.scale(scale_factor),
            zoomed_display.animate.scale(scale_factor),
            FadeOut(zoomed_camera_text),
            FadeOut(frame_text)
        )"""
        self.wait()
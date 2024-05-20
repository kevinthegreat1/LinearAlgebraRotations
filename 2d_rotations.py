from manim import *


class RotateVector(Scene):
    def construct(self):
        # Create a number plane and a vector v_1 = e_1
        number_plane = NumberPlane().scale(3)
        v1 = Vector(number_plane.c2p(1, 0, 0), color=RED)
        e1_label = MathTex(r"\vec{e_1}=", r"\begin{pmatrix}1\\0\end{pmatrix}").next_to(v1, DR)
        self.play(Create(number_plane), Create(v1), Write(e1_label))
        self.wait()

        # Rotate the vector by theta = pi / 6
        v1_theta = always_redraw(lambda: Arc(0.25, angle=v1.get_angle()))
        v1_theta_label = always_redraw(lambda: MathTex(r"\theta").next_to(v1_theta, UP))
        self.add(v1_theta, v1_theta_label)
        self.play(Rotate(v1, np.pi / 6, about_point=ORIGIN, path_arc=np.pi / 6))
        self.wait()

        # Show the components of the rotated vector
        v1_vertical_line = number_plane.get_vertical_line(v1.get_end())
        v1_vertical_line_label = MathTex(r"\sin\theta").next_to(v1_vertical_line, RIGHT)
        v1_horizonal_line = number_plane.get_horizontal_line(v1_vertical_line.get_bottom())
        v1_horizonal_line_label = MathTex(r"\cos\theta").next_to(v1_horizonal_line, DOWN)
        self.play(Create(v1_vertical_line), Write(v1_vertical_line_label), Create(v1_horizonal_line), Write(v1_horizonal_line_label))
        self.wait()

        # Show the action of rotation by theta on e_1
        v1_label = MathTex(r"\begin{pmatrix}1\\0\end{pmatrix}", r"\mapsto", r"\begin{pmatrix}\cos\theta\\\sin\theta\end{pmatrix}").next_to(v1, UR)
        self.play(ReplacementTransform(e1_label[1], v1_label[0]), FadeOut(e1_label[0]), Write(v1_label[1]), Write(v1_label[2][:1]), ReplacementTransform(v1_horizonal_line_label[0], v1_label[2][1:5]), ReplacementTransform(v1_vertical_line_label[0], v1_label[2][5:9]), Write(v1_label[2][9:10]))
        self.wait()

        # Show the action of rotation by theta on e_1 and e_2
        v2_label = MathTex(r"\begin{pmatrix}0\\1\end{pmatrix}", r"\mapsto", r"\begin{pmatrix}-\sin\theta\\\cos\theta\end{pmatrix}").next_to(ORIGIN, DOWN)
        self.play(FadeOut(number_plane), FadeOut(v1), FadeOut(v1_theta), FadeOut(v1_theta_label), FadeOut(v1_vertical_line), FadeOut(v1_horizonal_line), v1_label.animate.next_to(ORIGIN, UP), Write(v2_label))
        self.wait()

        # Show the matrix representation of rotation by theta
        m1 = MathTex(r"\begin{pmatrix}\cos\theta&-\sin\theta\\\sin\theta&\cos\theta\end{pmatrix}")
        self.play(FadeOut(v1_label[:2], v1_label[2][9:], v2_label[:2], v2_label[2][:1]), ReplacementTransform(v1_label[2][:5], m1[0][:5]), ReplacementTransform(v2_label[2][1:6], m1[0][5:10]), ReplacementTransform(v1_label[2][5:9], m1[0][10:14]), ReplacementTransform(v2_label[2][6:], m1[0][14:]))
        self.wait()

from manim import *


class RotateVector(Scene):
    def construct(self):
        # Create a number plane and a vector v_1 = e_1
        number_plane = NumberPlane().scale(3)
        v1 = Vector(number_plane.c2p(1, 0, 0), color=LIGHT_BROWN)
        e1_label = MathTex("\\vec{e_1}=", "\\begin{pmatrix}1\\\\0\\end{pmatrix}").next_to(v1, DR)
        self.play(Create(number_plane), Create(v1), Write(e1_label))
        self.wait()

        # Rotate the vector by theta = pi / 6
        v1_theta = always_redraw(lambda: Arc(0.25, angle=v1.get_angle()))
        v1_theta_label = always_redraw(lambda: MathTex("\\theta").next_to(v1_theta, UP))
        self.add(v1_theta, v1_theta_label)
        self.play(Rotate(v1, np.pi / 6, about_point=ORIGIN, path_arc=np.pi / 6))
        self.wait()

        # Show the components of the rotated vector
        v1_vertical_line = number_plane.get_vertical_line(v1.get_end())
        v1_vertical_line_label = MathTex("\\sin\\theta").next_to(v1_vertical_line, RIGHT)
        v1_horizonal_line = number_plane.get_horizontal_line(v1_vertical_line.get_bottom())
        v1_horizonal_line_label = MathTex("\\cos\\theta").next_to(v1_horizonal_line, DOWN)
        self.play(Create(v1_vertical_line), Write(v1_vertical_line_label), Create(v1_horizonal_line), Write(v1_horizonal_line_label))
        self.wait()

        # Show the action of rotation by theta on e_1
        v1_label = MathTex("\\begin{pmatrix}1\\\\0\\end{pmatrix}", "\\mapsto", "\\begin{pmatrix}\\cos\\theta\\\\\\sin\\theta\\end{pmatrix}").next_to(v1, UR)
        self.play(TransformMatchingTex(Group(v1_horizonal_line_label, v1_vertical_line_label, e1_label), v1_label))
        self.wait()

        # Show the action of rotation by theta on e_1 and e_2
        v2_label = MathTex("\\begin{pmatrix}0\\\\1\\end{pmatrix}", "\\mapsto", "\\begin{pmatrix}-\\sin\\theta\\\\\\cos\\theta\\end{pmatrix}").next_to(ORIGIN, DOWN)
        self.play(FadeOut(number_plane), FadeOut(v1), FadeOut(v1_theta), FadeOut(v1_theta_label), FadeOut(v1_vertical_line), FadeOut(v1_horizonal_line), v1_label.animate.next_to(ORIGIN, UP), Write(v2_label))
        self.wait()

        # Show the matrix representation of rotation by theta
        m1_v1 = MathTex("\\begin{pmatrix}\\cos\\theta\\\\\\sin\\theta\\end{pmatrix}").next_to(ORIGIN, LEFT)
        m1_v2 = MathTex("\\begin{pmatrix}-\\sin\\theta\\\\\\cos\\theta\\end{pmatrix}").next_to(ORIGIN, RIGHT)
        self.play(TransformMatchingTex(v1_label, m1_v1), TransformMatchingTex(v2_label, m1_v2))
        m1 = MathTex("\\begin{pmatrix}\\cos\\theta&-\\sin\\theta\\\\\\sin\\theta&\\cos\\theta\\end{pmatrix}")
        self.play(TransformMatchingTex(Group(m1_v1, m1_v2), m1))
        self.wait()

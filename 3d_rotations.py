from manim import *


class RotateVector(ThreeDScene):
    def construct(self):
        # Create a 3D axes and a vector v_1 = e_1
        three_d_axes = ThreeDAxes().scale(2)
        v1 = Vector(three_d_axes.c2p(1, 0, 0), color=LIGHT_BROWN)
        e1_label = MathTex(r"\vec{e_1}=", r"\begin{pmatrix}1\\0\\0\end{pmatrix}").next_to(v1, DR)
        self.play(Create(three_d_axes), Create(v1), Write(e1_label))
        self.wait()

        # Rotate the camera to show 3D
        self.move_camera(phi=np.pi / 3, theta=-np.pi / 3)

        # Create a vector a_1 = e_3
        a1 = Vector(three_d_axes.c2p(0, 0, 1), color=BLUE)
        e3_label = MathTex(r"\vec{e_3}=", r"\begin{pmatrix}0\\0\\1\end{pmatrix}").next_to(a1, UL).apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        self.play(Create(a1), Write(e3_label))
        self.wait()

        # Rotate the vector by theta = pi / 6
        v1_theta = always_redraw(lambda: Arc(0.25, angle=v1.get_angle()))
        v1_theta_label = always_redraw(lambda: MathTex(r"\theta").next_to(v1_theta, UP).apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix())))
        self.add(v1_theta, v1_theta_label)
        self.play(Rotate(v1, np.pi / 4, about_point=ORIGIN))
        self.wait()

        # Show the components of the rotated vector
        v1_vertical_line = three_d_axes.get_vertical_line(v1.get_end())
        v1_vertical_line_label = MathTex(r"\sin\theta").next_to(v1_vertical_line, RIGHT).apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        v1_horizonal_line = three_d_axes.get_horizontal_line(v1_vertical_line.get_bottom())
        v1_horizonal_line_label = MathTex(r"\cos\theta").next_to(v1_horizonal_line, DOWN).apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        self.play(Create(v1_vertical_line), Write(v1_vertical_line_label), Create(v1_horizonal_line), Write(v1_horizonal_line_label))
        self.wait()

        # Show the action of rotation by theta on e_1
        v1_label = MathTex(r"\begin{pmatrix}1\\0\\0\end{pmatrix}", r"\mapsto", r"\begin{pmatrix}\cos\theta\\\sin\theta\\0\end{pmatrix}").next_to(v1, UR).apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        self.play(ReplacementTransform(e1_label[1], v1_label[0]), FadeOut(e1_label[0]), Write(v1_label[1]), Write(v1_label[2][:2]), ReplacementTransform(v1_horizonal_line_label[0], v1_label[2][2:6]), ReplacementTransform(v1_vertical_line_label[0], v1_label[2][6:10]), Write(v1_label[2][10:]))
        self.wait()

        # Show the action of rotation by theta on e_1, e_2, and e_3
        v2_label = MathTex(r"\begin{pmatrix}0\\1\\0\end{pmatrix}", r"\mapsto", r"\begin{pmatrix}-\sin\theta\\\cos\theta\\0\end{pmatrix}").apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        v3_label = MathTex(r"\begin{pmatrix}0\\0\\1\end{pmatrix}", r"\mapsto", r"\begin{pmatrix}0\\0\\1\end{pmatrix}").next_to(v2_label, DOWN).apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        self.play(FadeOut(three_d_axes, a1, e3_label, v1, v1_theta, v1_theta_label, v1_vertical_line, v1_horizonal_line), v1_label.animate.apply_matrix(self.camera.get_rotation_matrix()).next_to(v2_label, UP).apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix())), Write(v2_label), Write(v3_label))
        self.wait()

        # Show the matrix representation of rotation by theta
        m1 = MathTex(r"\begin{pmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{pmatrix}").apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        self.play(FadeOut(v1_label[:2], v1_label[2][11:], v2_label[:2], v2_label[2][:2], v2_label[2][12:], v3_label[:2], v3_label[2][:2]),
                  ReplacementTransform(v1_label[2][:6], m1[0][:6]), ReplacementTransform(v2_label[2][2:7], m1[0][6:11]), ReplacementTransform(v3_label[2][2], m1[0][11]),
                  ReplacementTransform(v1_label[2][6:10], m1[0][12:16]), ReplacementTransform(v2_label[2][7:11], m1[0][16:20]), ReplacementTransform(v3_label[2][3], m1[0][20]),
                  ReplacementTransform(v1_label[2][10], m1[0][21]), ReplacementTransform(v2_label[2][11], m1[0][22]), ReplacementTransform(v3_label[2][4:], m1[0][23:]))
        self.wait()

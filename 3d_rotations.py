from manim import *


class RotateVectorAboutE3(ThreeDScene):
    def construct(self):
        # Create a 3D axes and a vector v_1 = e_1
        three_d_axes = ThreeDAxes().scale(2)
        v1 = Vector(three_d_axes.c2p(1, 0, 0), color=RED)
        e1_label = MathTex(r"\vec{e_1}=", r"\begin{pmatrix}1\\0\\0\end{pmatrix}").next_to(v1, DR)
        self.play(Create(three_d_axes), Create(v1), Write(e1_label))
        self.wait(2)

        # Rotate the camera to show 3D
        self.move_camera(phi=np.pi / 3, theta=-np.pi / 3)

        # Create a vector a_1 = e_3
        a1 = Vector(three_d_axes.c2p(0, 0, 1), color=BLUE)
        e3_label = MathTex(r"\vec{e_3}=", r"\begin{pmatrix}0\\0\\1\end{pmatrix}").next_to(a1, UL).apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        self.play(Create(a1), Write(e3_label))
        self.wait(5)

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
        self.wait(2)

        # Show the action of rotation by theta on e_1
        v1_label = MathTex(r"\begin{pmatrix}1\\0\\0\end{pmatrix}", r"\mapsto", r"\begin{pmatrix}\cos\theta\\\sin\theta\\0\end{pmatrix}").next_to(v1, RIGHT).apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        self.play(ReplacementTransform(e1_label[1], v1_label[0]), FadeOut(e1_label[0]), Write(v1_label[1]), Write(v1_label[2][:2]), ReplacementTransform(v1_horizonal_line_label[0], v1_label[2][2:6]), ReplacementTransform(v1_vertical_line_label[0], v1_label[2][6:10]), Write(v1_label[2][10:]))
        self.wait(5)

        # Show the action of rotation by theta on e_1, e_2, and e_3
        v2_label = MathTex(r"\begin{pmatrix}0\\1\\0\end{pmatrix}", r"\mapsto", r"\begin{pmatrix}-\sin\theta\\\cos\theta\\0\end{pmatrix}").apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        v3_label = MathTex(r"\begin{pmatrix}0\\0\\1\end{pmatrix}", r"\mapsto", r"\begin{pmatrix}0\\0\\1\end{pmatrix}").next_to(v2_label, DOWN).apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        self.play(FadeOut(three_d_axes, a1, e3_label, v1, v1_theta, v1_theta_label, v1_vertical_line, v1_horizonal_line), v1_label.animate.apply_matrix(self.camera.get_rotation_matrix()).next_to(v2_label, UP).apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix())), Write(v2_label), Write(v3_label))
        self.wait(2)

        # Show the matrix representation of rotation by theta
        r_z = MathTex(r"R_z(\theta)=", r"\begin{pmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{pmatrix}").apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        self.play(FadeOut(v1_label[:2], v1_label[2][11:], v2_label[:2], v2_label[2][:2], v2_label[2][12:], v3_label[:2], v3_label[2][:2]), Write(r_z[0]),
                  ReplacementTransform(v1_label[2][:6], r_z[1][:6]), ReplacementTransform(v2_label[2][2:7], r_z[1][6:11]), ReplacementTransform(v3_label[2][2], r_z[1][11]),
                  ReplacementTransform(v1_label[2][6:10], r_z[1][12:16]), ReplacementTransform(v2_label[2][7:11], r_z[1][16:20]), ReplacementTransform(v3_label[2][3], r_z[1][20]),
                  ReplacementTransform(v1_label[2][10], r_z[1][21]), ReplacementTransform(v2_label[2][11], r_z[1][22]), ReplacementTransform(v3_label[2][4:], r_z[1][23:]))
        self.wait(2)

        # Show the other two elemental rotation matrices
        r_y = MathTex(r"R_y(\theta)=", r"\begin{pmatrix}\cos\theta&0&\sin\theta\\0&1&0\\-\sin\theta&0&\cos\theta\end{pmatrix}").apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        r_x = MathTex(r"R_x(\theta)=", r"\begin{pmatrix}1&0&0\\0&\cos\theta&-\sin\theta\\0&\sin\theta&\cos\theta\end{pmatrix}").next_to(r_y, UP).apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix()))
        self.play(Write(r_x), Write(r_y), r_z.animate.apply_matrix(self.camera.get_rotation_matrix()).next_to(r_y, DOWN).apply_matrix(np.linalg.inv(self.camera.get_rotation_matrix())))
        self.wait(2)


class RotateVectorAboutVector(ThreeDScene):
    def construct(self):
        # Rotate the camera to show 3D
        self.move_camera(phi=np.pi / 3, theta=-np.pi / 3)
        self.begin_3dillusion_camera_rotation()

        # Create a 3D axes and rotation axis vector a_1 = < -1 / 2, -3 / 4, sqrt(3) / 4 >
        three_d_axes = ThreeDAxes(x_length=12, y_length=10, z_length=8).scale(2)
        a1 = Vector(three_d_axes.c2p(-1 / 2, -3 / 4, np.sqrt(3) / 4), color=YELLOW)
        a1_label = MathTex(r"\vec{a_1}=\begin{pmatrix}a_x\\a_y\\a_z\end{pmatrix}=", r"\begin{pmatrix}-\frac{1}{2}\\-\frac{3}{4}\\\frac{\sqrt{3}}{4}\end{pmatrix}").next_to(a1, LEFT)
        self.add_fixed_in_frame_mobjects(a1_label)
        self.play(Create(three_d_axes), Create(a1), Write(a1_label))
        self.wait(5)

        # Create vectors v_1 = e_1, v_2 = e_2, v_3 = e_3
        v1 = Vector(three_d_axes.c2p(1, 0, 0), color=RED)
        e1_label = MathTex(r"\vec{e_1}=", r"\begin{pmatrix}1\\0\\0\end{pmatrix}").next_to(v1, DR)
        v2 = Vector(three_d_axes.c2p(0, 1, 0), color=GREEN)
        e2_label = MathTex(r"\vec{e_2}=", r"\begin{pmatrix}0\\1\\0\end{pmatrix}").next_to(v2, RIGHT)
        v3 = Vector(three_d_axes.c2p(0, 0, 1), color=BLUE)
        e3_label = MathTex(r"\vec{e_3}=", r"\begin{pmatrix}0\\0\\1\end{pmatrix}").next_to(v3, UL)
        self.add_fixed_in_frame_mobjects(e1_label, e2_label, e3_label)
        self.play(Create(v1), Write(e1_label), Create(v2), Write(e2_label), Create(v3), Write(e3_label))
        self.wait(5)

        # Show the y and z components of the rotation axis vector
        a1_z_line = Line(three_d_axes.c2p(-1 / 2, 0, np.sqrt(3) / 4), three_d_axes.c2p(-1 / 2, 0, 0))
        a1_z_line_label = MathTex(r"a_z").next_to(a1_z_line, UR)
        a1_y_line = Line(three_d_axes.c2p(-1 / 2, -3 / 4, np.sqrt(3) / 4), three_d_axes.c2p(-1 / 2, 0, np.sqrt(3) / 4))
        a1_y_line_label = MathTex(r"a_y").next_to(a1_y_line, UL)
        self.play(FadeOut(e1_label, e2_label, e3_label))
        self.add_fixed_in_frame_mobjects(a1_z_line_label, a1_y_line_label)
        self.play(Create(a1_z_line), Write(a1_z_line_label), Create(a1_y_line), Write(a1_y_line_label))
        self.wait(5)

        # Rotate the vectors around the x-axis by theta = -pi / 3 to get the rotation vector onto the xz-plane
        r = MathTex(r"R_x(-\arctan(", r"\frac{a_y}{a_z}", r"))", r"R_y(-\arctan(", r"\frac{a_x}{\sqrt{a_y^2+a_z^2}}", r"))", r"R_z(\theta)", r"R_y(\arctan(", r"\frac{a_x}{\sqrt{a_y^2+a_z^2}}", r"))", r"R_x(\arctan(", r"\frac{a_y}{a_z}", r"))").scale(2 / 3).to_edge(UP)
        self.add_fixed_in_frame_mobjects(r[10:])
        self.play(FadeOut(a1_z_line, a1_y_line), FadeIn(r[10], r[11][2], r[12]), ReplacementTransform(a1_y_line_label[0], r[11][:2]), ReplacementTransform(a1_z_line_label[0], r[11][3:]),
                  Rotate(a1, -np.pi / 3, about_point=ORIGIN, axis=RIGHT), Rotate(v1, -np.pi / 3, about_point=ORIGIN, axis=RIGHT), Rotate(v2, -np.pi / 3, about_point=ORIGIN, axis=RIGHT), Rotate(v3, -np.pi / 3, about_point=ORIGIN, axis=RIGHT))
        self.wait(5)

        # Show the x and z components of the rotation axis vector
        a1_x_line = Line(three_d_axes.c2p(-1 / 2, 0, np.sqrt(3) / 2), three_d_axes.c2p(0, 0, np.sqrt(3) / 2))
        a1_x_line_label = MathTex(r"a_x").next_to(a1_x_line, UP)
        a1_yz_line = Line(three_d_axes.c2p(0, 0, np.sqrt(3) / 2), three_d_axes.c2p(0, 0, 0))
        a1_yz_line_label = MathTex(r"\sqrt{a_y^2+a_z^2}").next_to(a1_yz_line, RIGHT)
        self.add_fixed_in_frame_mobjects(a1_x_line_label, a1_yz_line_label)
        self.play(Create(a1_x_line), Write(a1_x_line_label), Create(a1_yz_line), Write(a1_yz_line_label))
        self.wait(5)

        # Rotate the vectors around the y-axis by theta = pi / 6 to get the rotation vector onto the z-axis
        self.add_fixed_in_frame_mobjects(r[7:])
        self.play(FadeOut(a1_x_line, a1_yz_line), FadeIn(r[7], r[8][2], r[9]), ReplacementTransform(a1_x_line_label[0], r[8][:2]), ReplacementTransform(a1_yz_line_label[0], r[8][3:]),
                  Rotate(a1, np.pi / 6, about_point=ORIGIN, axis=UP), Rotate(v1, np.pi / 6, about_point=ORIGIN, axis=UP), Rotate(v2, np.pi / 6, about_point=ORIGIN, axis=UP), Rotate(v3, np.pi / 6, about_point=ORIGIN, axis=UP))
        self.wait(5)

        # Rotate the vectors around the z-axis by theta = pi / 4 as the desired rotation angle
        self.add_fixed_in_frame_mobjects(r[6])
        self.play(FadeIn(r[6]), Rotate(a1, np.pi / 4, about_point=ORIGIN, axis=OUT), Rotate(v1, np.pi / 4, about_point=ORIGIN, axis=OUT), Rotate(v2, np.pi / 4, about_point=ORIGIN, axis=OUT), Rotate(v3, np.pi / 4, about_point=ORIGIN, axis=OUT))
        self.wait(5)

        # Rotate the vectors around the y-axis by theta = -pi / 6 to get the rotation vector back to the original y angle
        self.add_fixed_in_frame_mobjects(r[3:6])
        self.play(FadeIn(r[3:6]), Rotate(a1, -np.pi / 6, about_point=ORIGIN, axis=UP), Rotate(v1, -np.pi / 6, about_point=ORIGIN, axis=UP), Rotate(v2, -np.pi / 6, about_point=ORIGIN, axis=UP), Rotate(v3, -np.pi / 6, about_point=ORIGIN, axis=UP))
        self.wait(5)

        # Rotate the vectors around the x-axis by theta = pi / 3 to get the rotation vector back to the original x angle
        self.add_fixed_in_frame_mobjects(r[:3])
        self.play(FadeIn(r[:3]), Rotate(a1, np.pi / 3, about_point=ORIGIN, axis=RIGHT), Rotate(v1, np.pi / 3, about_point=ORIGIN, axis=RIGHT), Rotate(v2, np.pi / 3, about_point=ORIGIN, axis=RIGHT), Rotate(v3, np.pi / 3, about_point=ORIGIN, axis=RIGHT))
        self.wait(5)

        self.play(FadeOut(three_d_axes, a1, a1_label, v1, v2, v3))
        self.stop_3dillusion_camera_rotation()
        r_matrices_1_1 = MathTex(r"\begin{pmatrix}1&0&0\\0&\cos(-\arctan(\frac{a_y}{a_z}))&-\sin(-\arctan(\frac{a_y}{a_z}))\\0&\sin(-\arctan(\frac{a_y}{a_z}))&\cos(-\arctan(\frac{a_y}{a_z}))\end{pmatrix}", r"\begin{pmatrix}\cos(-\arctan(\frac{a_x}{\sqrt{a_y^2+a_z^2}}))&0&\sin(-\arctan(\frac{a_x}{\sqrt{a_y^2+a_z^2}}))\\0&1&0\\-\sin(-\arctan(\frac{a_x}{\sqrt{a_y^2+a_z^2}}))&0&\cos(-\arctan(\frac{a_x}{\sqrt{a_y^2+a_z^2}}))\end{pmatrix}", r"\begin{pmatrix}\cos\theta&-\sin\theta&0\\\sin\theta&\cos\theta&0\\0&0&1\end{pmatrix}").scale(1 / 2).next_to(ORIGIN, UP)
        r_matrices_1_2 = MathTex(r"\begin{pmatrix}\cos\arctan(\frac{a_x}{\sqrt{a_y^2+a_z^2}})&0&\sin\arctan(\frac{a_x}{\sqrt{a_y^2+a_z^2}})\\0&1&0\\-\sin\arctan(\frac{a_x}{\sqrt{a_y^2+a_z^2}})&0&\cos\arctan(\frac{a_x}{\sqrt{a_y^2+a_z^2}})\end{pmatrix}", r"\begin{pmatrix}1&0&0\\0&\cos\arctan(\frac{a_y}{a_z})&-\sin\arctan(\frac{a_y}{a_z})\\0&\sin\arctan(\frac{a_y}{a_z})&\cos\arctan(\frac{a_y}{a_z})\end{pmatrix}").scale(1 / 2).next_to(ORIGIN, DOWN)
        self.add_fixed_in_frame_mobjects(r_matrices_1_1, r_matrices_1_2)
        self.play(ReplacementTransform(r[:7], r_matrices_1_1), ReplacementTransform(r[7:], r_matrices_1_2))
        self.wait(5)

        r_matrices_2 = MathTex(r"\begin{pmatrix}\cos\theta+a_x^2(1-\cos\theta) & a_xa_y(1-\cos\theta)-a_z\sin\theta & a_xa_z(1-\cos\theta)+a_y\sin\theta \\ a_ya_x(1-\cos\theta)+a_z\sin\theta & \cos\theta+a_y^2(1-\cos\theta) & a_ya_z(1-\cos\theta)-a_x\sin\theta \\ a_za_x(1-\cos\theta)-a_y\sin\theta & a_za_y(1-\cos\theta)+a_x\sin\theta & \cos\theta+a_z^2(1-\cos\theta)\end{pmatrix}").scale(3 / 4)
        self.remove(r_matrices_1_1, r_matrices_1_2)
        self.add_fixed_in_frame_mobjects(r_matrices_2)
        # self.play(ReplacementTransform(r_matrices_1_1, r_matrices_2), ReplacementTransform(r_matrices_1_2, r_matrices_2))
        self.wait(5)

from manim import *


class RotateVector(Scene):
    def construct(self):
        grid = NumberPlane()
        self.play(Create(grid))

        v1 = Vector([1, 0], color=LIGHT_BROWN)
        m_rotate_90 = [[0, -1], [1, 0]]
        self.play(Create(v1), Create(IntegerMatrix(m_rotate_90, left_bracket="(", right_bracket=")").move_to([2, 2, 0])))
        self.wait()

        self.play(v1.animate.apply_matrix(m_rotate_90), path_arc=np.pi / 2)

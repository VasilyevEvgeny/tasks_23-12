from sympy import symbols, solve, Matrix
from time import time


class LizaTasks:
    def __init__(self):
        pass

    def solve_2nd_order(self):
        a0, a1, a2 = symbols('a0,a1,a2')
        m1 = Matrix([
            [a0, a2], 
            [a2, a0]]
        )
        m2 = Matrix([
            [a0, 0, a2, a1], 
            [a1, a0, 0, a2],
            [a2, 0, a0, a1],
            [a1, a2, 0, a0]]
        )
        
        equations = {'f(t + 2) - 2 f(t + 1) + 5 f(t) = 0': (1, -2, 5)}
        answers = {}

        for key, vals in equations.items():
            print("==========\nEquation: {}".format(key))
            answers.update({key: {'symbolic': None, 'numeric': None}})

            m1_det = m1.det()
            m2_det = m2.det()
            answers[key]['symbolic'] = m1_det * m2_det
            print("Delta_1 (symbolic) = {}".format(m1_det))
            print("Delta_2 (symbolic) = {}".format(m2_det))

            values_to_substitute = [(a0, vals[0]), (a1, vals[1]), (a2, vals[2])]
            m1_det_val = m1_det.subs(values_to_substitute)
            m2_det_val = m2_det.subs(values_to_substitute)
            answers[key]['numeric'] = m1_det_val * m2_det_val
            print("Delta_1 (numeric) = {}".format(m1_det_val))
            print("Delta_2 (numeric) = {}".format(m2_det_val))
    
    def solve_3rd_order(self):
        a0, a1, a2, a3 = symbols('a0,a1,a2,a3')
        m1 = Matrix([
            [a0, a3], 
            [a3, a0]]
        )
        m2 = Matrix([
            [a0,  0,    a3, a2], 
            [a1, a0,    0,  a3],

            [a3,  0,    a0, a1],
            [a2, a3,     0, a0]]
        )
        m3 = Matrix([
            [a0, 0,  0,   a3, a2, a1], 
            [a1, a0, 0,   0,  a3, a2],
            [a2, a1, a0,  0,  0,  a3],

            [a3,  0,  0,  a0, a1, a2],
            [a2, a3,  0,   0, a0, a1],
            [a1, a2, a3,   0,  0, a0]]
        )
        
        equations = {'a0 f(t + 3) + a1 f(t + 2) + a2 f(t + 1) + a3 * f(t) = 0': ('a0', 'a1', 'a2', 'a3')}
        answers = {}

        for key, vals in equations.items():
            print("==========\nEquation: {}".format(key))
            answers.update({key: {'symbolic': None, 'numeric': None}})

            m1_det = m1.det()
            m2_det = m2.det()
            m3_det = m3.det()
            answers[key]['symbolic'] = m1_det * m2_det * m3_det
            print("Delta_1 (symbolic) = {}".format(m1_det))
            print("Delta_2 (symbolic) = {}".format(m2_det))
            print("Delta_3 (symbolic) = {}".format(m3_det))

            values_to_substitute = [(a0, vals[0]), (a1, vals[1]), (a2, vals[2]), (a3, vals[3])]
            m1_det_val = m1_det.subs(values_to_substitute)
            m2_det_val = m2_det.subs(values_to_substitute)
            m3_det_val = m3_det.subs(values_to_substitute)
            answers[key]['numeric'] = m1_det_val * m2_det_val * m3_det_val
            print("Delta_1 (numeric) = {}".format(m1_det_val))
            print("Delta_2 (numeric) = {}".format(m2_det_val))
            print("Delta_3 (numeric) = {}".format(m3_det_val))
    
    def solve_4th_order(self):
        a0, a1, a2, a3, a4 = symbols('a0,a1,a2,a3,a4')
        m1 = Matrix([
            [a0, a4], 
            [a4, a0]]
        )
        m2 = Matrix([
            [a0,  0,    a4, a3], 
            [a1, a0,    0,  a4],

            [a4,  0,    a0, a1],
            [a3, a4,     0, a0]]
        )
        m3 = Matrix([
            [a0, 0,  0,   a4, a3, a2], 
            [a1, a0, 0,   0,  a4, a3],
            [a2, a1, a0,  0,  0,  a4],

            [a4,  0,  0,  a0, a1, a2],
            [a3, a4,  0,   0, a0, a1],
            [a2, a3, a4,   0,  0, a0]]
        )
        m4 = Matrix([
            [a0,  0,  0,  0,    a4, a3, a2, a1], 
            [a1, a0,  0,  0,    0,  a4, a3, a2],
            [a2, a1, a0,  0,    0,  0,  a4, a3],
            [a3, a2, a1, a0,    0,  0,  0,  a4],

            [a4,  0,  0,  0,    a0, a1, a2, a3],
            [a3, a4,  0,  0,     0, a0, a1, a2],
            [a2, a3, a4,  0,     0,  0, a0, a1],
            [a1, a2, a3, a4,     0,  0,  0, a0]]
        )
        
        equations = {
            'f(t + 4) + f(t + 3) + f(t) = 0': (1, 1, 0, 0, 1),
            '7 f(t + 4) - 4 f(t + 3) + 30 f(t + 2) - 4 f(t + 1) + 3 f(t) = 0': (7, -4, 30, -4, 3),
            'f(t + 4) + p f(t + 3) + q f(t) = 0': (1, 'p', 0, 0, 'q')
        }
        answers = {}

        for key, vals in equations.items():
            print("==========\nEquation: {}".format(key))
            answers.update({key: {'symbolic': None, 'numeric': None}})

            m1_det = m1.det()
            m2_det = m2.det()
            m3_det = m3.det()
            m4_det = m4.det()
            answers[key]['symbolic'] = m1_det * m2_det * m3_det * m4_det
            print("Delta_1 (symbolic) = {}".format(m1_det))
            print("Delta_2 (symbolic) = {}".format(m2_det))
            print("Delta_3 (symbolic) = {}".format(m3_det))
            print("Delta_4 (symbolic) = {}".format(m4_det))

            values_to_substitute = [(a0, vals[0]), (a1, vals[1]), (a2, vals[2]), (a3, vals[3]), (a4, vals[4])]
            m1_det_val = m1_det.subs(values_to_substitute)
            m2_det_val = m2_det.subs(values_to_substitute)
            m3_det_val = m3_det.subs(values_to_substitute)
            m4_det_val = m4_det.subs(values_to_substitute)
            answers[key]['numeric'] = m1_det_val * m2_det_val * m3_det_val * m4_det_val
            print("Delta_1 (numeric) = {}".format(m1_det_val))
            print("Delta_2 (numeric) = {}".format(m2_det_val))
            print("Delta_3 (numeric) = {}".format(m3_det_val))
            print("Delta_4 (numeric) = {}".format(m4_det_val))

    def solve_5th_order(self):
        a0, a1, a2, a3, a4, a5 = symbols('a0,a1,a2,a3,a4,a5')
        m1 = Matrix([
            [a0, a5], 
            [a5, a0]]
        )
        m2 = Matrix([
            [a0,  0,    a5, a4], 
            [a1, a0,    0,  a5],

            [a5,  0,    a0, a1],
            [a4, a5,     0, a0]]
        )
        m3 = Matrix([
            [a0, 0,  0,   a5, a4, a3], 
            [a1, a0, 0,   0,  a5, a4],
            [a2, a1, a0,  0,  0,  a5],

            [a5,  0,  0,  a0, a1, a2],
            [a4, a5,  0,   0, a0, a1],
            [a3, a4, a5,   0,  0, a0]]
        )
        m4 = Matrix([
            [a0,  0,  0,  0,    a5, a4, a3, a2], 
            [a1, a0,  0,  0,    0,  a5, a4, a3],
            [a2, a1, a0,  0,    0,  0,  a5, a4],
            [a3, a2, a1, a0,    0,  0,  0,  a5],

            [a5,  0,  0,  0,    a0, a1, a2, a3],
            [a4, a5,  0,  0,     0, a0, a1, a2],
            [a3, a4, a5,  0,     0,  0, a0, a1],
            [a2, a3, a4, a5,     0,  0,  0, a0]]
        )
        m5 = Matrix([
            [a0,  0,  0,  0,  0,    a5, a4, a3, a2, a1], 
            [a1, a0,  0,  0,  0,    0,  a5, a4, a3, a2],
            [a2, a1, a0,  0,  0,    0,  0,  a5, a4, a3],
            [a3, a2, a1, a0,  0,    0,  0,  0,  a5, a4],
            [a4, a3, a2, a1, a0,    0,  0,  0,  0,  a5],

            [a5,  0,  0,  0,  0,   a0, a1, a2, a3, a4],
            [a4, a5,  0,  0,  0,    0, a0, a1, a2, a3],
            [a3, a4, a5,  0,  0,    0,  0, a0, a1, a2],
            [a2, a3, a4, a5,  0,    0,  0,  0, a0, a1],
            [a1, a2, a3, a4, a5,    0,  0,  0,  0, a0]]
        )
        
        equations = {
            'f(t + 5) + p f(t) = 0': (1, 0, 0, 0, 0, 'p')
        }
        answers = {}

        for key, vals in equations.items():
            print("==========\nEquation: {}".format(key))
            answers.update({key: {'symbolic': None, 'numeric': None}})

            m1_det = m1.det()
            m2_det = m2.det()
            m3_det = m3.det()
            m4_det = m4.det()
            m5_det = m5.det()
            answers[key]['symbolic'] = m1_det * m2_det * m3_det * m4_det * m5_det
            print("Delta_1 (symbolic) = {}".format(m1_det))
            print("Delta_2 (symbolic) = {}".format(m2_det))
            print("Delta_3 (symbolic) = {}".format(m3_det))
            print("Delta_4 (symbolic) = {}".format(m4_det))
            print("Delta_5 (symbolic) = {}".format(m5_det))

            values_to_substitute = [(a0, vals[0]), (a1, vals[1]), (a2, vals[2]), (a3, vals[3]), (a4, vals[4]), (a5, vals[5])]
            m1_det_val = m1_det.subs(values_to_substitute)
            m2_det_val = m2_det.subs(values_to_substitute)
            m3_det_val = m3_det.subs(values_to_substitute)
            m4_det_val = m4_det.subs(values_to_substitute)
            m5_det_val = m5_det.subs(values_to_substitute)
            answers[key]['numeric'] = m1_det_val * m2_det_val * m3_det_val * m4_det_val * m5_det_val
            print("Delta_1 (numeric) = {}".format(m1_det_val))
            print("Delta_2 (numeric) = {}".format(m2_det_val))
            print("Delta_3 (numeric) = {}".format(m3_det_val))
            print("Delta_4 (numeric) = {}".format(m4_det_val))
            print("Delta_5 (numeric) = {}".format(m5_det_val))

    def solve_5th_order2(self):
        p = symbols('p')
        m1 = Matrix([
            [1, p], 
            [p, 1]]
        )
        m2 = Matrix([
            [1,  0,    p, 0], 
            [0, 1,    0,  p],

            [p,  0,    1, 0],
            [0, p,     0, 1]]
        )
        m3 = Matrix([
            [1, 0,  0,   p, 0, 0], 
            [0, 1, 0,   0,  p, 0],
            [0, 0, 1,  0,  0,  p],

            [p,  0,  0,  1, 0, 0],
            [0, p,  0,   0, 1, 0],
            [0, 0, p,   0,  0, 1]]
        )
        m4 = Matrix([
            [1,  0,  0,  0,    p, 0, 0, 0], 
            [0, 1,  0,  0,    0,  p, 0, 0],
            [0, 0, 1,  0,    0,  0,  p, 0],
            [0, 0, 0, 1,    0,  0,  0,  p],

            [p,  0,  0,  0,    1, 0, 0, 0],
            [0, p,  0,  0,     0, 1, 0, 0],
            [0, 0, p,  0,     0,  0, 1, 0],
            [0, 0, 0, p,     0,  0,  0, 1]]
        )
        m5 = Matrix([
            [1,  0,  0,  0,  0,    p, 0, 0, 0, 0], 
            [0, 1,  0,  0,  0,    0,  p, 0, 0, 0],
            [0, 0, 1,  0,  0,    0,  0,  p, 0, 0],
            [0, 0, 0, 1,  0,    0,  0,  0,  p, 0],
            [0, 0, 0, 0, 1,    0,  0,  0,  0,  p],

            [p,  0,  0,  0,  0,   1, 0, 0, 0, 0],
            [0, p,  0,  0,  0,    0, 1, 0, 0, 0],
            [0, 0, p,  0,  0,    0,  0, 1, 0, 0],
            [0, 0, 0, p,  0,    0,  0,  0, 1, 0],
            [0, 0, 0, 0, p,    0,  0,  0,  0, 1]]
        )
        
        equations = {
            'f(t + 5) + p f(t) = 0': (1, 0, 0, 0, 0, 'p')
        }
        answers = {}

        for key, vals in equations.items():
            print("==========\nEquation: {}".format(key))
            answers.update({key: {'symbolic': None, 'numeric': None}})

            m1_det = m1.det()
            m2_det = m2.det()
            m3_det = m3.det()
            m4_det = m4.det()
            m5_det = m5.det()
            answers[key]['symbolic'] = m1_det * m2_det * m3_det * m4_det * m5_det
            print("Delta_1 (symbolic) = {}".format(m1_det))
            print("Delta_2 (symbolic) = {}".format(m2_det))
            print("Delta_3 (symbolic) = {}".format(m3_det))
            print("Delta_4 (symbolic) = {}".format(m4_det))
            print("Delta_5 (symbolic) = {}".format(m5_det))


    def task_1(self):
        # self.solve_2nd_order()

        # self.solve_3rd_order()

        # self.solve_4th_order()

        start = time()
        # self.solve_5th_order()
        self.solve_5th_order2()
        end = time()
        print("T = {} s".format(end - start))

      
        # expr = m1.det()
        # print(expr)
        # print(expr.subs([(a0, 1), (a1, 1), (a2, 1), (a3, 1)]))

        y = 'd * x ** 4 + e * x ** 3 + a * x ** 2 + b * x + c'
        # print(solve(y,  'x')) 

if __name__ == "__main__":
    liza_tasks = LizaTasks()
    liza_tasks.task_1()

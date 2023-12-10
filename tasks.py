from sympy import symbols, solve, Matrix, simplify, Abs
from matplotlib import pyplot as plt
from numpy import linspace


class Tasks:
    def __init__(self):
        pass
    
    def make_equation_name(self, coefficients):
        if len(coefficients) == 3:
            return "({}) f(t + 2) + ({}) f(t + 1) + ({}) f(t) = 0" \
                .format(coefficients[0], coefficients[1], coefficients[2])
        elif len(coefficients) == 4:
            return "({}) f(t + 3) + ({}) f(t + 2) + ({}) f(t + 1) + ({}) f(t) = 0" \
                .format(coefficients[0], coefficients[1], coefficients[2], coefficients[3])
        elif len(coefficients) == 5:
            return "({}) f(t + 4) + ({}) f(t + 3) + ({}) f(t + 2) + ({}) f(t + 1) + ({}) f(t) = 0" \
                .format(coefficients[0], coefficients[1], coefficients[2], coefficients[3], coefficients[4])
        elif len(coefficients) == 6:
            return "({}) f(t + 5) + ({}) f(t + 4) + ({}) f(t + 3) + ({}) f(t + 2) + ({}) f(t + 1) + ({}) f(t) = 0" \
                .format(coefficients[0], coefficients[1], coefficients[2], coefficients[3], coefficients[4], coefficients[5])
        else:
            raise Excepton('Wrong number of coefficients!')

    def solve_characteristic_equation(self, eq):
        char_solution = solve(eq, 'L')
        print("Solutions of characteristic equation: {}".format(char_solution))
        abs_solution = char_solution[:]
        for i in range(len(abs_solution)):
            abs_solution[i] = Abs(abs_solution[i]).evalf()
        print("Absolute values of solutions: {}".format(abs_solution))
        product = char_solution[0]
        for i in range(1, len(char_solution)):
            product *= char_solution[i]
        print("Product of all solutions: {}".format(simplify(product)))

    def print_delta(self, number, mode, data):
        print("Delta_{} ({}) = {}".format(number, mode, data))

    def solve_2nd_order(self, **kwargs):
        coefficients = kwargs["coefficients"]
        print("==========\nEquation: {}".format(self.make_equation_name(coefficients)))

        #
        # Shur's determinants
        #
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

        m1_det = m1.det()
        m2_det = m2.det()
        self.print_delta(1, 'symbolic', m1_det)
        self.print_delta(2, 'symbolic', m2_det)

        values_to_substitute = [(a0, coefficients[0]), (a1, coefficients[1]), (a2, coefficients[2])]
        m1_det_val = m1_det.subs(values_to_substitute)
        m2_det_val = m2_det.subs(values_to_substitute)
        self.print_delta(1, 'numeric', m1_det_val)
        self.print_delta(2, 'numeric', m2_det_val)

        #
        # Characteristic equation
        #
        self.solve_characteristic_equation('{} * L ** 2 + {} * L + {}' \
            .format(coefficients[0], coefficients[1], coefficients[2]))

    def solve_3rd_order(self, **kwargs):
        coefficients = kwargs["coefficients"]
        print("==========\nEquation: {}".format(self.make_equation_name(coefficients)))

        #
        # Shur's determinants
        #
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

        m1_det = m1.det()
        m2_det = m2.det()
        m3_det = m3.det()
        self.print_delta(1, 'symbolic', m1_det)
        self.print_delta(2, 'symbolic', m2_det)
        self.print_delta(3, 'symbolic', m3_det)

        values_to_substitute = [(a0, coefficients[0]), (a1, coefficients[1]), (a2, coefficients[2]), (a3, coefficients[3])]
        m1_det_val = m1_det.subs(values_to_substitute)
        m2_det_val = m2_det.subs(values_to_substitute)
        m3_det_val = m3_det.subs(values_to_substitute)
        self.print_delta(1, 'numeric', m1_det_val)
        self.print_delta(2, 'numeric', m2_det_val)
        self.print_delta(3, 'numeric', m3_det_val)

        #
        # Characteristic equation
        #
        self.solve_characteristic_equation('{} * L ** 3 + {} * L ** 2 + {} * L + {}' \
            .format(coefficients[0], coefficients[1], coefficients[2], coefficients[3]))
    
    def solve_4th_order(self, **kwargs):
        coefficients = kwargs["coefficients"]
        print("==========\nEquation: {}".format(self.make_equation_name(coefficients)))

        #
        # Shur's determinants
        #
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
        
        m1_det = m1.det()
        m2_det = m2.det()
        m3_det = m3.det()
        m4_det = m4.det()
        self.print_delta(1, 'symbolic', m1_det)
        self.print_delta(2, 'symbolic', m2_det)
        self.print_delta(3, 'symbolic', m3_det)
        self.print_delta(4, 'symbolic', m4_det)

        values_to_substitute = [(a0, coefficients[0]), (a1, coefficients[1]), (a2, coefficients[2]), (a3, coefficients[3]), (a4, coefficients[4])]
        m1_det_val = m1_det.subs(values_to_substitute)
        m2_det_val = m2_det.subs(values_to_substitute)
        m3_det_val = m3_det.subs(values_to_substitute)
        m4_det_val = m4_det.subs(values_to_substitute)
        self.print_delta(1, 'numeric', m1_det_val)
        self.print_delta(2, 'numeric', m2_det_val)
        self.print_delta(3, 'numeric', m3_det_val)
        self.print_delta(4, 'numeric', m4_det_val)

        #
        # Characteristic equation
        #
        self.solve_characteristic_equation('{} * L ** 4 + {} * L ** 3 + {} * L ** 2 + {} * L + {}' \
            .format(coefficients[0], coefficients[1], coefficients[2], coefficients[3], coefficients[4]))

    def solve_specific_5th_order(self):
        print("==========\nEquation: (1) f(t + 5) + (0) f(t + 4) + (0) f(t + 3) + (0) f(t + 2) + (0) f (t + 1) + p f(t) = 0")

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

        m1_det = m1.det()
        m2_det = m2.det()
        m3_det = m3.det()
        m4_det = m4.det()
        m5_det = m5.det()
        self.print_delta(1, 'symbolic', m1_det)
        self.print_delta(2, 'symbolic', m2_det)
        self.print_delta(3, 'symbolic', m3_det)
        self.print_delta(4, 'symbolic', m4_det)
        self.print_delta(5, 'symbolic', m5_det)

        #
        # Characteristic equation
        #
        self.solve_characteristic_equation('{} * L ** 5 + {} * L ** 4 + {} * L ** 3 + {} * L ** 2 + {} * L + {}' \
            .format(1, 0, 0, 0, 0, 'p'))

    def difference_equation(self):
        print("#########################\nDifference equations\n#########################")

        self.solve_2nd_order(coefficients=(1, -2, 5))
        self.solve_4th_order(coefficients=(1, 1, 0, 0, 1))
        self.solve_4th_order(coefficients=(7, -4, 30, -4, 3))

        self.solve_3rd_order(coefficients=('a0', 'a1', 'a2', 'a3'))
        self.solve_4th_order(coefficients=(1, 'p', 0, 0, 'q'))
        self.solve_specific_5th_order()

    def dynamics(self):
        n_steps = 6

        N0_vals = [1.7]
        a_vals = [2.5]
        
        data = {}
        for a in a_vals:
            for N0 in N0_vals:
                t = [0]
                N = [N0]
                name = "a = {}, $N_0$ = {}".format(a, N0)
                print("==========\n{}".format(name))
                data.update({name: {'t': t, 'N': N}})
                for i in range(1, n_steps):
                    data[name]['t'].append(i)
                    data[name]['N'].append(a * N[-1] - N[-1]**2)

                    print("N({}) = {}".format(i, data[name]['N'][-1]))
        
        plt.figure(figsize=(10, 7))
        for name in data.keys():
            plt.plot(data[name]['t'], data[name]['N'], markersize=10, marker='o', ls='-', lw=1, label=name)
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.xlabel("t", fontsize=20)
        plt.ylabel("N", fontsize=20)
        # plt.ylim(-0.1, 4)
        plt.grid(c='gray', ls=':', lw=0.5, alpha=0.5)
        plt.legend(fontsize=20)
        plt.savefig("N(t).png", bbox_inches="tight", dpi=300)
        plt.close()

        # N0 = 1.7, a = 2.5
        func = []
        xs = linspace(0, 2.5, 1000)
        for x in xs:
            func.append(2.5 * x - x**2)

        plt.figure(figsize=(10, 7))
        plt.plot(xs, xs, ls='-', lw=1, color='black', label='bisector')
        plt.plot(xs, func, ls='-', lw=2, color='black', label='$F(N_t) = 2.5 N_t - N_t^2$')
        plt.axvline(x=1.7, ls=':', lw=1, color='black', label='$N_0=1.7$')
        plt.axvline(1.36, ls=':', lw=1, c='green', label='$N_1=1.36$')
        plt.axvline(1.55, ls=':', lw=1, c='red', label='$N_2=1.55$')
        plt.axvline(1.47, ls=':', lw=1, c='magenta', label='$N_3=1.47$')
        plt.axvline(1.51, ls=':', lw=1, c='olive', label='$N_4=1.51$')
        plt.axvline(1.49, ls=':', lw=1, c='blue', label='$N_5=1.49$')
        plt.xticks(fontsize=15)
        plt.yticks(fontsize=15)
        plt.xlabel("$N_t$", fontsize=20)
        plt.ylabel("$N_{t + 1}$", fontsize=20)
        plt.xlim([-0.1, 2.6])
        plt.grid(c='gray', ls=':', lw=0.5, alpha=0.5)
        plt.arrow(1.7, 0, 0, 1.25, head_width=0.04, head_length=0.1, fc='k', ec='k')
        plt.arrow(1.7, 1.36, -0.24, 0, head_width=0.05, head_length=0.1, fc='k', ec='k')
        plt.arrow(1.36, 1.36, 0, 0.09, head_width=0.04, head_length=0.1, fc='k', ec='k')
        plt.arrow(1.36, 1.55, 0.09, 0.0, head_width=0.05, head_length=0.1, fc='k', ec='k')
        plt.legend(fontsize=20)
        plt.savefig("stairs.png", bbox_inches="tight", dpi=300)
        plt.close()

        func0 = []
        func1 = []
        func2 = []
        xs = linspace(0, 7, 1000)
        for x in xs:
            func0.append(1.1 * x - x**2)
            func1.append(2.5 * x - x**2)
            func2.append(5.0 * x - x**2)
        
        plt.figure(figsize=(10, 7))
        plt.plot(xs, xs, ls='-', lw=1, color='black', label='bisector')
        plt.plot(xs, func0, ls='-', lw=2, color='red', label='$F(N_t) = 1.1 N_t - N_t^2$')
        plt.plot(xs, func1, ls='-', lw=2, color='blue', label='$F(N_t) = 2.5 N_t - N_t^2$')
        plt.plot(xs, func2, ls='-', lw=2, color='green', label='$F(N_t) = 5.0 N_t - N_t^2$')
        plt.xticks(fontsize=12)
        plt.yticks(fontsize=12)
        plt.xlabel("$N_t$", fontsize=15)
        plt.ylabel("$N_{t + 1}$", fontsize=15)
        plt.ylim([-0.1, 7])
        plt.grid(c='gray', ls=':', lw=0.5, alpha=0.5)
        plt.legend(fontsize=12)
        plt.savefig("dynamics.png", bbox_inches="tight", dpi=300)
        plt.close()


if __name__ == "__main__":
    tasks = Tasks()
    tasks.difference_equation()
    tasks.dynamics()

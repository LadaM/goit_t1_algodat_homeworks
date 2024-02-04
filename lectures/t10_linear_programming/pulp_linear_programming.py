import pulp

# Possible LpStatus values:
# Not Solved — задача ще не була розв'язана. Це початковий статус до виклику solve().
# Optimal — задача успішно розв'язана з оптимальним рішенням.
# Infeasible — задача не має розв'язку, тобто не існує жодного набору змінних, який би задовольняв усі обмеження.
# Unbounded — задача має необмежений розв'язок, тобто цільова функція може бути покращена нескінченно.
# Undefined — статус розв'язку не визначено, часто виникає, коли в моделі є помилки.


def production_optimization():
    # initialize the model
    model = pulp.LpProblem("Maximize Profit", pulp.LpMaximize)

    # define the variables
    A = pulp.LpVariable('A', lowBound=0, cat='Integer')  # Кількість продукту А
    B = pulp.LpVariable('B', lowBound=0, upBound=10, cat='Integer')  # Кількість продукту Б

    # objective function (profit)
    model += 50 * A + 40 * B, "Profit"

    # constraints
    model += 5 * A + 2 * B <= 80  # Обмеження для машини №1
    model += 3 * A + 2 * B <= 40  # Обмеження для машини №2

    model.solve()

    print("Виробляти продуктів А:", A.varValue)
    print("Виробляти продуктів Б:", B.varValue)



def main():
    min_model = pulp.LpProblem("Minimization Model", pulp.LpMinimize)
    # or
    max_model = pulp.LpProblem("Maximization Model", pulp.LpMaximize) 

    x = pulp.LpVariable('x', lowBound=0, cat='Continuous')   # cat='Continuous' is set by default
    y = pulp.LpVariable('y', 3, 7)        # 3 ≤ y ≤ 7

    model = min_model
    # Object function
    model += 2 * x + 3 * y, "Problem"
    # Constraints
    model += x + 2 * y <= 8, "Constraint1"
    model += y >= 2, "Constraint2"

    model.solve()
    print(f"Status: {model.status}, {pulp.LpStatus[model.status]}") # to get the status
    print(f"Optimal value: {model.objective.value()}")  # to get the optimal value of the function
    print(f"x = {x.value()}, y = {y.value()}")  # to get the optimal values of the variables


if __name__ == "__main__":
    # main()
    production_optimization()

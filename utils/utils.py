import csv


def read_from_csv(filename):
    """
    Reads data from a csv file.
    expressions -> list of expressions from csv file.
    """
    with open(filename, "r") as csv_file:
        csv_data = csv.reader(csv_file, delimiter="\n")
        expressions = list(csv_data)
    return expressions


def expression_already_in_file(expression, filename):
    """
    Checks if a certain expression is already in a csv file.
    True -> is in file
    """
    expressions = read_from_csv(filename)
    for exp in expressions:
        for i in exp:
            if expression == i:
                return True


def append_to_csv(expression, filename):
    """
    Appends an expression to a csv file.
    True -> wrote to file sucessfully
    """
    with open(filename, "a", newline="") as csv_file:
        csv_data = csv.writer(csv_file)
        if not expression_already_in_file(expression, filename):
            csv_data.writerow([expression])
            return True


def remove_from_csv(expression, filename):
    """
    Removes an expression from a csv file.
    True -> sucessfully removed expression from file.
    """
    expressions = read_from_csv(filename)
    for exp in expressions:
        for i in exp:
            if expression == i:
                expressions.remove(i)

                with open(filename, "w", newline="") as csv_file:
                    csv_data = csv.writer(csv_file)
                    for e in expressions:
                        csv_data.writerow([e])
                        return True

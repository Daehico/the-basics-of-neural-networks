from neuron import Neuron

def main():
    bias = 15
    input_parameters = [1, 2, 1, 1]
    weights = [5, 4, 6, 3]

    n = Neuron(input_parameters, weights)
    s = n.y() - bias
    y = n.onStep(s)

    print("S = ", s)
    print("Y = ", y)


if __name__ == "__main__":
    main()
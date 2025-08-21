import matplotlib.pyplot as plt
import matplotlib.patches as patches

def draw_neuron(ax, center, radius=0.2, label=None):
    circle = plt.Circle(center, radius, fill=False, lw=2)
    ax.add_patch(circle)
    if label:
        ax.text(center[0], center[1], label,
                ha='center', va='center', fontsize=10)

def draw_arrow(ax, start, end):
    ax.annotate("",
                xy=end, xycoords='data',
                xytext=start, textcoords='data',
                arrowprops=dict(arrowstyle="->", lw=1.2))

def draw_perceptron():
    fig, ax = plt.subplots(figsize=(6,4))
    ax.set_xlim(-1, 5)
    ax.set_ylim(-1, 3)
    ax.axis("off")
    ax.set_title("Perceptron (Single Neuron)")

    # Inputs
    inputs = [(0, 2), (0, 1), (0, 0)]
    for i, pos in enumerate(inputs, start=1):
        draw_neuron(ax, pos, label=f"x{i}")

    # Neuron
    draw_neuron(ax, (2, 1), label="Neuron")

    # Output
    draw_neuron(ax, (4, 1), label="y")

    # Connections
    for pos in inputs:
        draw_arrow(ax, (pos[0]+0.2, pos[1]), (1.8, 1))
    draw_arrow(ax, (2.2, 1), (3.8, 1))

    plt.show()

def draw_mlp():
    fig, ax = plt.subplots(figsize=(8,5))
    ax.set_xlim(-1, 9)
    ax.set_ylim(-1, 5)
    ax.axis("off")
    ax.set_title("Multi-Layer Perceptron (MLP)")

    # Input layer
    inputs = [(0, 4), (0, 2), (0, 0)]
    for i, pos in enumerate(inputs, start=1):
        draw_neuron(ax, pos, label=f"x{i}")

    # Hidden layer
    hidden = [(3, 4), (3, 2), (3, 0)]
    for j, pos in enumerate(hidden, start=1):
        draw_neuron(ax, pos, label=f"h{j}")

    # Output layer
    outputs = [(6, 2)]
    draw_neuron(ax, outputs[0], label="y")

    # Connections
    for inp in inputs:
        for hid in hidden:
            draw_arrow(ax, (inp[0]+0.2, inp[1]), (hid[0]-0.2, hid[1]))
    for hid in hidden:
        draw_arrow(ax, (hid[0]+0.2, hid[1]), (outputs[0][0]-0.2, outputs[0][1]))

    plt.show()

# Draw diagrams
draw_perceptron()
draw_mlp()

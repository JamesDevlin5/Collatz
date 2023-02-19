import matplotlib.pyplot as plt
from matplotlib.widgets import TextBox

START_NUM = 21

fig, ax = plt.subplots()
fig.subplots_adjust(bottom=0.2)
ax.set_xlabel("Step Number")
ax.set_ylabel("Function Value")
ax.set_title("Collatz Conjecture")


def is_even(num: int):
    """Checks whether the number argument is even"""
    return num & 1 == 0


def submit(num: str):
    ax.clear()
    counter = 0
    num = int(num)
    while num > 1:
        if is_even(num):
            # Number is Even: Divide by 2
            new_num = num >> 1
            new_color = "red"
        else:
            # Number is Odd: Multiply by 3, Add 1
            new_num = num * 3 + 1
            new_color = "blue"
        # Draw line from current point to new point
        new_counter = counter + 1
        ax.plot([counter, new_counter], [num, new_num], color=new_color)
        ax.annotate(f"{str(new_num)}", xy=(new_counter, new_num + 1), textcoords='data')
        num = new_num
        counter = new_counter
    ax.relim()
    ax.autoscale_view()
    plt.draw()


bottom_axis = fig.add_axes([0.25, 0.05, 0.6, 0.07])
text_box = TextBox(bottom_axis, "Initial Value: ", textalignment="left")
text_box.on_submit(submit)
text_box.set_val(str(START_NUM))

plt.show()

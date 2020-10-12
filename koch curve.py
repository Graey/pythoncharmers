import turtle


def snowflake(lengthSide, levels):
    if levels == 0:
        t.forward(lengthSide)
        return
    lengthSide /= 3.0
    snowflake(lengthSide, levels - 1)
    t.left(60)
    snowflake(lengthSide, levels - 1)
    t.right(120)
    snowflake(lengthSide, levels - 1)
    t.left(60)
    snowflake(lengthSide, levels - 1)


if __name__ == "__main__":
    t = turtle.Pen()
    t.speed(0)
    length = 300.0
    t.penup()
    t.backward(length / 2.0)
    t.pendown()
    for i in range(3):
        snowflake(length, 4)
        t.right(120)

import time
import ctypes

# Matrix multiplication function
def on_mult(m_ar, m_br):
    pha = [[1.0] * m_ar for _ in range(m_ar)]
    phb = [[float(i + 1) for _ in range(m_br)] for i in range(m_br)]
    phc = [[0.0] * m_br for _ in range(m_ar)]

    time1 = time.time()

    for i in range(m_ar):
        for j in range(m_br):
            temp = 0
            for k in range(m_ar):
                temp += pha[i][k] * phb[k][j]
            phc[i][j] = temp

    time2 = time.time()
    print(f"Time: {time2 - time1:.3f} seconds")

    # Display 10 elements of the result matrix to verify correctness
    print("Result matrix:")
    for i in range(1):
        for j in range(min(10, m_br)):
            print(phc[i][j], end=" ")
    print()

# Function for line x line matrix multiplication
def on_mult_line(m_ar, m_br):
    pha = [[1.0] * m_ar for _ in range(m_ar)]
    phb = [[float(i + 1) for _ in range(m_br)] for i in range(m_br)]
    phc = [[0.0] * m_br for _ in range(m_ar)]

    time1 = time.time()

    for i in range(m_ar):
        for k in range(m_br):
            rowCache = phc[i]
            temp1 = pha[i][k]
            temp2 = phb[k]
            for j in range(m_ar):
                rowCache[j] += temp1 * temp2[j]
            phc[i] = rowCache

    time2 = time.time()
    print(f"Time: {time2 - time1:.3f} seconds")

    # Display 10 elements of the result matrix to verify correctness
    print("Result matrix:")
    for i in range(1):
        for j in range(min(10, m_br)):
            print(phc[i][j], end=" ")
    print()

# Main function
def main():
    lin, col, block_size = 0, 0, 0
    op = 1

    while op != 0:
        print("\n1. Multiplication")
        print("2. Line Multiplication")
        op = int(input("Selection?: "))

        if op == 0:
            break

        lin = int(input("Dimensions: lins=cols? "))
        col = lin

        if op == 1:
            on_mult(lin, col)
        elif op == 2:
            on_mult_line(lin, col)


if __name__ == "__main__":
    main()

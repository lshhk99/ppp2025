def f2c(temp_c):
    return (temp_c *9/5) +32

def main():
    temp_c=int(input("썹씨 온도는?"))
    temp_f=f2c(temp_c)
    print(f"{temp_c:.1f}℃ => {temp_f:.1f}℉")

if __name__ == "__main__":
 main()
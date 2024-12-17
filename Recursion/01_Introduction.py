import inspect

def function(count):
    print("Function Call Info:")
    print(f" - Memory Address of count: {id(count)}")
    print(f" - Value of count: {count}")
    # print(f" - Call Stack:\n {inspect.stack()}")

    count += 1
    if count == 10:
        return
    function(count)

def main():
    function(1)

main()

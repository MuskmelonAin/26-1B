def add_info(AList):
    info=input("Enter your info (or type 'exit' to end): ")
    if info.lower()=='exit':
        return False
    AList.append(info)
    return True

def show_info(AList):
    print("Your new to do list:")
    for i, element in enumerate(AList, 1):
        print(f"{i}.{element}")

def main():
    AList_info=[]
    print("Welcome! Enter something for to do list.")

    while True:
        if not add_info(AList_info):
            break

    show_info(AList_info)

if __name__=="__main__":
    main()
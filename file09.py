def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """

# Read data from file
    s=[]
    for i in data:
        if i.isdigit():
            s.append(i)
    return min(s)

data=open('txt_file/data09.txt','r').read()
print(main(data))
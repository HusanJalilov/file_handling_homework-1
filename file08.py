def main(data:str):
    """
    The data is from the file. Find the largest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    a=[]
    s=''.join(data).split()
    for i in s:
        if i.isdigit():
            a.append(int(i))
    return max(a)


# Read data from file

data=open('txt_file/data08.txt','r').read()
print(main(data))
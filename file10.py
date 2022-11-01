def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    s='\n'.join(data).split()
    s.append('Computer Vision')
    a=[]
    for i in s:
        a.append(len(i))
    return max(a)

# Read data from file

data=open('txt_file/data06.txt','r').read()
print(main(data))
def main(data:str):
    """
    The data is from the file. Find the each row length and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s=''.join(data).split()
    
    m=[]
    for i in s:
        m.append(len(i))
    return m


    
# Read data from file

data=open('txt_file/data06.txt','r').read()
print(main(data))
def main(data:str):
    """
    The data is from the file. Find the number of digital and str(non-digital) data and return as list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    s=0
    m=0
    for i in data:
        if not i.isdigit():
            s+=1
        else:
            m+=1
    return [m,s]

    
# Read data from file

data=open('txt_file/data05.txt','r').read()
print(main(data))
from zipfile import ZipFile, ZipInfo

lst = []

with ZipFile("channel.zip") as myzip:
    with myzip.open("90052.txt") as myfile:
        next_file = myfile.readline().split()[-1] + ".txt"
        info = myzip.getinfo(next_file)
        lst.append(info.comment)
        for i in range(911):
            with myzip.open(next_file) as nextfile:
                info = myzip.getinfo(next_file)
                lst.append(info.comment)
                next_file = nextfile.readline().split()[-1] + ".txt"
                print(lst)
                print("".join(lst))
                print(next_file)

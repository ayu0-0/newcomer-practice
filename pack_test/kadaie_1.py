def kadaie_1(input1: str, input2: int) -> None:
    from Bio import SeqIO
    import urllib.request
    import gzip
    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    fastafile = input1
    count = 0
    allrecords = 0

    with gzip.open(fastafile, "rt") as handle:
        for record in SeqIO.parse(handle, 'fasta'):
            allrecords += 1
            # print(record.description)
            length = record.description.split(" ")[2][7:]
            # print(length)
            if int(length) <= input2:
                count += 1

    print(count / allrecords * 100)

# 19.80302002207796

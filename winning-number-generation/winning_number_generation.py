import requests, json, time, csv, hashlib, sys, sets

hash_list = []
setlist = set()
winningnumberv2 = []
winningnumberv3 = []
winningnumberv4 = []
winningnumberv5 = []

while True:

  params = {'token': '74831528a6694379b3bb8588d1e6fe46'}
  request_api = requests.get('https://api.blockcypher.com/v1/btc/main', params=params)
  hash_value = request_api.json()['hash']
  BUF_SIZE = 65536
  sha256 = hashlib.sha256()

  if hash_value not in setlist:             
      hash_list.append(hash_value)
      setlist.add(hash_value)

  with open('entries#x.csv', 'rb') as entriesfile:
    buf = entriesfile.read(BUF_SIZE)
    while len(buf) > 0:
      sha256.update(buf)
      buf = entriesfile.read(BUF_SIZE)

    entryhash = sha256.hexdigest()

##start of hashing hashes

  if len(hash_list) == 1: ##hash number 1 

    print("First number generated waiting for next Bitcoin Block Hash.")
    print("Hash of entries file=", entryhash)
    print("Bitcoin block hash list=", hash_list)

    bothhash = entryhash + hash_list[0]

    hasher = hashlib.sha512()
    hasher.update(bothhash)

    sha512hash = hasher.hexdigest()

    print("SHA512 Hash of both hashes=", sha512hash)

    base10number = int(sha512hash, 16)

    remainder = base10number%15
    remainderplus1 = remainder+1

    print("First winning number=", remainderplus1)

    winningnumber1 = remainderplus1
##next number
  if len(hash_list) == 2: ##hash number 2

    print("Second number generated waiting for next Bitcoin Block Hash.")
    print("Hash of entries file=", entryhash)
    print("Bitcoin block hash list=", hash_list)

    bothhash2 = entryhash + hash_list[1]

    hasher2 = hashlib.sha512()
    hasher2.update(bothhash2)

    sha512hash2 = hasher2.hexdigest()

    print("SHA512 Hash of both hashes=", sha512hash2)

    base10number2 = int(sha512hash2, 16)

    remainder2 = base10number2%15
    remainderplus12 = remainder2+1

    print("Second winning number=", remainderplus12)

    winningnumber2 = remainderplus12

    if winningnumber2 == winningnumber1: ##ensuring no duplicate numbers

      winningnumber2 = []
      hasher2.update(sha512hash2)
      hashv2 = hasher2.hexdigest()

      base10numberv2 = int(hashv2, 16)
      remainderv2 = base10numberv2%15
      remainderplus1v2 = remainderv2+1

      winningnumberv2 = remainderplus1v2
##next number
  if len(hash_list) == 3: ##hash number 3

    print("Third number generated waiting for next Bitcoin Block Hash.")
    print("Hash of entries file=", entryhash)
    print("Bitcoin block hash list=", hash_list)

    bothhash3 = entryhash + hash_list[2]

    hasher3 = hashlib.sha512()
    hasher3.update(bothhash3)

    sha512hash3 = hasher3.hexdigest()

    print("SHA512 Hash of both hashes=", sha512hash3)

    base10number3 = int(sha512hash3, 16)

    remainder3 = base10number3%15
    remainderplus13 = remainder3+1

    print("Third winning number=", remainderplus13)

    winningnumber3 = remainderplus13

    if winningnumber3 == [winningnumber2, winningnumber1]: ##ensuring no duplicate numbers

      winningnumber3 = []
      hasher2.update(sha512hash3)
      hashv3 = hasher2.hexdigest()

      base10numberv3 = int(hashv3, 16)
      remainderv3 = base10numberv3%15
      remainderplus1v3 = remainderv3+1

      winningnumberv3 = remainderplus1v3
##next number
  if len(hash_list) == 4: ##hash number 4

    print("Fourth number generated waiting for next Bitcoin Block Hash.")
    print("Hash of entries file=", entryhash)
    print("Bitcoin block hash list=", hash_list)

    bothhash4 = entryhash + hash_list[3]

    hasher4 = hashlib.sha512()
    hasher4.update(bothhash4)

    sha512hash4 = hasher4.hexdigest()

    print("SHA512 Hash of both hashes=", sha512hash4)

    base10number4 = int(sha512hash4, 16)

    remainder4 = base10number4%15
    remainderplus14 = remainder4+1

    print("Fourth winning number=", remainderplus14)

    winningnumber4 = remainderplus14

    if winningnumber4 == [winningnumber3, winningnumber2, winningnumber1]: ##ensuring no duplicate numbers

      winningnumber4 = []
      hasher4.update(sha512hash4)
      hashv4 = hasher4.hexdigest()

      base10numberv4 = int(hashv4, 16)
      remainderv4 = base10numberv4%15
      remainderplus1v4 = remainderv4+1

      winningnumberv4 = remainderplus1v4
##next number
  if len(hash_list) == 5: ##hash number 5

    print("Fifth number generated waiting for next Bitcoin Block Hash.")
    print("Hash of entries file=", entryhash)
    print("Bitcoin block hash list=", hash_list)

    bothhash5 = entryhash + hash_list[4]

    hasher5 = hashlib.sha512()
    hasher5.update(bothhash5)

    sha512hash5 = hasher5.hexdigest()

    print("SHA512 Hash of both hashes=", sha512hash5)

    base10number5 = int(sha512hash5, 16)

    remainder5 = base10number5%15
    remainderplus15 = remainder5+1

    print("Fifth winning number=", remainderplus15)

    winningnumber5 = remainderplus15

    if winningnumber5 == [winningnumber4, winningnumber3, winningnumber2, winningnumber2]: ##ensuring no duplicate numbers

      winningnumber5 = []
      hasher5.update(sha512hash5)
      hashv5 = hasher5.hexdigest()

      base10numberv5 = int(hashv5, 16)
      remainderv5 = base10numberv5%15
      remainderplus1v5 = remainderv5+1

      winningnumberv5 = remainderplus1v5

    with open('winningnumbers.csv', "w") as output: ##Outputing winning numbers
      writer = csv.writer(output, delimiter=',')
      writer.writerow([str(winningnumber1)])
      if winningnumberv2 == []:
        writer = csv.writer(output, delimiter=',')
        writer.writerow([str(winningnumber2)])
      else:
        writer = csv.writer(output, delimiter=',')
        write.writerow([str(winningnumberv2)])

      if winningnumberv3 == []:
        writer = csv.writer(output, delimiter=',')
        writer.writerow([str(winningnumber3)])
      else:
        writer.writerow([str(winningnumberv3)])

      if winningnumberv4 == []:
        writer = csv.writer(output, delimiter=',')
        writer.writerow([str(winningnumber4)])
      else:
        writer.writerow([str(winningnumberv4)])

      if winningnumberv5 == []:
        writer = csv.writer(output, delimiter=',')
        writer.writerow([str(winningnumber5)])
      else:
        writer.writerow([str(winningnumberv5)])

    with open('winninghashes.csv', "w") as output: ##outputing winning hashes
      writer = csv.writer(output, delimiter=',')
      writer.writerow([hash_list[0]])
      writer.writerow([hash_list[1]])
      writer.writerow([hash_list[2]])
      writer.writerow([hash_list[3]])
      writer.writerow([hash_list[4]])
      
    sys.exit("Winning numbers and hashes generated and saved")

  else:
    time.sleep(10)
##end 
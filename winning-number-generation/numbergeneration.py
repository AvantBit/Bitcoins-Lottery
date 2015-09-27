from __future__ import print_function
import blocktrail, time, csv, hashlib, sys, sets

hash_list = []
setlist = set()

while True: 
	client = blocktrail.APIClient(api_key="37f70c31d64f259ef56ed3216be865a999e12897", api_secret="586748656875a86c396da29834bf30d982ffed29", network="BTC", testnet=False)
	address = client.address('1NcXPMRaanz43b1kokpPuYDdk6GGDvxT2T')
	BUF_SIZE = 65536
	latest_block = client.block_latest()
	h = latest_block['hash']
	sha256 = hashlib.sha256()
	
	if h not in setlist:             
	    hash_list.append(h)
	    setlist.add(h)

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
##space
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
##space
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
##space
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
##space
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

		with open('winningnumbers.csv', "w") as output:
			writer = csv.writer(output, delimiter=',')
			writer.writerow([str(winningnumber1)])
			writer.writerow([str(winningnumber2)])
			writer.writerow([str(winningnumber3)])
			writer.writerow([str(winningnumber4)])
			writer.writerow([str(winningnumber5)])

		with open('winninghashes.csv', "w") as output:
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



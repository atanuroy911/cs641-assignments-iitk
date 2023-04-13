def break_RSA(x_str, max_len_M, N, C, e):
    modN = Zmod(N)
    x_str_binary = ''.join(['{0:08b}'.format(ord(x)) for x in x_str])

    for len_M in range(0, max_len_M + 1, 4):
        P. < M > = modN[]
        poly = ((int(x_str_binary, 2) << len_M) + M) ^ e - C
        poly_deg = poly.degree()
        m = ceil(7 / poly_deg)
        X = ceil(N ** ((1 / poly_deg) - 1 / 7))

        nn = poly_deg * m
        polZ = poly.change_ring(ZZ)
        x = polZ.parent().gen()
        gg = []
        for i in range(m):
            for j in range(poly_deg):
                gg.append((x * X) ** j * N ** (m - i) * polZ(x * X) ** i)
        BB = Matrix(ZZ, nn)
        for i in range(nn):
            for j in range(i + 1):
                BB[i, j] = gg[i][j]
        BB = BB.LLL()
        new_pol = 0
        for i in range(nn):
            new_pol += x ** i * BB[0, i] / X ** i
        potential_roots = new_pol.roots()
        roots = []
        for root in potential_roots:
            if root[0].is_integer():
                result = polZ(ZZ(root[0]))
                if gcd(N, result) >= N:
                    roots.append(ZZ(root[0]))
        if roots:
            root = '{0:b}'.format(roots[0])
            extra = 8 - len(root) % 8
            root = '0' * extra + root
            print("Binary Password: ", root)
            root = ''.join([chr(int(root[i:i + 8], 2)) for i in range(0, len(root), 8)])
            print("Password: '{}'".format(root))
            return
    print("No solution")

e = 5
N =  96182747699505978203493279981459430727937518292984193016886561106363353916386586758651815856242697524548399409635684640624230932849019432043523839656109820905413293723212528269787011277318767034395809409730691799969185752755297017069076766221915260066697903171224961815482777385986349777177392842831115599253
C = 20201765140890787982530130195511967548091360440538993670623792704567712038919530764394425658165724068637112509577956875243834666714708335194598214292722491948910926394322615836713937583472704702361084785003321627398529552902491607466460697544576189592562247393758514331473269321103800540848207736515155096484
# RSA known parameters
ZmodN = Zmod(N);


break_RSA("You see a Gold-Bug in one corner. It is the key to a treasure found by", 300, N, C, e)

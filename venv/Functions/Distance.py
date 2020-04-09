##Distancia euclidea de dos vectores

#import math

def Euclidean_Dist(M):

    M_dist = []

    i = 0
    j = 0
    n = len(M)
    while i < n:

        j = i + 1
        while j < n:

            l = []
            cont = 0
            d = 0
            lenV = len(M[i])
            while cont < lenV:

                v = M[i][cont]-M[j][cont]
                d = d + v**2
                cont += 1

            distancia = d**(0.5)
            M_dist.append([i,j,distancia])
            j += 1

        i += 1
    return M_dist



def Simple_Link(M):

    M_dist = []

    i = 0
    j = 0
    n = len(M)
    dmin = 0
    ind_pos = -1
    
    while i < n:

        if i == 0:
            dmin = M[i][len(M[i])-1]
            ind_pos = i
        else:
            if M[i][len(M[i])-1] < dmin:
                dmin = M[i][len(M[i])-1]
                ind_pos = i

        i += 1
    return ind_pos


def Update_Matrix(l,n_v1,n_v2,M):

    i = 0
    n = len(M)
    DISTA = []
    M_final = []
    n_v1 = str(n_v1)
    n_v2 = str(n_v2)

    while i < n:
        if (str(M[i][0]) == n_v1) and (str(M[i][1]) != n_v2):
            DISTA.append([n_v1,M[i][1],M[i][2]])
        elif (str(M[i][1]) == n_v1) and (str(M[i][0]) != n_v2):
            DISTA.append([n_v1, M[i][0], M[i][2]])
        elif (str(M[i][0]) == n_v2) and (str(M[i][1]) != n_v1):
            DISTA.append([n_v2, M[i][1], M[i][2]])
        elif (str(M[i][1]) == n_v2) and (str(M[i][0]) != n_v1):
            DISTA.append([n_v2, M[i][0], M[i][2]])
        else:
            if str(M[i][0]) != n_v1 and str(M[i][0]) != n_v2 and str(M[i][1]) != n_v1 and str(M[i][1]) != n_v2:
                M_final.append(M[i])
        i += 1

    m = len(DISTA)
    j = 0
    d_final = []

    while j < m:
        k = 0
        while k < j:
            if DISTA[k][1] == DISTA[j][1]:
                if DISTA[k][2] < DISTA[j][2]:
                    d_final.append(['C'+str(l),DISTA[k][1],DISTA[k][2]])
                else:
                    d_final.append(['C'+str(l),DISTA[k][1], DISTA[j][2]])
            k += 1
        j += 1

    for v in d_final:
        M_final.append(v)

    return M_final
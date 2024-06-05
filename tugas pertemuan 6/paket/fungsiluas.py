import math

def balok(p, l, t):
    return 2 * (p * l + p * t + l * t)

def kubus(sisi):
    return 6 * (sisi ** 2)

def limassegiempat(p, l, t):
    luas_alas = p * l
    sisi_miring_panjang = math.sqrt((t * 2) + (l / 2) * 2)
    sisi_miring_lebar = math.sqrt((t * 2) + (p / 2) * 2)
    luas_selubung = (p * sisi_miring_panjang) + (l * sisi_miring_lebar)
    return luas_alas + luas_selubung

def bola(jari_jari):
    return 4 * math.pi * (jari_jari ** 2)
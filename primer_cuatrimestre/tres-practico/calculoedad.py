from datetime import date

def edad(fn, separador): # Agregado parametro separador para adaptarse al formato del practico
    hoy = date.today()
    dn, mn, an = fn.split(separador)
    dn = int(dn)
    mn = int(mn)
    an = int(an)
    dh = hoy.day
    mh = hoy.month
    ah = hoy.year
    e = ah - an
    if (mn > mh) or (mn == mh and dn > dh):
        e -= 1
    return e


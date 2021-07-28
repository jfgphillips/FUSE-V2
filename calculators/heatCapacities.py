

def Schomate_equation(A, B, C, D, E, temp):
    """
    Parameters for each compound can be found at: https://webbook.nist.gov/chemistry/
    ensure temperature of reaction is being considered
    :param A:
    :param B:
    :param C:
    :param D:
    :param E:
    :param temp: reaction temperature in Kelvin
    :return: Heat_capaacity (C_p) in J/[mol*K]
    """

    t = temp/1000
    C_p = A + B * t + C * t**(2) + D * t**(3) + E / (t**(2))
    return(C_p)

if __name__ == '__main__':
    test = Schomate_equation(87.08619, -7.114391 * 10**(-9), 4.866034 * 10**(-9), -1.034098 * 10**(-9), -1.452635 * 10**(-10), 363.15)
    print(test)
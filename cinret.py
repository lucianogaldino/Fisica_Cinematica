def velmed(vm, ds, dt):
    if vm == '?':
        ds = float(ds)
        dt = float(dt)
        vm = ds / dt
        print(f'A velocidade média é de {vm:.2f} m/s')
    elif ds == '?':
        vm = float(vm)
        dt = float(dt)
        ds = vm * dt
        print(f'A variação da posição é de {ds:.2f} m')
    elif dt == '?':
        vm = float(vm)
        ds = float(ds)
        dt = ds / vm
        print(f'O intervalo de tempo é de {dt:.2f} s')
    else:
        print('ERRO na digitação dos dados! Tente novamente.')

def acelmed(am, dv, dt):
    if am == '?':
        dv = float(dv)
        dt = float(dt)
        am = dv / dt
        print(f'A aceleração média é de {am:.2f} m/s2')
    elif dv == '?':
        am = float(am)
        dt = float(dt)
        dv = am * dt
        print(f'A variação da velocidade é de {dv:.2f} m/s')
    elif dt == '?':
        am = float(am)
        dv = float(dv)
        dt = dv / am
        print(f'O intervalo de tempo é de {dt:.2f} s')
    else:
        print('ERRO na digitação dos dados! Tente novamente.')

def mru(s, so, v, t):
    if s == '?':
        so = float(so)
        v = float(v)
        t = float(t)
        s = so + v * t
        print(f'A posição final é de {s:.2f} m')
    elif so == '?':
        s = float(s)
        v = float(v)
        t = float(t)
        so = s - v * t
        print(f'A posição inicial é {so:.2f} m')
    elif v == '?':
        s = float(s)
        so = float(so)
        t = float(t)
        v = (s - so) / t
        print(f'A velocidade é {v:.2f} m/s')
    elif t == '?':
        s = float(s)
        so = float(so)
        v = float(v)
        t = (s - so) / v
        print(f'O intervalo de tempo é {t:.2f} s')
    else:
        print('ERRO na digitação dos dados! Tente novamente.')

def mruv(s, so, d, v, vo, a, t):
    resp = 'S'
    while resp != 'N':
        # Cálculo da posição final
        if d == '?' and s != '?' and so != '?':
            s = float(s)
            so = float(so)
            d = s - so
        if s == '?' and so != '?' and t != '?' and a != '?' and vo != '?':
            so = float(so)
            vo = float(vo)
            t = float(t)
            a = float(a)
            s = so + vo * t + a * t ** 2 / 2
            print(f'A posição final é de {s:.2f} m')
        if s == '?' and t == '?' and v != '?' and vo != '?' and a != '?' and so != '?':
            v = float(v)
            vo = float(vo)
            so = float(so)
            a = float(a)
            s = ((v ** 2 - vo ** 2) / (2 * a)) + so
            print(f'A posição final é de {s:.2f} m')

        # Cálculo da posição inicial
        if so == '?' and t != '?' and s != '?' and vo != '?' and a!= '?':
            s = float(s)
            vo = float(vo)
            t = float(t)
            a = float(a)
            so = s - vo * t - a * t ** 2 / 2
            print(f'A posição inicial é de {so:.2f} m')
        if so == '?' and t == '?' and s != '?' and v != '?' and vo != '?' and a != '?':
            s = float(s)
            v = float(v)
            vo = float(vo)
            a = float(a)
            so = s - ((v ** 2 - vo ** 2) / (2 * a))
            print(f'A posição inicial é de {so:.2f} m')

        # Cálculo do deslocamento
        if d == '?' and t != '?' and vo != '?' and a != '?':
            vo = float(vo)
            t = float(t)
            a = float(a)
            d = vo * t + a * t ** 2 / 2
            print(f'O deslocamento é de {d:.2f} m')
        if d == '?' and t == '?' and v != '?' and vo != '?' and a != '?':
            v = float(v)
            vo = float(vo)
            a = float(a)
            d = (v ** 2 - vo ** 2) / (2 * a)
            print(f'O deslocamento é de {d:.2f} m')

        # Cálculo da Velocidade final
        if v == '?' and t != '?' and vo != '?' and a != '?':
            vo = float(vo)
            a = float(a)
            t = float(t)
            v = vo + a * t
            print(f'A velocidade final é de {v:.2f} m/s')
        if v == '?' and t == '?' and vo != '?' and a!= '?' and d != '?':
            vo = float(vo)
            a = float(a)
            d = float(t)
            if vo ** 2 + 2 * a * d > 0:
                v = (vo ** 2 + 2 * a * d) ** 0.5
            else:
                print('Erro em algum dado informado!')
                v = str('Não pertence aos reais')
            print(f'A velocidade final é de {v:.2f} m/s')

        # Cálculo da Velocidade Inicial
        if vo == '?' and s != '?' and so != '?' and t != '?' and a != '?':
            s = float(s)
            so = float(so)
            t = float(t)
            a = float(a)
            vo = (s - so) / t - a * t / 2
            print(f'A velocidade inicial é de {vo:.2f} m/s')
        if vo == '?' and v != '?' and a != '?' and t != '?':
            v = float(v)
            t = float(t)
            a = float(a)
            vo = v - a * t
            print(f'A velocidade inicial é de {vo:.2f} m/s')
        if vo == '?' and t == '?' and v != '?' and a != '?' and d != '?':
            v = float(v)
            a = float(a)
            d = float(d)
            if v ** 2 - 2 * a * d > 0:
                vo = (v ** 2 - 2 * a * d) ** 0.5
            else:
                print('Erro em algum dado informado!')
                vo = str('Não pertence aos reais')
            print(f'A velocidade inicial é de {vo:.2f} m/s')

        # Cálculo do tempo
        if t == '?' and vo != '?' and a != '?' and s != '?' and so != '?':
            vo = float(vo)
            a = float(a)
            s = float(s)
            so = float(so)
            delta = vo ** 2 + 2 * a * (s - so)
            if delta >= 0:
                t1 = (-vo + (delta) ** 0.5) / a
                t2 = (-vo - (delta) ** 0.5) / a
                if t1 > t2:
                    t = t1
                else:
                    t = t2
            else:
                t = -10  # Foi usado o -10 só para mostrar o erro no final, pois a raiz de delta foi qualquer valor negativo
            if t >= 0:
                print(f'o tempo é {t:.2f} s')
            else:
                print(f'Erro nos valores atribuídos. Digite novamente!')
        if t == '?' and v != '?' and vo != '?' and a != '?':
            vo = float(vo)
            a = float(a)
            v = float(v)
            t = (v - vo) / a
            if t >= 0:
                print(f'o tempo é {t:.2f} s')
            else:
                print(f'Erro nos valores atribuídos. Digite novamente!')

        # Cálculo da aceleração
        if a == '?' and t != '?' and s != '?' and so != '?' and vo != '?':
            s = float(s)
            so = float(so)
            vo = float(vo)
            t = float(t)
            a = (s - so - vo * t) * 2 / t ** 2
            print(f'A aceleração é de {a:.2f} m/s2')
        if a == '?' and t != '?' and v != '?' and vo != '?':
            v = float(v)
            vo = float(vo)
            t = float(t)
            a = (v - vo) / t
            print(f'A aceleração é de {a:.2f} m/s2')
        if a == '?' and t == '?' and v != '?' and vo != '?' and d != '?':
            v = float(v)
            vo = float(vo)
            d = float(d)
            a = (v ** 2 - vo ** 2) / (2 * d)
            print(f'A aceleração é de {a:.2f} m/s2')
        if t == '?' and a == '?' and v == '?' or t == '?' and a == '?' and vo == '?' or t == '?' and a == '?' and d == '?':
            print('Estão faltando valores para os cálculos!')
        resp = (str(input('Tendo essa(s) resposta(s), quer continuar para verificar a possibilidade de outro resultado? (S) ou (N)? ')).strip().upper())

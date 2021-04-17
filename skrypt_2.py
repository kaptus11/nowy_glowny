# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:53:27 2021

@author: HOME
"""
import numpy as np
import matplotlib.pyplot as plt
import random as r

####zadanie2####
#parametry sterujące
c=0
f=0
#geometria
x_0=0
x_p=1

#wezly = np.array([[1, 0],[2, 1],[3, 0.5],[4, 0.75]])

#elementy = np.array([[1, 1, 3],[2, 4, 2],[4, 3, 4]])

twb_L = 'D'
twb_R = 'D'

wwb_L = 0
wwb_R = 1
####zadanie3####
n=100
def generujTabliceGeometrii(x_0, x_p, n):
    temp = (x_p - x_0) / (n - 1)
    matrix = np.array([x_0])

    for i in range(1, n, 1):
        matrix = np.block([matrix, i * temp + x_0])
    return matrix

print(generujTabliceGeometrii(x_0,x_p,4))
print('\n')
####zadanie4####
def inicjacja_parametrow(array):
    
    if(array == 0):
        print('wpisz x_0,x_p,xxb_L,wwb_R,twb_L,twb_R')
        array = input()
    
    zakres = np.array([array[0], array[1]])
    stan = np.array([array[2], array[3]])
    war_brzeg = np.array([array[4], array[5]])
    return zakres, stan, war_brzeg


def generujTabliceGeometrii_v2(zakres):
    print('podaj liczbe wezlow')
    id_wez = int(input())
    val = (zakres[1]-zakres[0])/(id_wez-1)
    wezly = np.array([zakres[0]])
    
    for i in range(1,id_wez):
        wezly = np.block([wezly, i * val + zakres[0]])
    for i in range(1,id_wez-1):
        wezly[i] = wezly[i] + round(r.uniform(-0.05, 0.05),2)
    wezly = np.around(wezly, decimals=2)
    
    sekcje = np.zeros((id_wez-1,2))


    for i in range(0, id_wez-1, 1):
        sekcje[i][0] = i
        sekcje[i][1] = i+1

    return wezly, sekcje


def rysuj_geometrie(zakres, wezly,war_brzeg):
    plt.plot(zakres[0],0,'*')
    plt.plot(zakres[1],0,'*')
    plt.plot(zakres,[0,0])
    plt.plot(wezly,np.zeros(len(wezly)),'*')
    
    plt.text(zakres[0]-0.15,0,war_brzeg[0])
    plt.text(zakres[1]+0.15,0,war_brzeg[1])
    
    for i in range(0,len(wezly)):
        plt.text(wezly[i]-0.03,0.01,str(wezly[i]))
        plt.text(wezly[i]-0.05,-0.05,str(i+1))
    
    for i in range(0,len(wezly)-1):
        print((wezly[i]-wezly[i+1])/2)
        plt.text(wezly[i]/2+wezly[i+1]/2, 0.05,str(i+1))
    
    plt.xlim([zakres[0]-0.3,zakres[1]+0.3])
    plt.ylim([-0.2,0.42])



zakres, stan, war_brzeg = inicjacja_parametrow([0,1,1,4,'D','D'])
print('zakres',zakres)
print('stan', stan)
print('warunek przegowy', war_brzeg)

wezly, sekcje = generujTabliceGeometrii_v2(zakres)
print('wezly', wezly)
print('sekcje', sekcje)

rysuj_geometrie(zakres, wezly, war_brzeg)
    
# =============================================================================
# % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# % % % % % PRE - PROCESSING % % % % %
# %% 1(a) inicjalizacja parametrow sterujacych programem CZESC 1
# [ parametry_sterujace ] = inicjalizacja_parametrow_sterujacych ( ... ) ;
# %% 1(b) definicja parametrow fizycznych i geometrycznych obszaru , warunkow brzegowych CZESC 1
# % - definicja przedzialu ,
# % - liczba wezlow / elementow modelu w przypadku dyskretyzacji jednorodnej
# % - zadanie funkcji wymuszajacej , parametrow rownania rozniczkowego
# % - ...
# [ parametry_geom_i_fiz ] = definicja_parametrow_geom_i_fiz ( ... ) ;
# %% 1(b/c) CZESC 1
# [ WEZLY , ELEMENTY , WAR_BRZEGOWE ] = definicja_zmiennych_przechowujacych_informacje_o_geometrii (
# parametry_geom_i_fiz , ... )
# % - / ew. odczytanie geometrii z pliku
# %% 1(d) prezentacja geometrii zagadnienia CZESC 2
# rysuj_geometrie ( WEZLY , ELEMENTY , WAR_BRZEGOWE ) ;
# % 1(e) utworzenie macierzy wypelnionych zerami CZESC 3
# [A , b] = alokacja_pamieci_na_zmienne_globalne ( liczba_wezlow ) ;
# %% 2(a) CZESC 3
# [ lokalne_fun_ksztaltu , pochodne_lokalnych_fun_ksztaltu ] = definicja_funkcji_ksztaltu ( ... ) ;
# % % % % % PROCESSING % % % % %
# for k = 1: liczba_elementow_skonczonych
# %% 2(b) CZESC 4
# [ nr_glob_elem , nr_glob_wezlow_elem , wspolrzedne_wezlow , jakobian ] =
# zgromadzenie_informacji_dotyczacych_elementu (k , WEZLY , ELEMENTY , ...) ;
# M = obliczenie_lokalnej_macierzy_opisujacej_element ( ) ;
# %% 2(c) CZESC 5
# A = agregacja_macierzy_lokalnej_w_macierzy_globalnej (M , nr_glob_wezlow_elem , ...) ;
# b = obliczanie_elementow_wektora_prawej_strony ( ) ;
# end % for k = 1: liczba_elementow_skonczonych
# %% 2(d) CZESC 6
# [A , b] = uwzglednienie_warunkow_brzegowych ( WAR_BRZEGOWE , ... ) ;
# %% 2(e) CZESC 7
# a = rozwiazanie_url (A ,b )
# % % % % % POST - PROCESSING % % % % %
# %% 3(a) obrobka_wynikow ???? CZESC 8
# %% 3(b) prezentacja graficzna rozwiazania
# rysuj_rozwiazanie ( WEZLY , ELEMENTY , a)
# % %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# 
# =============================================================================

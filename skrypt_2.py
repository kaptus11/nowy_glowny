# -*- coding: utf-8 -*-
"""
Created on Thu Apr 15 14:53:27 2021

@author: HOME
"""
import numpy as np


c=0
f=0

x_0=0
x_p=1



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

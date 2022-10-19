#!/usr/bin/env python

import math


def dissipated_power(voltage, resistance):
	# TODO: Calculer la puissance dissipée par la résistance.
	P = (voltage ** 2) / resistance
	return P


def orthogonal(v1, v2):
	# TODO: Retourner vrai si les vecteurs sont orthogonaux, faux sinon.
	v1[0]  # Pour accéder au X
	v1[1]  # Pour accéder au Y
	nv1 = math.sqrt(v1[0] ** 2 + v1[1] ** 2)
	nv2 = math.sqrt(v2[0] ** 2 + v2[1] ** 2)
	PS = (v1[0] * v2[0] + v1[1] * v2[1]) / (nv1 * nv2)
	if PS == 0:
		return True
	pass


def average(values):
	# TODO: Calculer la moyenne des valeurs positives (on ignore les valeurs strictement négatives).
	somme = 0
	n = 0
	for v in values:
		if v < 0:
			pass  # La variable v contient une valeur de la liste.
		else:
			somme += v
			n += 1
	return somme / n


def bills(value):
	# TODO: Calculez le nombre de billets de 20$, 10$ et 5$ et pièces de 1$ à remettre pour représenter la valeur.
	twenties, tens, fives, twos, ones = 0, 0, 0, 0, 0
	while value != 0:

		if value >= 20:
			twenties+=1
			value-=20
			pass
		elif value >= 10:
			tens+=1
			value-=10
			pass
		elif value >= 5:
			fives+=1
			value-=5
			pass
		elif value >= 2:
			twos+=1
			value-=2
		elif value >= 1:
			ones+=1
			value-=1
			pass

	return (twenties, tens, fives, twos, ones);


def format_base(value, base, digit_letters):
	# Formater un nombre dans une base donné en utilisant les lettres fournies pour les chiffres<
	# `digits_letters[0]` Nous donne la lettre pour le chiffre 0, ainsi de suite.
	result = ""
	abs_value = abs(value)
	while abs_value != 0:
		index=abs_value % base
		result+=digit_letters[index]
		abs_value//=base

	if value < 0:
		# TODO: Ne pas oublier d'ajouter '-' devant pour les nombres négatifs.
		result+='-'
	return result[::-1]


if __name__ == "__main__":
	print(dissipated_power(69, 420))
	print(orthogonal((1, 1), (-1, 1)))
	print(average([1, 4, -2, 10]))
	print(bills(137))
	print(format_base(-42, 16, "0123456789ABCDEF"))

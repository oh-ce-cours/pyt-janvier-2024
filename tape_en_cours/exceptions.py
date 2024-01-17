try:
print("peut lever une exception") raise AssertionError()
except AssertionError as e:
print(" gère l'exception AssertionError")
except (IndexError, ArithmeticError) as e: print(" gère d'autres exceptions")
except Exception as e:
print(" gère le reste des exceptions")
else:
print("suite logique du code qui peut lever une exception") print("mais qui n'en lève pas lui-même")
finally:
print("appelé quel que soit le parcours d'exception")
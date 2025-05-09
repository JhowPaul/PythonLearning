
class ExcecaoCustom(Exception):
    pass
def throws():
    raise ExcecaoCustom
try:
    throws()

except ExcecaoCustom as ex:
    print("Exeção lançada")



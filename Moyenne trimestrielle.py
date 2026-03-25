print("Exercice 1 : moyenne trimestriel")
print("")
note_1 = float(input("Quel est votre 1ère note en PC:"))
note_2 = float(input("Quel est votre 2ème note en PC :"))
note_3 = float(input("Quel est votre 3ère note en pc :"))
if note_1>20 or note_2>20 or note_3>20 :
    print("Votre note ne peut pas dépassé 20 meme si tes intelligent comment comment")
    breakpoint()
if note_1 < 0 or note_2 < 0 or note_3 < 0:
    print("Votre note ne peut pas etre inferieur a 0 meme si tes bete comment comment")
    breakpoint()
moy_pc = (note_1+note_2+note_3)/3
pond_pc=moy_pc*5
print("Votre moyenne en pc est :", moy_pc)
print("Votre pondérer est :",pond_pc)
print("")
note_1 = float(input("Quel est votre 1ère note en math:"))
note_2 = float(input("Quel est votre 2ème note en math :"))
note_3 = float(input("Quel est votre 3ère note en math :"))
if note_1>20 or note_2>20 or note_3>20 :
    print("Votre note ne peut pas dépassé 20 meme si tes intelligent comment comment")
    breakpoint()
if note_1 < 0 or note_2 < 0 or note_3 < 0:
    print("Votre note ne peut pas etre inferieur a 0 meme si tes bete comment comment")
    breakpoint()
moy_math=(note_1+note_2+note_3)/3
pond_math=moy_math*5
print("Votre moyenne en math est :", moy_math)
print("Votre pondérer est :",pond_math)
print("")
note_1 = float(input("Quel est votre 1ère note en français:"))
note_2 = float(input("Quel est votre 2ème note en français :"))
note_3 = float(input("Quel est votre 3ère note en français :"))
if note_1>20 or note_2>20 or note_3>20 :
    print("Votre note ne peut pas dépassé 20 meme si tes intelligent comment comment")
    breakpoint()
if note_1 < 0 or note_2 < 0 or note_3 < 0:
    print("Votre note ne peut pas etre inferieur a 0 meme si tes bete comment comment")
    breakpoint()
moy_fr=(note_1+note_2+note_3)/3
pond_fr=moy_fr*3
print("Votre moyenne en français est :", moy_fr)
print("Votre pondérer est :",pond_fr)
print("")
note_1 = float(input("Quel est votre 1ère note en HG:"))
note_2 = float(input("Quel est votre 2ème note en HG :"))
note_3 = float(input("Quel est votre 3ère note en HG :"))
if note_1>20 or note_2>20 or note_3>20 :
    print("Votre note ne peut pas dépassé 20 meme si tes intelligent comment comment")
    breakpoint()
if note_1 < 0 or note_2 < 0 or note_3 < 0:
    print("Votre note ne peut pas etre inferieur a 0 meme si tes bete comment comment")
    breakpoint()
moy_hg=(note_1+note_2+note_3)/3
pond_hg=moy_hg*3
print("Votre moyenne en hg est :", moy_hg)
print("Votre pondérer est :",pond_hg)
print("")
note_1 = float(input("Quel est votre 1ère note en svt:"))
note_2 = float(input("Quel est votre 2ème note en svt:"))
note_3 = float(input("Quel est votre 3ère note en svt:"))
if note_1>20 or note_2>20 or note_3>20 :
    print("Votre note ne peut pas dépassé 20 meme si tes intelligent comment comment")
    breakpoint()
if note_1 < 0 or note_2 < 0 or note_3 < 0:
    print("Votre note ne peut pas etre inferieur a 0 meme si tes bete comment comment")
    breakpoint()
moy_svt=(note_1+note_2+note_3)/3
pond_svt=moy_svt*5
print("Votre moyenne en svt est :", moy_svt)
print("Votre pondérer est :",pond_svt)
print("")
note_1 = float(input("Quel est votre 1ère note en anglais:"))
note_2 = float(input("Quel est votre 2ème note en anglais :"))
note_3 = float(input("Quel est votre 3ère note en anglais :"))
if note_1>20 or note_2>20 or note_3>20 :
    print("Votre note ne peut pas dépassé 20 meme si tes intelligent comment comment")
    breakpoint()
if note_1 < 0 or note_2 < 0 or note_3 < 0:
    print("Votre note ne peut pas etre inferieur a 0 meme si tes bete comment comment")
    breakpoint()
moy_an=(note_1+note_2+note_3)/3
pond_an=moy_an*2
print("Votre moyenne en anglais est :", moy_an)
print("Votre pondérer est :",pond_an)
print("")
note_1 = float(input("Quel est votre 1ère note en eps:"))
note_2 = float(input("Quel est votre 2ème note en eps :"))
note_3 = float(input("Quel est votre 3ère note en eps :"))
if note_1>20 or note_2>20 or note_3>20 :
    print("Votre note ne peut pas dépassé 20 meme si tes intelligent comment comment")
    breakpoint()
if note_1 < 0 or note_2 < 0 or note_3 < 0:
    print("Votre note ne peut pas etre inferieur a 0 meme si tes bete comment comment")
    breakpoint()
moy_eps=(note_1+note_2+note_3)/3
pond_eps=moy_eps*2
print("Votre moyenne en eps est :", moy_eps)
print("Votre pondérer est :",pond_eps)
print("")
pond_gen=pond_eps+pond_an+pond_fr+pond_hg+pond_pc+pond_svt+pond_math
moy_gen=pond_gen/24
print("Votre pondére total est ",pond_gen,"et votre moyenne général est :",moy_gen)
if moy_gen<10:
    print("votre moyenne est insuffisante")
elif moy_gen>=18 :
    print("votre moyenne est excellente")
elif moy_gen>=16 :
    print("votre moyenne est tres bien ")
elif moy_gen>=12 :
    print("votre moyenne est bien")
elif moy_gen>=10:
    print("votre moyenne est passable")

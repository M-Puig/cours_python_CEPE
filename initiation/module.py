def suppr_element(liste_a_reduire, a_suppr):
    list_new = []
    for elt_list in liste_a_reduire:
        if elt_list != a_suppr:
            list_new.append(elt_list)
    return list_new
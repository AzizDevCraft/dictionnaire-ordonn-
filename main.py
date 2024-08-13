class DictionnaireOrdonne : 
    
    def __init__ (self, individual = {}, **pret) : 
        self._cles = []
        self._valeurs = []
        
        if individual != {} :
            if type (individual) != dict : 
                raise TypeError ("on accepte seulement les dictionnaires ! ")
            
            for key in individual : 
                self [key] = individual [key]
            
        if pret != {} : 
            for key in pret : 
                self [key] = pret [key]
                     

    def __repr__ (self) : 
        if len (self) == 0 : 
            return '{}'
        else : 
            formatage = "{"
            for index in range (len (self)) : 
                 formatage += f"'{self._cles[index]}' : {self._valeurs[index]}, "
            return formatage[:-2] + '}'
    
    def keys (self) : 
        return self._cles
    
    def values (self) : 
        return self._valeurs 
    
    def items (self) : 
        items = [(self._cles[index], self._valeurs[index]) for index in range (len (self))] 
        return items 
     
    def __len__ (self) : 
        return len (self._cles)
    
    def __getitem__ (self, cle) :
        if cle not in self : 
            raise KeyError (f"'{cle}' n'existe pas !")
        else :
            pos = self._cles.index (cle)
            return self._valeurs[pos]
    
    def __setitem__ (self, cle, new) :
        if cle in self : 
            pos = self._cles.index (cle)
            self._valeurs[pos] = new
        else : 
            self._cles.append (cle)
            self._valeurs.append (new)
    
    def __delitem__ (self, cle) : 
        if cle not in self : 
            raise KeyError (f"'{cle}' n'existe pas !")
        else :
            pos = self._cles.index (cle)
            del (self._cles [pos])
            del (self._valeurs [pos])
        
    def __contains__ (self, cle) : 
        return cle in self._cles 
    
    def __add__ (self, nouveau) : 
        if type (nouveau) not in (dict, DictionnaireOrdonne) : 
            raise TypeError ("deux type different on ne peux pas les concatiner !")
        else :
            if type(nouveau) == dict : 
                dic2 = DictionnaireOrdonne (nouveau)
            else : dic2 = nouveau
            
            for index in range (len (dic2)) : 
                self._cles.insert (index, dic2._cles [index])
                self._valeurs.insert (index, dic2._valeurs [index])    
            return self
    
    def reverse (self) : 
        self._cles = self._cles[::-1]
        self._valeurs = self._valeurs[::-1]
        return self
    
    def sort (self) :
        new_items = self.items()
        new_items.sort(key=lambda x : x[0])
        new_key = []
        new_value = []
        for tuplee in new_items : 
            new_key.append (tuplee [0])
            new_value.append (tuplee [1])
        self._cles = new_key
        self._valeurs = new_value
        
    def __iter__ (self) :
        return iter (self._cles) 
    

if "__main__" == __name__ : 
    fruits = DictionnaireOrdonne()
    print (fruits)
    fruits["pomme"] = 52
    fruits["poire"] = 34
    fruits["prune"] = 128
    fruits["melon"] = 15
    print (fruits)
    fruits.sort()
    print(fruits)
    legumes = DictionnaireOrdonne(carotte = 26, haricot = 48)
    print(legumes)
    print (len(legumes))
    legumes.reverse()
    fruits = fruits + legumes
    print (fruits)
    del fruits['haricot']
    print ('haricot' in fruits)
    print (legumes['haricot'])
    for cle in legumes:
        print(cle)
    print (legumes.keys())
    print (legumes.values())
    for nom, qtt in legumes.items():
        print("{0} ({1})".format(nom, qtt))

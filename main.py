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
        pos = self._cles.index (cle)
        del (self._cles [pos])
        del (self._valeurs [pos])
        
    def __contains__ (self, cle) : 
        return cle in self._cles 
    
    def __add__ (self, dic2) : 
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
    dic = DictionnaireOrdonne ({"aziz" : 20, "ouss" : 19, "ahmed" : 17})
    dic ["aziz"] = 21
    dic ["lonys"] = 12
    print (dic)
    dd = DictionnaireOrdonne (adem=2, ysf=3)
    print (dd)
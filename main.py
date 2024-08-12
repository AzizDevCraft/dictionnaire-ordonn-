class DictionnaireOrdonne : 
    
    def __init__ (self, individual = {}, **pret) : 
        self.cles = []
        self.valeurs = []
        
        if individual != {} :
            for key in individual.keys () : 
                self.cles.append (key)
            
            for val in individual.values () : 
                self.valeurs.append (val)
            
        if pret != {} : 
            for key in pret.keys () : 
                self.cles.append (key)
            
            for val in pret.values () : 
                self.valeurs.append (val)       

    def __repr__ (self) : 
        if len (self) == 0 : 
            return '{}'
        else : 
            formatage = "{"
            for index in range (len (self)) : 
                 formatage += f"'{self.cles[index]}' : {self.valeurs[index]}, "
            return formatage[:-2] + '}'
    
    def keys (self) : 
        return self.cles
    
    def values (self) : 
        return self.valeurs 
    
    def items (self) : 
        items = [(self.cles[index], self.valeurs[index]) for index in range (len (self))] 
        return items 
     
    def __len__ (self) : 
        return len (self.cles)
    
    def __getitem__ (self, cle) :
        pos = self.cles.index (cle)
        return self.valeurs[pos]
    
    def __setitem__ (self, cle, new) :
        if cle in self : 
            pos = self.cles.index (cle)
            self.valeurs[pos] = new
        else : 
            self.cles.append (cle)
            self.valeurs.append (new)
    
    def __delitem__ (self, cle) : 
        pos = self.cles.index (cle)
        del (self.cles [pos])
        del (self.valeurs [pos])
        
    def __contains__ (self, cle) : 
        return cle in self.cles 
    
    def __add__ (self, ) : 
        pass
    
    def __radd__ (self, ) : 
        pass
    
    def __del__ (self, ) :
        pass 
    
    def reverse (self, ) : 
        pass
    
    def sort (self, ) :
        pass
    
    def __iter__ (self, ) :
        pass 
    

if "__main__" == __name__ : 
    dic = DictionnaireOrdonne ({"aziz" : 20, "ouss" : 19, "ahmed" : 17})
    print (dic)
    print (dic["aziz"])
    dic ["aziz"] = 21
    dic ["lonys"] = 12
    print (dic)
    del dic ["ouss"]
    print (dic)
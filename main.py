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
    
    def __add__ (self, ) : 
        pass
    
    def __radd__ (self, ) : 
        pass
    
    def __contains__ (self, ) : 
        pass 
    
    def __getitem__ (self, ) :
        pass 
    
    def __setitem__ (self, ) :
        pass 
    
    def __del__ (self, ) :
        pass 
    
    def __delitem__ (self, ) : 
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
    di = DictionnaireOrdonne (azizzz = 20, ouss = 19, ahmed = 18)
    print (len (di))
    print (di.items ())
    d = DictionnaireOrdonne()
    print (d)
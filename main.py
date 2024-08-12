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
        if len (self.cles) == 0 : 
            return '{}'
        else : 
            formatage = "{"
            for index in range (len (self.cles)) : 
                 formatage += f"'{self.cles[index]}' : {self.valeurs[index]}, "
            return formatage[:-2] + '}'
    
    def keys (self) : 
        pass
    
    def values (self) : 
        pass 
    
    def items (self) : 
        pass 
    
    def __len__ (self) : 
        pass
    
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
    print (di)
    d = DictionnaireOrdonne()
    print (d)
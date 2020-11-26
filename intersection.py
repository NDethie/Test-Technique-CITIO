from shapely.geometry import LineString


def intersectionn(la, lb):
    stations = la.intersection(lb) 

    if not la or  not lb: # 1 ou 2 itinéraires vides
        print ("No itinéraire") 
        return True

    else: 
         if la.intersection(lb): # S'il trouve des stations
            print ("Intersection: ", stations )
            return True 

         else : # s'il ne d'intersection 
            print ("No intersections")
            return True

    

#intersectionn(LineString([(3,4), (5,5), (1,2), (8,4), (5,7)]) , LineString([(2,3), (3,5), (5,7), (5,8), (8,9)]) )



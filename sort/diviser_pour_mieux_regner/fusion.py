

def tri_fusion(arr):
    """
    Fonction pour diviser les tableaux 
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = tri_fusion(arr[:mid])
    right = tri_fusion(arr[mid:])
    
    return fusion(left, right)


def fusion(left, right):
    """
    Fonction pour fusionner
    """
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Exemple
arr = [5, 2, 9, 1, 7]
print(tri_fusion(arr))  

from GUI_Functions import SORTING_KEY_PRESSED


def Partition(Vis, l, r, Win, Font):
    pivot = Vis.array[l]
    i = l - 1
    j = r + 1

    
    while True:
        i += 1
        while (Vis.array[i] < pivot):
            i += 1
            SORTING_KEY_PRESSED()
            Vis.Draw(Win, Font)
            
        j -= 1
        while (Vis.array[j] > pivot):
            j -= 1
            SORTING_KEY_PRESSED()
            Vis.Draw(Win, Font)
        
        if (i >= j):
            SORTING_KEY_PRESSED()
            Vis.Draw(Win, Font)
            return j
        
        Vis.array[i], Vis.array[j] = Vis.array[j], Vis.array[i]
        
        Vis.Moving_Elements = [Vis.array[i], Vis.array[j]]
        SORTING_KEY_PRESSED()
        Vis.Draw(Win, Font, newAccess=2)

def QuickSort(Vis, Win, Font):
    def _quick_sort(Vis, l, r):
        if (l < r):
            pi = Partition(Vis, l, r, Win, Font)
            
            _quick_sort(Vis, l, pi)
            _quick_sort(Vis, pi + 1, r)

    _quick_sort(Vis, 0, Vis.size-1)
    if not Vis.is_sorted:
        Vis.Draw_Check_Sorted(Win, Font)

    Vis.is_sorted = True
    Vis.Draw(Win, Font)
from mmu_class import *

def mmu(paginas, frames, archivo):
    pagefaults = 0
    cola_paginas = initq(paginas)
    orden = Cola()
    lista_paginas = []

    for i in range(paginas):
        orden.enq(i)
        lista_paginas.append(page(i))
    
    with open(archivo) as file:
        for line in file:
            operacion = line[0]
            pagina = int(line[1])
            if verificarcarga(lista_paginas, pagina) or operacion == 'F':
                if operacion == 'F':
                    freeframe(lista_paginas, pagina, cola_paginas)
                else:
                    lista_paginas[pagina].modifybit(operacion)
            else:
                pagefaults += 1
                cargarpagina(lista_paginas, pagina, cola_paginas, orden)
                if operacion == 'F':
                    freeframe(lista_paginas, pagina, cola_paginas)
                else:
                    lista_paginas[pagina].modifybit(operacion)
    entrega(lista_paginas, paginas, frames, pagefaults, archivo)

paginas=int(input())
frames=int(input())
archivo=input()
mmu(paginas,frames,archivo)


            
                

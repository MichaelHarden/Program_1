cities = {
    'A': {
        'neighbors': ['B', 'C'],
        'B': {'prob': 0.1, 'distance': 5},
        'C': {'prob': 0.9, 'distance': 6}
    },
    'B' : {
        'neighbors': ['D', 'E'],
        'D': {'prob': 0.2, 'distance': 4},
        'E': {'prob': 0.8, 'distance': 7}
    },
    'C': {
        'neighbors': ['E', 'F'],
        'E': {'prob': 0.3, 'distance': 4},
        'F': {'prob': 0.7, 'distance': 6}    
    },
    'D': {
        'neighbors': ['G', 'H'],
        'G': {'prob': 0.1, 'distance': 4},
        'H': {'prob': 0.9, 'distance': 6},
    },
    'E': {
        'neighbors': ['H', 'I'],
        'H': {'prob': 0.4, 'distance': 6},
        'I': {'prob': 0.6, 'distance': 4}
    }, 
    'F': {
        'neighbors': ['I', 'J'],
        'I': {'prob': 0.2, 'distance': 3},
        'J': {'prob': 0.8, 'distance': 7}
    }, 
    'G': {
        'neighbors': ['K'],
        'K': {'prob': 1.0, 'distance': 4}
    }, 
    'H': {
        'neighbors': ['K', 'L'],
        'K': {'prob': 0.3, 'distance': 4},
        'L': {'prob': 0.7, 'distance': 8}
    }, 
    'I': {
        'neighbors': ['L', 'M'],
        'L': {'prob': 0.5, 'distance': 6},
        'M': {'prob': 0.5, 'distance': 4}
    }, 
    'J':  {
        'neighbors': ['M'],
        'M': {'prob': 1.0, 'distance': 5}
    }, 
    'K': {
        'neighbors': ['N'],
        'N': {'prob': 1.0, 'distance': 4}
    },
    'L': {
        'neighbors': ['N', 'O'],
        'N': {'prob': 0.4, 'distance': 5},
        'O': {'prob': 0.6, 'distance': 6}
    }, 
    'M': {
        'neighbors': ['O'],
        'O': {'prob': 1.0, 'distance': 5}
    }, 
    'N': {
        'neighbors': ['P'],
        'P': {'prob': 1.0, 'distance': 5}
    }, 
    'O': {
        'neighbors': ['P'],
        'P': {'prob': 1.0, 'distance': 5}
    },
    
    'P': {
        'neighbors': [],
    }
} 



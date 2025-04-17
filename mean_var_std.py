import numpy as np

def calculate(mat:list):
    mat_org = mat.copy()
    mat = np.array(mat).reshape(3, 3)
    stats = {
        'mean': [np.mean(mat[:], axis=0).tolist(), np.mean(mat[:], axis=1).tolist(), float(np.mean(mat_org))], 
        'variance': [np.var(mat[:], axis=0).tolist(), np.var(mat[:], axis=1).tolist(), float( np.var(mat_org))],
        'standard_deviation': [np.std(mat[:], axis=0).tolist(), np.std(mat[:], axis=1).tolist(), float( np.std(mat_org))],
        'max': [np.max(mat[:], axis=0).tolist(), np.max(mat[:], axis=1).tolist(), int( np.max(mat_org))],
        'min': [np.min(mat[:], axis=0).tolist(), np.min(mat[:], axis=1).tolist(), int( np.min(mat_org))],
        'sum': [np.sum(mat[:], axis=0).tolist(), np.sum(mat[:], axis=1).tolist(), int( np.sum(mat_org))]
    }
    return mat, stats
       
   
    
if __name__ == "__main__":
    mat = [0,1,2,3,4,5,6,7,8]
    sol_mat = calculate(mat)[0]
    sol_stats = calculate(mat)[1]
    for key, values in sol_stats.items():
        print(f"{key}: {values}", sep='\n')
    # print(sol_mat)

import pandas as pd

s_box = {
    0x0: 0xE, 0x1: 0x4, 0x2: 0xD, 0x3: 0x1,
    0x4: 0x2, 0x5: 0xF, 0x6: 0xB, 0x7: 0x8,
    0x8: 0x3, 0x9: 0xA, 0xA: 0x6, 0xB: 0xC,
    0xC: 0x5, 0xD: 0x9, 0xE: 0x0, 0xF: 0x7
}

def difference_distribution_table(s_box):
    diff_dist_table = [[0 for i in range(16)] for i in range(16)]
    print(diff_dist_table)
    for x_prime in range(16):
        for x in range(16):
            x_star = x ^ x_prime # x_prime is the XOR value we want to analyze
            y = s_box[x]
            y_star = s_box[x_star]
            y_prime = y ^ y_star
            diff_dist_table[x_prime][y_prime] += 1
    
    df = pd.DataFrame(diff_dist_table, index=[f"{i}" for i in range(16)], columns=[f"{i}" for i in range(16)])
    return df


print(difference_distribution_table(s_box))


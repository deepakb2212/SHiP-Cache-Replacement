ipc_SHiP = []
ipc_LRU = []

SHiP_3_bits = [ 2.8320, 3.4849, 1.4876, 3.1726, 3.7107, 0.8133, 3.1474, 3.8322, 3.1274, 3.2746, 3.6178, 2.6331, 3.8924, 1.2907, 2.8117, 3.7286, 3.9771, 3.2336, 1.5586, 1.9794, 3.5452, 3.6789,2.5745, 2.3345, 3.0130, 2.6169, 0.6871]

SHiP_4_bits = [ 2.8314, 3.4850, 1.4897, 3.1725, 3.7107, 0.8131, 3.1532, 3.8323, 3.1390, 3.2753, 3.6185, 2.6332, 3.8929, 1.3013, 2.8117, 3.7334, 3.9771, 3.2336, 1.5590, 1.9780, 3.5559, 3.6812, 2.5974, 2.3347, 3.0120, 2.6191, 0.6816]

SHiP_5_bits = [ 2.8291, 3.4847, 1.4942, 3.1727, 3.7107, 0.8129, 3.1562, 3.8323, 3.1461, 3.2754, 3.6186, 2.6330, 3.8926, 1.3046, 2.8117, 3.7382, 3.9771, 3.2332, 1.5590, 1.9595, 3.5583, 3.6826, 2.6054, 2.3348, 3.0146, 2.6175, 0.6764]

SHiP_6_bits = [ 2.8284, 3.4849, 1.4973, 3.1729, 3.7107, 0.8128,  3.1578,  3.8323, 3.1768, 3.2758,  3.6186, 2.6335, 3.8925, 1.3109, 2.8117, 3.7439, 3.9771, 3.2332, 1.5589, 1.9589, 3.5595, 3.6830, 2.6145, 2.3348, 3.0149, 2.6190, 0.6715]

SHiP_16k= [ 2.8276, 3.4844, 1.4935, 3.1722, 3.7107, 0.8128, 3.1576, 3.8354, 3.1960, 3.2775, 3.6186, 2.6337, 3.8935, 1.3121, 2.8117, 3.7431, 3.9771, 3.2333, 1.5605, 1.9589, 3.5597, 3.6858, 2.5491, 2.3345,3.0151, 2.6192, 0.6704]

SHiP_64k =[ 2.8284, 3.4846, 1.4946, 3.1729, 3.7107, 0.8128, 3.1577, 3.8343,  3.1726, 3.2760, 3.6186, 2.6336, 3.8928, 1.3155, 2.8117, 3.7435, 3.9771, 3.2332, 1.5594, 1.9589, 3.5597, 3.6836, 2.6145, 2.3347, 3.0151, 2.6185, 0.6722]

SHiP_32k = [ 2.8280, 3.4845, 1.4933, 3.1729, 3.7107, 0.8128, 3.1580, 3.8350,  3.2024, 3.2784, 3.6186, 2.6336, 3.8931, 1.3151, 2.8117, 3.7433, 3.9771, 3.2332, 1.5600, 1.9589, 3.5598, 3.6830, 2.6145, 2.3347, 3.0159, 2.6185, 0.6722]

SHiP_128k = [ 2.8287, 3.4845, 1.4962, 3.1729, 3.7107, 0.8128, 3.1584, 3.8336, 3.1828, 3.2759, 3.6186, 2.6335, 3.8927, 1.3102, 2.8117, 3.7439, 3.9771, 3.2332, 1.5590, 1.9589, 3.5597, 3.6831, 2.6145, 2.3345, 3.0146, 2.6200, 0.6709]

SHiP_3_32 = [ 2.8325, 3.4845, 1.4949, 3.1727, 3.7107, 0.8133, 3.1494, 3.8348, 3.1383, 3.2774, 3.6178, 2.6338, 3.8932, 1.2903, 2.8117, 3.7287, 3.9771, 3.2338, 1.5596, 1.9794, 3.5454, 3.6780, 2.5745, 2.3347, 3.0123, 2.6169, 0.6846]

SHiP_4_32= [ 2.8306, 3.4849, 1.4902, 3.1725, 3.7107, 0.8131, 3.1540, 3.8349, 3.1494, 3.2778, 3.6185, 2.6337, 3.8934, 1.3011, 2.8117, 3.7311, 3.9771, 3.2337, 1.5600, 1.9780, 3.5561, 3.6811, 2.5974, 2.3346, 3.0109, 2.6186, 0.6813]

SHiP_5_32= [2.8299, 3.4846, 1.4947, 3.1727, 3.7107, 0.8129, 3.1576, 3.8350, 3.1569, 3.2781, 3.6186, 2.6333, 3.8932, 1.3047, 2.8117, 3.7391, 3.9771, 3.2334, 1.5601, 1.9595, 3.5587, 3.6823, 2.6054, 2.3347, 3.0128, 2.6176, 0.6776]

ipc_lru=[ 2.5802,3.5470, 1.4640, 3.3200,3.7107, 0.8236, 3.3862, 3.5944, 2.2487,3.2847, 3.6531, 2.6273, 3.9170, 1.2580, 2.8117, 3.6472, 3.9759, 3.2380, 1.6051, 1.9139, 3.4528, 3.7198, 2.5053, 2.4891, 3.0973, 1.3701, 0.4637]
speedup_3_bits = [ i/j for i,j in zip(SHiP_3_bits,ipc_lru)]
speedup_4_bits = [ i/j for i,j in zip(SHiP_4_bits,ipc_lru)]
speedup_5_bits = [ i/j for i,j in zip(SHiP_5_bits,ipc_lru)]
speedup_6_bits = [ i/j for i,j in zip(SHiP_6_bits,ipc_lru)]
speedup_16 = [ i/j for i,j in zip(SHiP_16k,ipc_lru)]
speedup_32 = [ i/j for i,j in zip(SHiP_32k,ipc_lru)]
speedup_64 = [ i/j for i,j in zip(SHiP_64k,ipc_lru)]
speedup_128 = [ i/j for i,j in zip(SHiP_128k,ipc_lru)]
speedup_3_32 = [ i/j for i,j in zip(SHiP_3_32,ipc_lru)]
speedup_4_32 = [ i/j for i,j in zip(SHiP_4_32,ipc_lru)]
speedup_5_32 = [ i/j for i,j in zip(SHiP_5_32,ipc_lru)]

g_m_3 = reduce(lambda x, y: x*y, speedup_3_bits)**(1.0/len(speedup_3_bits))
g_m_4 = reduce(lambda x, y: x*y, speedup_4_bits)**(1.0/len(speedup_4_bits))
g_m_5 = reduce(lambda x, y: x*y, speedup_5_bits)**(1.0/len(speedup_5_bits))
g_m_6 = reduce(lambda x, y: x*y, speedup_6_bits)**(1.0/len(speedup_6_bits))
g_m_16 = reduce(lambda x, y: x*y, speedup_16)**(1.0/len(speedup_16))
g_m_32 = reduce(lambda x, y: x*y, speedup_32)**(1.0/len(speedup_32))
g_m_64 = reduce(lambda x, y: x*y, speedup_64)**(1.0/len(speedup_64))
g_m_128 = reduce(lambda x, y: x*y, speedup_128)**(1.0/len(speedup_128))
g_m_3_32 = reduce(lambda x, y: x*y, speedup_3_32)**(1.0/len(speedup_3_32))
g_m_4_32 = reduce(lambda x, y: x*y, speedup_4_32)**(1.0/len(speedup_4_32))
g_m_5_32 = reduce(lambda x, y: x*y, speedup_5_32)**(1.0/len(speedup_5_32))
#print(g_m_3)
#print(g_m_4)
#print(g_m_5)
#print(g_m_6)
#print(g_m_16)
print(g_m_32)
#print(g_m_64)
#print(g_m_128)
print(g_m_3_32)
print(g_m_4_32)
print(g_m_5_32)
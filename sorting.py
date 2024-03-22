# def insertion_sort(arr):
#     for i in range(1, len(arr)):
#         key = arr[i]
#         j = i -1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key 


# numbers = [7573, 6804, 6147, 10141, 4141, 13649, 7091, 10965, 14544,
# 1560, 10984, 4610, 9782, 10999, 10039, 8084, 7753, 11096, 1605, 2469,
# 6812, 4411, 1550, 1066, 2810, 1306, 14919, 6639, 9869, 11483, 752, 14409,
# 7673, 13713, 12944, 1344, 570, 2904, 11432, 7056, 1859, 12252, 12812,
# 9407, 10349, 9787, 7425, 12922, 10678, 4972, 3773, 11166, 14304, 7718,
# 7989, 611, 12911, 5057, 7568, 13573, 11232, 9405, 4756, 5811, 8251, 9066,
# 2189, 9322, 1820, 13035, 11659, 459, 3905, 7818, 8662, 7112, 5427, 10038,
# 506, 9129, 13408, 6563, 143, 2969, 14750, 903, 12325, 4373, 698, 9592,
# 9345, 3853, 11974, 8124, 2000, 11262, 10840, 480, 13560, 6200, 1316, 440,
# 1232, 12449, 9524, 2096, 252, 5428, 6220, 6274, 1321, 9704, 10360, 946,
# 13792, 3101, 10467, 1, 13767, 5246, 13084, 5943, 11612, 4675, 14555,
# 14646, 12272, 965, 14915, 1337, 9327, 13185, 4101, 2043, 11093, 7919, 879,
# 3662, 12912, 10005, 87, 1827, 5660, 9684, 3594, 4078, 5584, 5502, 895,
# 437, 3004, 5442, 10714, 9398, 14579, 960, 2522, 9425, 2075, 12263, 11539,
# 3942, 9362, 11626, 7650, 13616, 2151, 12757, 10430, 2377, 12352, 12187,
# 4870, 2457, 460, 4704, 2937, 6777, 3756, 6629, 11213, 5129, 8920, 1194,
# 13174, 3224, 6732, 11048, 2009, 14714, 8250, 4386, 12392, 2351, 1494,
# 7497, 2727, 1884, 4528, 3655, 10188, 9608, 6705, 9109, 13388, 4843, 1898,
# 3176, 6714, 3434, 8446, 5259, 10822, 7286, 12814, 13028, 5125, 4510, 8506,
# 407, 10352, 9752, 3143, 7605, 13988, 5027, 9437, 3833, 14498, 11976, 3387,
# 4054, 4757, 9358, 8003, 4201, 5175, 12226, 4555, 12455, 2304, 3192, 5229,
# 3228, 6510, 4017, 2441, 14473, 4599, 14501, 4861, 992, 2055, 6877, 11300,
# 14292, 13323, 10617, 2162, 7224, 12686, 11147, 4739, 8424, 10095, 6250,
# 10750, 4488, 14208, 4648, 333, 11837, 3724, 1962, 3737, 14682, 596, 9572,
# 10530, 3039, 13134, 6967, 8675, 11903, 11954, 12939, 4936, 11163, 6983,
# 7226, 1708, 11421, 11288, 353, 13947, 5447, 1387, 1383, 6896, 2161, 13057,
# 7962, 9552, 4065, 10655, 7633, 7063, 967, 4403, 1061, 13149, 11076, 10754,
# 3828, 8702, 11005, 8938, 9429, 5577, 4181, 13583, 5333, 2719, 6193, 9234,
# 4125, 10455, 14359, 7356, 4088, 8413, 4507, 14063, 3403, 13082, 11777,
# 6085, 3323, 3203, 13548, 42, 1519, 8536, 2234, 2453, 11492, 1149, 4617,
# 11678, 2367, 7719, 6936, 7039, 5238, 2669, 800, 2774, 2311, 11935, 11904,
# 13621, 10933, 9306, 2642, 10447, 2947, 4384, 1612, 11330, 12284, 7483,
# 14810, 1758, 8900, 14034, 10568, 3682, 805, 684, 1567, 1165, 2228, 10881,
# 1014, 9908, 10977, 12697, 11381, 4317, 13471, 9318, 13971, 4318, 2593,
# 8799, 11419, 13770, 2387, 12863, 2740, 13565, 7881, 57, 13361, 7960, 482,
# 8304, 6297, 12585, 1041, 10324, 3240, 14972, 308, 5968, 457, 1753, 6612,
# 8583, 13162, 9836, 1664, 10334, 6205, 10500, 10710, 12943, 8107, 12811,
# 4825, 13073, 12104, 2067, 7832, 4969, 2007, 4, 11103, 9826, 12857, 10652,
# 11829, 4608, 10702, 7129, 4842, 3098, 14643, 14127, 14986, 5834, 4146,
# 9984, 10758, 11007, 5939, 9617, 3123, 2269, 3280, 11534, 6128, 10947, 909,
# 14228, 11102, 11968, 8567, 10474, 4620, 14111, 1226, 7941, 5254, 11414,
# 2244, 10734, 8244, 5578, 10648, 12893, 11580, 6908, 432, 420, 5084, 297,
# 9474, 789, 8037, 3715, 6997, 132, 14391, 2546, 3943, 6445, 13444, 7109,
# 5764, 11439, 8013, 13908, 6144, 6101, 2320, 4220, 601, 9241, 14458, 7517,
# 14865, 14250, 2869, 7770, 14525, 8576, 3382, 10160, 14340, 14743, 6670,
# 14235, 6941, 3740, 12648, 10912, 6404, 9461, 332, 5953, 422, 13426, 12531,
# 2575, 857, 14923, 14624, 14104, 9123, 14023, 9802, 8105, 4005, 4496,
# 11649, 494, 2049, 2175, 8754, 8401, 8299, 10344, 2254, 12456, 2080, 973,
# 11641, 13352, 8228, 349, 10796, 9223, 14425, 14831, 2312, 920, 5697,
# 11241, 5542, 3866, 6252, 10981, 2331, 9874, 1482, 12879, 4114, 4981,
# 10231, 3721, 12003, 7434, 4160, 1121, 13945, 10458, 12077, 1834, 808,
# 1665, 4187, 5637, 410, 10483, 619, 5533, 1828, 8247, 12609, 12222, 9167,
# 13147, 10798, 11203, 10835, 14275, 721, 6042, 218, 4110, 2, 9012, 9415,
# 2786, 5247, 3814, 12323, 1582, 11806, 13215, 8456, 5977, 5878, 12533,
# 11672, 5450, 2782, 4567, 6544, 7567, 14783, 9410, 2794, 9411, 2917, 5321,
# 1411, 3898, 3286, 12628, 13916, 7240, 375, 10408, 3071, 2451, 14796,
# 10152, 174, 2157, 2931, 11703, 14586, 13630, 8393, 5076, 9065, 723, 14811,
# 11266, 5044, 8744, 13679, 9254, 8863, 14308, 9395, 1022, 6162, 10035, 690,
# 4255, 8377, 8781, 4949, 2008, 8447, 8758, 3507, 3483, 6656, 5274, 1620,
# 12393, 3000, 14093, 9497, 930, 3413, 3379, 4061, 842, 7464, 13951, 6646,
# 11706, 7932, 10175, 4377, 711, 11604, 8708, 2236, 10264, 11887, 9891,
# 4621, 4245, 8420, 530, 3912, 12550, 3819, 12541, 7034, 5415, 9965, 1242,
# 6047, 12488, 13229, 9670, 5312, 13255, 10159, 12466, 4902, 1439, 11430,
# 13704, 181, 11805, 6719, 5202, 6488, 6393, 13047, 1462, 10391, 1976, 2194,
# 3274, 4376, 4015, 14928, 5882, 1296, 5626, 4320, 7215, 1661, 8747, 12906,
# 14993, 5904, 11646, 5668, 9334, 4849, 12603, 6192, 5352, 7715, 14863,
# 5836, 14466, 7428, 7640, 4751, 10137, 2069, 5046, 9050, 6474, 688, 3233,
# 3923, 4914, 7249, 14373, 8961, 9198, 7235, 12450, 11416, 12148, 10519,
# 4819, 5803, 8849, 13398, 7054, 6071, 9283, 3540, 4489, 8966, 7119, 7217,
# 10064, 9294, 5221, 2042, 6459, 12000, 9711, 12098, 12086, 7909, 13558,
# 12198, 2489, 4546, 1925, 8256, 1179, 250, 12566, 8625, 12997, 247, 223,
# 11494, 7209, 1597, 12680, 2691, 1082, 1347, 6417, 12028, 11931, 993, 9667,
# 11080, 4574, 8560, 2470, 7348, 10125, 1868, 2763, 3581, 11759, 7834, 3666,
# 1215, 8501, 2173, 6569, 5283, 14375, 6893, 3321, 3561, 11975, 10558, 8355,
# 4234, 6686, 1198, 222, 14368, 7334, 2883, 1297, 7635, 7137, 13510, 3596,
# 5855, 3306, 4717, 12233, 13572, 1622, 12738, 7744, 2376, 13633, 2793,
# 13733, 5618, 1390, 5980, 14431, 12902, 858, 5964, 4992, 2684, 13198, 7440,
# 2205, 10177, 13439, 430, 11225, 12203, 9637, 3503, 5873, 14672, 10103,
# 1715, 8705, 8201, 8214, 2335, 1635, 2891, 2843, 10245, 626, 3815, 8163,
# 5619, 2870, 689, 8834, 10979, 9726, 5519, 9612, 91, 1091, 6142, 2223,
# 3616, 8302, 12240, 3684, 6235, 8697, 7970, 14708, 4458, 4067, 14167,
# 14745, 14345, 8917, 6650, 13252, 1736, 9150, 6760, 9413, 9423, 2101, 8165,
# 3183, 4692, 13702, 12801, 12540, 4752, 4996, 8210, 13873, 102, 1045, 9101,
# 3642, 14858, 1889, 14135, 7330, 6009, 2664, 6920, 11040, 2001, 4872,
# 10516, 6070, 11224, 3739, 14625, 9252, 7384, 103, 6460, 8649, 5517, 4694,
# 2681, 5454, 1735, 6045, 6135, 5903, 7000, 9892, 9834, 2291, 2302, 10987,
# 9577, 6929, 7736, 6124, 9258, 13911, 12269, 10518, 7487, 264, 12596,
# 13625, 14759, 9997, 10741, 5126, 2553, 1667, 10691, 3679, 14837, 6788,
# 1563, 3299, 14651, 1128, 8525, 7536, 8090, 11117, 1523, 1641, 7758, 1065,
# 4429, 1105, 13899, 6973, 6669, 900, 7906, 14088, 14213, 7734, 11392, 5355,
# 6596, 14819, 3792, 14405, 2672, 6618, 3703, 7033, 11216, 8952, 12850,
# 2968, 7900, 3560, 6616, 13734, 6863, 11643, 12813, 6706, 1996, 1455,
# 13543, 10185, 6789, 13736, 4051, 4864, 8777, 242, 6857, 12687, 10396,
# 6194, 3861, 6944, 9585, 6379, 2541, 2791, 11728, 12910, 5799, 13302, 2481,
# 6032, 7166, 10065, 9070, 9629, 4066, 11444, 4029, 14969, 10546, 6224,
# 5139, 14080, 6282, 13852, 13930, 12185, 3171, 11764, 3695, 1228, 585,
# 9828, 13791, 7668, 5381, 3181, 9934, 6350, 8652, 12942, 5824, 4553, 3338,
# 13724, 4632, 11651, 14765, 10004, 10011, 9290, 4193, 1394, 1399, 14506,
# 1781, 2622, 970, 5972, 14050, 10656, 13081, 5474, 1470, 2725, 14461, 9379,
# 14363, 5066, 7606, 11568, 14832, 8884, 13980, 14226, 550, 3878, 9034,
# 7958, 5162, 3289, 13992, 6762, 9304, 12653, 9636, 3500, 6357, 2660, 14844,
# 11600, 7144, 5338, 3593, 5848, 7648, 7761, 9006, 3371, 3597, 1954, 4233,
# 6610, 12230, 10982, 4922, 11615, 2429, 7747, 10694, 8512, 11709, 1191,
# 3599, 2225, 11150, 84, 351, 14497, 8527, 3020, 9365, 98, 10706, 9911,
# 4099, 10668, 2983, 10246, 14042, 6842, 14756, 2840, 8566, 1862, 10107,
# 4268, 8489, 2460, 4799, 2371, 6702, 11233, 5739, 964, 3209, 14306, 12546,
# 9250, 13670, 13711, 6409, 9046, 678, 6867, 10760, 1525, 9180, 12301,
# 14110, 1594, 228, 10003, 2916, 1963, 6685, 13487, 10014, 2245, 10449,
# 13146, 12227, 50, 10735, 4547, 14081, 14526, 10388, 2747, 14548, 5147,
# 12489, 12581, 9681, 6140, 14099, 1501, 10937, 1790, 2045, 7044, 10830,
# 7584, 4236, 7791, 5987, 3383, 9317, 10028, 9599, 1518, 10046, 1874, 9313,
# 9804, 13265, 13144, 3291, 8867, 10642, 10550, 14981, 827, 11691, 11391,
# 13093, 5114, 12396, 5476, 1922, 5724, 6077, 6343, 13231, 4863, 4695, 93,
# 8127, 12500, 11753, 1213, 4947, 1526, 415, 11489, 9426, 3896, 7830, 7083,
# 11182, 4633, 6176, 8432, 3564, 6133, 11780, 9016, 6006, 13517, 11622,
# 1109, 13898, 285, 2700, 4509, 10756, 7259, 4845, 5513, 2386, 3941, 1398,
# 2837, 5529, 12934, 9300, 6743, 4480, 6382, 6507, 8001, 7093, 13072, 6586,
# 6948, 12118, 1308, 1381, 14943, 14124, 4667, 11572, 4954, 4571, 12374,
# 11603, 12843, 1413, 13820, 12777, 1703, 6021, 1803, 9248, 2062, 7103,
# 8789, 3281, 13281, 9600, 7429, 4330, 12482, 9531, 6959, 1953, 1209, 14233,
# 1309, 12730, 9595, 1909, 12186, 5141, 8268, 1168, 6949, 12854, 14434,
# 8978, 1591, 3735, 11664, 13843, 5106, 738, 5109, 14206, 9278, 8634, 9943,
# 5798, 11955, 13701, 3421, 11123, 4359, 1072, 6496, 5692, 9589, 575, 8851,
# 3366, 1628, 11417, 8724, 4502, 14082, 12762, 2114, 8641, 13637, 13520,
# 12905, 2665, 189, 10234, 2336, 7526, 4763, 13768, 6831, 2402, 9823, 12367,
# 2933, 107, 3377, 6158, 5462, 6385, 13065, 29, 3640, 10787, 2078, 11323,
# 655, 13518, 3029, 12629, 10146, 14825, 2578, 3748, 11283, 12692, 12040,
# 10565, 12179, 9244, 13698, 14013, 65, 9222, 5051, 13413, 1610, 5190, 9163,
# 7013, 5767, 6778, 4772, 5853, 9783, 6241, 8908, 3628, 13585, 127, 14707,
# 10350, 7155, 6300, 270, 10033, 3883, 8329, 345, 5235, 5568, 5294, 1324,
# 8999, 6754, 10959, 11457, 10749, 6580, 6037, 3179, 13209, 3552, 9694,
# 11978, 12834, 423, 1763, 10531, 4530, 5702, 4801, 4780, 4683, 301, 5563,
# 10420, 1203, 852, 6984, 4090, 882, 7762, 3793, 3245, 14281, 1510, 7559,
# 4587, 12122, 6746, 11526, 12139, 14222, 9777, 5392, 13935, 14742, 4364,
# 2797, 13365, 14153, 4886, 3634, 12593, 637, 6418, 12919, 14134, 1081,
# 7947, 9551, 14869, 8942, 12480, 9570, 361, 13044, 6181, 2675, 14753, 9164,
# 11229, 1849, 7108, 13597, 9713, 6190, 14214, 1778, 11814, 4077, 12437,
# 11011, 14523, 1836, 10636, 7847, 2877, 3921, 14873, 8931, 12769, 9646,
# 14549, 2238, 741, 5122, 192, 933, 7546, 12543, 1067, 2822, 2149, 6555,
# 10993, 501, 7931, 178, 8590, 4658, 7355, 7846, 10078, 7814, 12999, 14829,
# 9534, 1950, 4286, 14674, 735, 3433, 3568, 5966, 744, 7835, 11046, 11670,
# 8176, 9517, 7344, 7008, 3120, 296, 6368, 13533, 6680, 786, 8748, 12883,
# 3823, 4660, 767, 7246, 4868, 14301, 9116, 2206, 14059, 14722, 2047, 8745,
# 8643, 13706, 467, 747, 4519, 873, 5695, 5118, 12032, 11524, 12702, 10888,
# 435, 12385, 4557, 366, 7092, 465, 12896, 8593, 7586, 5310, 298, 10903,
# 9332, 1553, 146, 5788, 3880, 11827, 4084, 12399, 3718, 1927, 3273, 5419,
# 2679, 8211, 3089, 6735, 1358, 12357, 9966, 409, 4841, 13131, 8236, 8295,
# 3750, 7303, 12337, 2216, 12509, 3463, 7077, 13243, 11741, 2754, 11598,
# 12927, 11237, 10203, 6570, 10693, 9281, 4355, 8275, 886, 5950, 4738, 7011,
# 9452, 10614, 11094, 2122, 13676, 4592, 7651, 13955, 11731, 2174, 4521,
# 5508, 6178, 12406, 628, 14393, 4915, 72, 9779, 12607, 1802, 8794, 14290,
# 9210, 11790, 6011, 13017, 1354, 7442, 8464, 1166, 1544, 1709, 8828, 7916,
# 497, 5737, 13620, 1250, 9145, 14878, 11862, 2760, 11234, 10871, 11769,
# 11486, 4344, 7558, 5880, 8526, 3948, 13189, 13225, 12460, 9889, 12015,
# 10777, 12634, 7842, 13622, 1733, 2550, 11020, 2318, 9346, 6383, 8109,
# 14901, 13513, 2838, 2663, 7418, 3725, 11306, 14089, 4963, 1844, 5214,
# 1193, 8690, 3420, 8065, 9970, 1653, 2462, 12320, 7264, 5382, 7041, 10869,
# 12679, 112, 9565, 11559, 2784, 12795, 9259, 13960, 13872, 6880, 11677,
# 12682, 7575, 1985, 2629, 11950, 9364, 5296, 6149, 10069, 6072, 9001,
# 12095, 8217, 4939, 9962, 5667, 612, 2605, 6487, 1461, 11278, 1013, 3102,
# 10027, 8141, 6590, 2058, 4442, 8385, 14327, 14574, 5449, 8674, 3913,
# 10407, 12937, 377, 3764, 14307, 12162, 4777, 12125, 1571, 9386, 11127,
# 8402, 2535, 2894, 11771, 10670, 9656, 10220, 13092, 9851, 6374, 10867,
# 8014, 12209, 10454, 13758, 6285, 3155, 14360, 2131, 8907, 7048, 8861,
# 10377, 7079, 5569, 2503, 9186, 8709, 8234, 2314, 13722, 9751, 1147, 7354,
# 9991, 9029, 8164, 8241, 7951, 8137, 2030, 4746, 2898, 3856, 14258, 360,
# 5480, 12360, 8430, 778, 13799, 11379, 12867, 4224, 8843, 14996, 4291,
# 8694, 3462, 13609, 1466, 7187, 1328, 12356, 3551, 2029, 2668, 3097, 7190,
# 6338, 10310, 13888, 11495, 14215, 6187, 6249, 13842, 11226, 6846, 13812,
# 2235, 1112, 2808, 6676, 8502, 9596, 3345, 6216, 3021, 10348, 9634, 1299,
# 8511, 2530, 9131, 8551, 10820, 2680, 277, 10916, 4888, 13821, 5800, 2010,
# 5722, 10611, 8954, 4783, 10950, 14130, 10058, 3251, 6575, 6552, 3543, 131,
# 7702, 12041, 11844, 7445, 13411, 6233, 4630, 2728, 9876, 8797, 6399, 2355,
# 14910, 4898, 27, 1942, 763, 5825, 9383, 10059, 8969, 6843, 3340, 3497,
# 1700, 7267, 9824, 10905, 1972, 1301, 10575, 11024, 8216, 10971, 11588,
# 9288, 7268, 11388, 6979, 8364, 14225, 7981, 14836, 275, 4226, 13489, 9506,
# 11951, 12787, 53, 11910, 13150, 1001, 8360, 13910, 1231, 5599, 4297, 8944,
# 7849, 1679, 8816, 12177, 9741, 5543, 6781, 7250, 10679, 4699, 1885, 3337,
# 3972, 7706, 5130, 8282, 5123, 7389, 2867, 2583, 2499, 3711, 11316, 4556,
# 5095, 289, 1926, 6689, 3650, 14892, 7858, 1127, 1521, 287, 11595, 509,
# 8057, 7583, 6363, 2852, 5945, 14798, 8035, 13660, 12391, 3235, 6395, 1011,
# 7700, 5725, 12667, 2023, 8142, 4097, 1364, 7619, 12886, 9134, 12601, 9393,
# 8948, 3651, 6881, 4176, 10747, 14978, 9121, 541, 8960, 9205, 12452, 1682,
# 6663, 2048, 6120, 11387, 10278, 12772, 7596, 412, 9712, 2703, 4974, 4223,
# 9838, 3899, 2860, 6817, 8893, 11401, 14764, 7080, 10948, 10941, 5672,
# 13628, 5227, 11423, 14734, 10639, 10795, 2105, 12483, 7787, 12739, 11341,
# 13032, 14894, 13579, 14541, 7903, 13182, 13070, 11239, 13333, 10484, 8911,
# 5546, 11044, 12348, 393, 5107, 11207, 8766, 9097, 8056, 5605, 13869, 9749,
# 3691, 1343, 7049, 4250, 9649, 10338, 4691, 9495, 4665, 8859, 2743, 3243,
# 13840, 7938, 10504, 3624, 14451, 9099, 142, 4994, 8707, 3397, 768, 10309,
# 4847, 13493, 12365, 13395, 9854, 12444, 13062, 12583, 7685, 11785, 11831,
# 337, 2908, 3211, 8305, 5642, 11018, 11371, 4820, 14053, 2567, 10692,
# 13090, 14538, 1794, 14781, 5608, 1951, 8622, 7065, 9168, 13001, 5708,
# 10470, 11367, 9527, 6755, 7557, 2303, 7110, 13414, 8639, 12411, 13989,
# 13299, 10864, 7422, 10416, 1863, 2612, 13880, 14973, 6490, 2231, 7895,
# 5888, 2221, 8087, 13499, 8007, 13765, 8713, 11877, 6191, 14125, 4644,
# 3444, 832, 11160, 6384, 10896, 5552, 11752, 164, 2415, 3846, 14146, 4744,
# 9584, 4126, 3706, 6204, 911, 1419, 636, 12362, 9221, 6546, 4778, 1448,
# 12658, 7289, 8288, 11369, 6064, 9235, 11052, 1904, 1087, 14899, 13717,
# 1798, 1416, 10471, 5028, 5483, 9990, 7017, 11332, 4971, 10526, 8273, 1875,
# 9508, 9830, 3081, 13742, 7621, 12485, 2861, 6260, 6644, 9217, 12821,
# 14450, 8741, 11763, 5837, 6227, 7994, 6002, 10563, 12623, 14571, 12963,
# 5038, 8384, 4194, 4735, 9818, 4595, 1018, 10097, 5847, 6822, 1256, 5187,
# 2054, 9067, 12839, 1454, 2368, 5857, 5144, 4623, 10176, 13688, 746, 11364,
# 7469, 4306, 13550, 11852, 7001, 11525, 162, 49, 11635, 13822, 2815, 154,
# 3446, 6208, 6530, 14891, 7262, 938, 9303, 6671, 4503, 4579, 5896, 9950,
# 14747, 13835, 2340, 14352, 8326, 4646, 8132, 11965, 9387, 392, 3869, 6022,
# 9069, 5090, 3960, 2940, 917, 1656, 6514, 9591, 3806, 7957, 7012, 8118,
# 499, 288, 1952, 8423, 9886, 5818, 3685, 7564, 5675, 11265, 9780, 6442,
# 13650, 3247, 10326, 14788, 452, 812, 10513, 14519, 4006, 10877, 10415,
# 12638, 13037, 6035, 2382, 1070, 14801, 5146, 10899, 8285, 4859, 9657,
# 2372, 2077, 2952, 12335, 13982, 5348, 12426, 52, 9541, 7489, 6501, 987,
# 8474, 6939, 1850, 14009, 6018, 14668, 13417, 5745, 7199, 4804, 11291,
# 8746, 12505, 13419, 6900, 2044, 9960, 7035, 194, 9056, 11669, 5330, 10882,
# 14247, 3778, 822, 14933, 10743, 3241, 8362, 1636, 9603, 12378, 14462,
# 5791, 13661, 195, 3129, 10725, 1230, 618, 4178, 1024, 2426, 9064]




# def sort_numbers(unsorted_list):
#     unsorted_list.sort()
#     return unsorted_list

# # Example usage
# unsorted = [7573, 6804, 6147, 10141, 4141, 13649, 7091, 10965, 14544,
# 1560, 10984, 4610, 9782, 10999, 10039, 8084, 7753, 11096, 1605, 2469,
# 6812, 4411, 1550, 1066, 2810, 1306, 14919, 6639, 9869, 11483, 752, 14409,
# 7673, 13713, 12944, 1344, 570, 2904, 11432, 7056, 1859, 12252, 12812,
# 9407, 10349, 9787, 7425, 12922, 10678, 4972, 3773, 11166, 14304, 7718,
# 7989, 611, 12911, 5057, 7568, 13573, 11232, 9405, 4756, 5811, 8251, 9066,
# 2189, 9322, 1820, 13035, 11659, 459, 3905, 7818, 8662, 7112, 5427, 10038,
# 506, 9129, 13408, 6563, 143, 2969, 14750, 903, 12325, 4373, 698, 9592,
# 9345, 3853, 11974, 8124, 2000, 11262, 10840, 480, 13560, 6200, 1316, 440,
# 1232, 12449, 9524, 2096, 252, 5428, 6220, 6274, 1321, 9704, 10360, 946,
# 13792, 3101, 10467, 1, 13767, 5246, 13084, 5943, 11612, 4675, 14555,
# 14646, 12272, 965, 14915, 1337, 9327, 13185, 4101, 2043, 11093, 7919, 879,
# 3662, 12912, 10005, 87, 1827, 5660, 9684, 3594, 4078, 5584, 5502, 895,
# 437, 3004, 5442, 10714, 9398, 14579, 960, 2522, 9425, 2075, 12263, 11539,
# 3942, 9362, 11626, 7650, 13616, 2151, 12757, 10430, 2377, 12352, 12187,
# 4870, 2457, 460, 4704, 2937, 6777, 3756, 6629, 11213, 5129, 8920, 1194,
# 13174, 3224, 6732, 11048, 2009, 14714, 8250, 4386, 12392, 2351, 1494,
# 7497, 2727, 1884, 4528, 3655, 10188, 9608, 6705, 9109, 13388, 4843, 1898,
# 3176, 6714, 3434, 8446, 5259, 10822, 7286, 12814, 13028, 5125, 4510, 8506,
# 407, 10352, 9752, 3143, 7605, 13988, 5027, 9437, 3833, 14498, 11976, 3387,
# 4054, 4757, 9358, 8003, 4201, 5175, 12226, 4555, 12455, 2304, 3192, 5229,
# 3228, 6510, 4017, 2441, 14473, 4599, 14501, 4861, 992, 2055, 6877, 11300,
# 14292, 13323, 10617, 2162, 7224, 12686, 11147, 4739, 8424, 10095, 6250,
# 10750, 4488, 14208, 4648, 333, 11837, 3724, 1962, 3737, 14682, 596, 9572,
# 10530, 3039, 13134, 6967, 8675, 11903, 11954, 12939, 4936, 11163, 6983,
# 7226, 1708, 11421, 11288, 353, 13947, 5447, 1387, 1383, 6896, 2161, 13057,
# 7962, 9552, 4065, 10655, 7633, 7063, 967, 4403, 1061, 13149, 11076, 10754,
# 3828, 8702, 11005, 8938, 9429, 5577, 4181, 13583, 5333, 2719, 6193, 9234,
# 4125, 10455, 14359, 7356, 4088, 8413, 4507, 14063, 3403, 13082, 11777,
# 6085, 3323, 3203, 13548, 42, 1519, 8536, 2234, 2453, 11492, 1149, 4617,
# 11678, 2367, 7719, 6936, 7039, 5238, 2669, 800, 2774, 2311, 11935, 11904,
# 13621, 10933, 9306, 2642, 10447, 2947, 4384, 1612, 11330, 12284, 7483,
# 14810, 1758, 8900, 14034, 10568, 3682, 805, 684, 1567, 1165, 2228, 10881,
# 1014, 9908, 10977, 12697, 11381, 4317, 13471, 9318, 13971, 4318, 2593,
# 8799, 11419, 13770, 2387, 12863, 2740, 13565, 7881, 57, 13361, 7960, 482,
# 8304, 6297, 12585, 1041, 10324, 3240, 14972, 308, 5968, 457, 1753, 6612,
# 8583, 13162, 9836, 1664, 10334, 6205, 10500, 10710, 12943, 8107, 12811,
# 4825, 13073, 12104, 2067, 7832, 4969, 2007, 4, 11103, 9826, 12857, 10652,
# 11829, 4608, 10702, 7129, 4842, 3098, 14643, 14127, 14986, 5834, 4146,
# 9984, 10758, 11007, 5939, 9617, 3123, 2269, 3280, 11534, 6128, 10947, 909,
# 14228, 11102, 11968, 8567, 10474, 4620, 14111, 1226, 7941, 5254, 11414,
# 2244, 10734, 8244, 5578, 10648, 12893, 11580, 6908, 432, 420, 5084, 297,
# 9474, 789, 8037, 3715, 6997, 132, 14391, 2546, 3943, 6445, 13444, 7109,
# 5764, 11439, 8013, 13908, 6144, 6101, 2320, 4220, 601, 9241, 14458, 7517,
# 14865, 14250, 2869, 7770, 14525, 8576, 3382, 10160, 14340, 14743, 6670,
# 14235, 6941, 3740, 12648, 10912, 6404, 9461, 332, 5953, 422, 13426, 12531,
# 2575, 857, 14923, 14624, 14104, 9123, 14023, 9802, 8105, 4005, 4496,
# 11649, 494, 2049, 2175, 8754, 8401, 8299, 10344, 2254, 12456, 2080, 973,
# 11641, 13352, 8228, 349, 10796, 9223, 14425, 14831, 2312, 920, 5697,
# 11241, 5542, 3866, 6252, 10981, 2331, 9874, 1482, 12879, 4114, 4981,
# 10231, 3721, 12003, 7434, 4160, 1121, 13945, 10458, 12077, 1834, 808,
# 1665, 4187, 5637, 410, 10483, 619, 5533, 1828, 8247, 12609, 12222, 9167,
# 13147, 10798, 11203, 10835, 14275, 721, 6042, 218, 4110, 2, 9012, 9415,
# 2786, 5247, 3814, 12323, 1582, 11806, 13215, 8456, 5977, 5878, 12533,
# 11672, 5450, 2782, 4567, 6544, 7567, 14783, 9410, 2794, 9411, 2917, 5321,
# 1411, 3898, 3286, 12628, 13916, 7240, 375, 10408, 3071, 2451, 14796,
# 10152, 174, 2157, 2931, 11703, 14586, 13630, 8393, 5076, 9065, 723, 14811,
# 11266, 5044, 8744, 13679, 9254, 8863, 14308, 9395, 1022, 6162, 10035, 690,
# 4255, 8377, 8781, 4949, 2008, 8447, 8758, 3507, 3483, 6656, 5274, 1620,
# 12393, 3000, 14093, 9497, 930, 3413, 3379, 4061, 842, 7464, 13951, 6646,
# 11706, 7932, 10175, 4377, 711, 11604, 8708, 2236, 10264, 11887, 9891,
# 4621, 4245, 8420, 530, 3912, 12550, 3819, 12541, 7034, 5415, 9965, 1242,
# 6047, 12488, 13229, 9670, 5312, 13255, 10159, 12466, 4902, 1439, 11430,
# 13704, 181, 11805, 6719, 5202, 6488, 6393, 13047, 1462, 10391, 1976, 2194,
# 3274, 4376, 4015, 14928, 5882, 1296, 5626, 4320, 7215, 1661, 8747, 12906,
# 14993, 5904, 11646, 5668, 9334, 4849, 12603, 6192, 5352, 7715, 14863,
# 5836, 14466, 7428, 7640, 4751, 10137, 2069, 5046, 9050, 6474, 688, 3233,
# 3923, 4914, 7249, 14373, 8961, 9198, 7235, 12450, 11416, 12148, 10519,
# 4819, 5803, 8849, 13398, 7054, 6071, 9283, 3540, 4489, 8966, 7119, 7217,
# 10064, 9294, 5221, 2042, 6459, 12000, 9711, 12098, 12086, 7909, 13558,
# 12198, 2489, 4546, 1925, 8256, 1179, 250, 12566, 8625, 12997, 247, 223,
# 11494, 7209, 1597, 12680, 2691, 1082, 1347, 6417, 12028, 11931, 993, 9667,
# 11080, 4574, 8560, 2470, 7348, 10125, 1868, 2763, 3581, 11759, 7834, 3666,
# 1215, 8501, 2173, 6569, 5283, 14375, 6893, 3321, 3561, 11975, 10558, 8355,
# 4234, 6686, 1198, 222, 14368, 7334, 2883, 1297, 7635, 7137, 13510, 3596,
# 5855, 3306, 4717, 12233, 13572, 1622, 12738, 7744, 2376, 13633, 2793,
# 13733, 5618, 1390, 5980, 14431, 12902, 858, 5964, 4992, 2684, 13198, 7440,
# 2205, 10177, 13439, 430, 11225, 12203, 9637, 3503, 5873, 14672, 10103,
# 1715, 8705, 8201, 8214, 2335, 1635, 2891, 2843, 10245, 626, 3815, 8163,
# 5619, 2870, 689, 8834, 10979, 9726, 5519, 9612, 91, 1091, 6142, 2223,
# 3616, 8302, 12240, 3684, 6235, 8697, 7970, 14708, 4458, 4067, 14167,
# 14745, 14345, 8917, 6650, 13252, 1736, 9150, 6760, 9413, 9423, 2101, 8165,
# 3183, 4692, 13702, 12801, 12540, 4752, 4996, 8210, 13873, 102, 1045, 9101,
# 3642, 14858, 1889, 14135, 7330, 6009, 2664, 6920, 11040, 2001, 4872,
# 10516, 6070, 11224, 3739, 14625, 9252, 7384, 103, 6460, 8649, 5517, 4694,
# 2681, 5454, 1735, 6045, 6135, 5903, 7000, 9892, 9834, 2291, 2302, 10987,
# 9577, 6929, 7736, 6124, 9258, 13911, 12269, 10518, 7487, 264, 12596,
# 13625, 14759, 9997, 10741, 5126, 2553, 1667, 10691, 3679, 14837, 6788,
# 1563, 3299, 14651, 1128, 8525, 7536, 8090, 11117, 1523, 1641, 7758, 1065,
# 4429, 1105, 13899, 6973, 6669, 900, 7906, 14088, 14213, 7734, 11392, 5355,
# 6596, 14819, 3792, 14405, 2672, 6618, 3703, 7033, 11216, 8952, 12850,
# 2968, 7900, 3560, 6616, 13734, 6863, 11643, 12813, 6706, 1996, 1455,
# 13543, 10185, 6789, 13736, 4051, 4864, 8777, 242, 6857, 12687, 10396,
# 6194, 3861, 6944, 9585, 6379, 2541, 2791, 11728, 12910, 5799, 13302, 2481,
# 6032, 7166, 10065, 9070, 9629, 4066, 11444, 4029, 14969, 10546, 6224,
# 5139, 14080, 6282, 13852, 13930, 12185, 3171, 11764, 3695, 1228, 585,
# 9828, 13791, 7668, 5381, 3181, 9934, 6350, 8652, 12942, 5824, 4553, 3338,
# 13724, 4632, 11651, 14765, 10004, 10011, 9290, 4193, 1394, 1399, 14506,
# 1781, 2622, 970, 5972, 14050, 10656, 13081, 5474, 1470, 2725, 14461, 9379,
# 14363, 5066, 7606, 11568, 14832, 8884, 13980, 14226, 550, 3878, 9034,
# 7958, 5162, 3289, 13992, 6762, 9304, 12653, 9636, 3500, 6357, 2660, 14844,
# 11600, 7144, 5338, 3593, 5848, 7648, 7761, 9006, 3371, 3597, 1954, 4233,
# 6610, 12230, 10982, 4922, 11615, 2429, 7747, 10694, 8512, 11709, 1191,
# 3599, 2225, 11150, 84, 351, 14497, 8527, 3020, 9365, 98, 10706, 9911,
# 4099, 10668, 2983, 10246, 14042, 6842, 14756, 2840, 8566, 1862, 10107,
# 4268, 8489, 2460, 4799, 2371, 6702, 11233, 5739, 964, 3209, 14306, 12546,
# 9250, 13670, 13711, 6409, 9046, 678, 6867, 10760, 1525, 9180, 12301,
# 14110, 1594, 228, 10003, 2916, 1963, 6685, 13487, 10014, 2245, 10449,
# 13146, 12227, 50, 10735, 4547, 14081, 14526, 10388, 2747, 14548, 5147,
# 12489, 12581, 9681, 6140, 14099, 1501, 10937, 1790, 2045, 7044, 10830,
# 7584, 4236, 7791, 5987, 3383, 9317, 10028, 9599, 1518, 10046, 1874, 9313,
# 9804, 13265, 13144, 3291, 8867, 10642, 10550, 14981, 827, 11691, 11391,
# 13093, 5114, 12396, 5476, 1922, 5724, 6077, 6343, 13231, 4863, 4695, 93,
# 8127, 12500, 11753, 1213, 4947, 1526, 415, 11489, 9426, 3896, 7830, 7083,
# 11182, 4633, 6176, 8432, 3564, 6133, 11780, 9016, 6006, 13517, 11622,
# 1109, 13898, 285, 2700, 4509, 10756, 7259, 4845, 5513, 2386, 3941, 1398,
# 2837, 5529, 12934, 9300, 6743, 4480, 6382, 6507, 8001, 7093, 13072, 6586,
# 6948, 12118, 1308, 1381, 14943, 14124, 4667, 11572, 4954, 4571, 12374,
# 11603, 12843, 1413, 13820, 12777, 1703, 6021, 1803, 9248, 2062, 7103,
# 8789, 3281, 13281, 9600, 7429, 4330, 12482, 9531, 6959, 1953, 1209, 14233,
# 1309, 12730, 9595, 1909, 12186, 5141, 8268, 1168, 6949, 12854, 14434,
# 8978, 1591, 3735, 11664, 13843, 5106, 738, 5109, 14206, 9278, 8634, 9943,
# 5798, 11955, 13701, 3421, 11123, 4359, 1072, 6496, 5692, 9589, 575, 8851,
# 3366, 1628, 11417, 8724, 4502, 14082, 12762, 2114, 8641, 13637, 13520,
# 12905, 2665, 189, 10234, 2336, 7526, 4763, 13768, 6831, 2402, 9823, 12367,
# 2933, 107, 3377, 6158, 5462, 6385, 13065, 29, 3640, 10787, 2078, 11323,
# 655, 13518, 3029, 12629, 10146, 14825, 2578, 3748, 11283, 12692, 12040,
# 10565, 12179, 9244, 13698, 14013, 65, 9222, 5051, 13413, 1610, 5190, 9163,
# 7013, 5767, 6778, 4772, 5853, 9783, 6241, 8908, 3628, 13585, 127, 14707,
# 10350, 7155, 6300, 270, 10033, 3883, 8329, 345, 5235, 5568, 5294, 1324,
# 8999, 6754, 10959, 11457, 10749, 6580, 6037, 3179, 13209, 3552, 9694,
# 11978, 12834, 423, 1763, 10531, 4530, 5702, 4801, 4780, 4683, 301, 5563,
# 10420, 1203, 852, 6984, 4090, 882, 7762, 3793, 3245, 14281, 1510, 7559,
# 4587, 12122, 6746, 11526, 12139, 14222, 9777, 5392, 13935, 14742, 4364,
# 2797, 13365, 14153, 4886, 3634, 12593, 637, 6418, 12919, 14134, 1081,
# 7947, 9551, 14869, 8942, 12480, 9570, 361, 13044, 6181, 2675, 14753, 9164,
# 11229, 1849, 7108, 13597, 9713, 6190, 14214, 1778, 11814, 4077, 12437,
# 11011, 14523, 1836, 10636, 7847, 2877, 3921, 14873, 8931, 12769, 9646,
# 14549, 2238, 741, 5122, 192, 933, 7546, 12543, 1067, 2822, 2149, 6555,
# 10993, 501, 7931, 178, 8590, 4658, 7355, 7846, 10078, 7814, 12999, 14829,
# 9534, 1950, 4286, 14674, 735, 3433, 3568, 5966, 744, 7835, 11046, 11670,
# 8176, 9517, 7344, 7008, 3120, 296, 6368, 13533, 6680, 786, 8748, 12883,
# 3823, 4660, 767, 7246, 4868, 14301, 9116, 2206, 14059, 14722, 2047, 8745,
# 8643, 13706, 467, 747, 4519, 873, 5695, 5118, 12032, 11524, 12702, 10888,
# 435, 12385, 4557, 366, 7092, 465, 12896, 8593, 7586, 5310, 298, 10903,
# 9332, 1553, 146, 5788, 3880, 11827, 4084, 12399, 3718, 1927, 3273, 5419,
# 2679, 8211, 3089, 6735, 1358, 12357, 9966, 409, 4841, 13131, 8236, 8295,
# 3750, 7303, 12337, 2216, 12509, 3463, 7077, 13243, 11741, 2754, 11598,
# 12927, 11237, 10203, 6570, 10693, 9281, 4355, 8275, 886, 5950, 4738, 7011,
# 9452, 10614, 11094, 2122, 13676, 4592, 7651, 13955, 11731, 2174, 4521,
# 5508, 6178, 12406, 628, 14393, 4915, 72, 9779, 12607, 1802, 8794, 14290,
# 9210, 11790, 6011, 13017, 1354, 7442, 8464, 1166, 1544, 1709, 8828, 7916,
# 497, 5737, 13620, 1250, 9145, 14878, 11862, 2760, 11234, 10871, 11769,
# 11486, 4344, 7558, 5880, 8526, 3948, 13189, 13225, 12460, 9889, 12015,
# 10777, 12634, 7842, 13622, 1733, 2550, 11020, 2318, 9346, 6383, 8109,
# 14901, 13513, 2838, 2663, 7418, 3725, 11306, 14089, 4963, 1844, 5214,
# 1193, 8690, 3420, 8065, 9970, 1653, 2462, 12320, 7264, 5382, 7041, 10869,
# 12679, 112, 9565, 11559, 2784, 12795, 9259, 13960, 13872, 6880, 11677,
# 12682, 7575, 1985, 2629, 11950, 9364, 5296, 6149, 10069, 6072, 9001,
# 12095, 8217, 4939, 9962, 5667, 612, 2605, 6487, 1461, 11278, 1013, 3102,
# 10027, 8141, 6590, 2058, 4442, 8385, 14327, 14574, 5449, 8674, 3913,
# 10407, 12937, 377, 3764, 14307, 12162, 4777, 12125, 1571, 9386, 11127,
# 8402, 2535, 2894, 11771, 10670, 9656, 10220, 13092, 9851, 6374, 10867,
# 8014, 12209, 10454, 13758, 6285, 3155, 14360, 2131, 8907, 7048, 8861,
# 10377, 7079, 5569, 2503, 9186, 8709, 8234, 2314, 13722, 9751, 1147, 7354,
# 9991, 9029, 8164, 8241, 7951, 8137, 2030, 4746, 2898, 3856, 14258, 360,
# 5480, 12360, 8430, 778, 13799, 11379, 12867, 4224, 8843, 14996, 4291,
# 8694, 3462, 13609, 1466, 7187, 1328, 12356, 3551, 2029, 2668, 3097, 7190,
# 6338, 10310, 13888, 11495, 14215, 6187, 6249, 13842, 11226, 6846, 13812,
# 2235, 1112, 2808, 6676, 8502, 9596, 3345, 6216, 3021, 10348, 9634, 1299,
# 8511, 2530, 9131, 8551, 10820, 2680, 277, 10916, 4888, 13821, 5800, 2010,
# 5722, 10611, 8954, 4783, 10950, 14130, 10058, 3251, 6575, 6552, 3543, 131,
# 7702, 12041, 11844, 7445, 13411, 6233, 4630, 2728, 9876, 8797, 6399, 2355,
# 14910, 4898, 27, 1942, 763, 5825, 9383, 10059, 8969, 6843, 3340, 3497,
# 1700, 7267, 9824, 10905, 1972, 1301, 10575, 11024, 8216, 10971, 11588,
# 9288, 7268, 11388, 6979, 8364, 14225, 7981, 14836, 275, 4226, 13489, 9506,
# 11951, 12787, 53, 11910, 13150, 1001, 8360, 13910, 1231, 5599, 4297, 8944,
# 7849, 1679, 8816, 12177, 9741, 5543, 6781, 7250, 10679, 4699, 1885, 3337,
# 3972, 7706, 5130, 8282, 5123, 7389, 2867, 2583, 2499, 3711, 11316, 4556,
# 5095, 289, 1926, 6689, 3650, 14892, 7858, 1127, 1521, 287, 11595, 509,
# 8057, 7583, 6363, 2852, 5945, 14798, 8035, 13660, 12391, 3235, 6395, 1011,
# 7700, 5725, 12667, 2023, 8142, 4097, 1364, 7619, 12886, 9134, 12601, 9393,
# 8948, 3651, 6881, 4176, 10747, 14978, 9121, 541, 8960, 9205, 12452, 1682,
# 6663, 2048, 6120, 11387, 10278, 12772, 7596, 412, 9712, 2703, 4974, 4223,
# 9838, 3899, 2860, 6817, 8893, 11401, 14764, 7080, 10948, 10941, 5672,
# 13628, 5227, 11423, 14734, 10639, 10795, 2105, 12483, 7787, 12739, 11341,
# 13032, 14894, 13579, 14541, 7903, 13182, 13070, 11239, 13333, 10484, 8911,
# 5546, 11044, 12348, 393, 5107, 11207, 8766, 9097, 8056, 5605, 13869, 9749,
# 3691, 1343, 7049, 4250, 9649, 10338, 4691, 9495, 4665, 8859, 2743, 3243,
# 13840, 7938, 10504, 3624, 14451, 9099, 142, 4994, 8707, 3397, 768, 10309,
# 4847, 13493, 12365, 13395, 9854, 12444, 13062, 12583, 7685, 11785, 11831,
# 337, 2908, 3211, 8305, 5642, 11018, 11371, 4820, 14053, 2567, 10692,
# 13090, 14538, 1794, 14781, 5608, 1951, 8622, 7065, 9168, 13001, 5708,
# 10470, 11367, 9527, 6755, 7557, 2303, 7110, 13414, 8639, 12411, 13989,
# 13299, 10864, 7422, 10416, 1863, 2612, 13880, 14973, 6490, 2231, 7895,
# 5888, 2221, 8087, 13499, 8007, 13765, 8713, 11877, 6191, 14125, 4644,
# 3444, 832, 11160, 6384, 10896, 5552, 11752, 164, 2415, 3846, 14146, 4744,
# 9584, 4126, 3706, 6204, 911, 1419, 636, 12362, 9221, 6546, 4778, 1448,
# 12658, 7289, 8288, 11369, 6064, 9235, 11052, 1904, 1087, 14899, 13717,
# 1798, 1416, 10471, 5028, 5483, 9990, 7017, 11332, 4971, 10526, 8273, 1875,
# 9508, 9830, 3081, 13742, 7621, 12485, 2861, 6260, 6644, 9217, 12821,
# 14450, 8741, 11763, 5837, 6227, 7994, 6002, 10563, 12623, 14571, 12963,
# 5038, 8384, 4194, 4735, 9818, 4595, 1018, 10097, 5847, 6822, 1256, 5187,
# 2054, 9067, 12839, 1454, 2368, 5857, 5144, 4623, 10176, 13688, 746, 11364,
# 7469, 4306, 13550, 11852, 7001, 11525, 162, 49, 11635, 13822, 2815, 154,
# 3446, 6208, 6530, 14891, 7262, 938, 9303, 6671, 4503, 4579, 5896, 9950,
# 14747, 13835, 2340, 14352, 8326, 4646, 8132, 11965, 9387, 392, 3869, 6022,
# 9069, 5090, 3960, 2940, 917, 1656, 6514, 9591, 3806, 7957, 7012, 8118,
# 499, 288, 1952, 8423, 9886, 5818, 3685, 7564, 5675, 11265, 9780, 6442,
# 13650, 3247, 10326, 14788, 452, 812, 10513, 14519, 4006, 10877, 10415,
# 12638, 13037, 6035, 2382, 1070, 14801, 5146, 10899, 8285, 4859, 9657,
# 2372, 2077, 2952, 12335, 13982, 5348, 12426, 52, 9541, 7489, 6501, 987,
# 8474, 6939, 1850, 14009, 6018, 14668, 13417, 5745, 7199, 4804, 11291,
# 8746, 12505, 13419, 6900, 2044, 9960, 7035, 194, 9056, 11669, 5330, 10882,
# 14247, 3778, 822, 14933, 10743, 3241, 8362, 1636, 9603, 12378, 14462,
# 5791, 13661, 195, 3129, 10725, 1230, 618, 4178, 1024, 2426, 9064]


# sorted_list = sort_numbers(unsorted)
# print("Sorted array: ", sorted_list)

def merge_sort(arr):
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    merge_sort(left_half)
    merge_sort(right_half)
   
    i = j = k = 0
   
    while i < len(left_half) and j < len(right_half):
        if left_half[i] < right_half[j]:
            arr[k]= left_half[i]
            i += 1
        else:
            arr[k] = right_half[j]
            j += 1
        k += 1
    
    while i < len(left_half):
        arr[k] = left_half[i]
        i += 1
        k += 1
       
    while j < len(right_half):
        arr[k] = right_half[j]
        j += 1
        k += 1
            
#Example usage: 
numbers = [981, 345, 123, 876, 234, 567, 789, 432, 901, 678, 543, 210, 654, 876, 109, 345, 876, 432, 567, 789, 123, 890, 678, 210, 987, 543, 876, 654, 321, 109, 876, 567, 234, 890, 432, 789, 210, 654, 987, 876, 543, 123, 321, 109, 678, 345, 567, 890, 654, 432, 789, 876, 210, 987, 234, 543, 321, 678, 109, 876, 654, 432, 567, 789, 123, 210, 890, 345, 876, 987, 234, 678, 321, 543, 109, 654, 432, 567, 789, 876, 210, 890, 123, 345, 987, 654, 109, 432, 543, 678, 876, 789, 234, 567, 210, 123, 876, 345, 987, 432, 678, 789, 654, 543, 109, 890]
merge_sort(numbers)
print("Sorted array: ", numbers)




        
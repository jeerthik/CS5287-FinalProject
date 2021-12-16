import numpy as np
import matplotlib.pyplot as plt

iterations = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
client_1_results = np.sort(np.array([0.08435556888580323,0.08086297035217285,0.10454936742782593,0.08138546943664551,0.08174059391021729,0.08156983375549316,0.08372113943099975,0.08116529464721679,0.08062012195587158,0.08260789394378662]))
client_5_results = np.sort(np.array([0.08356356859207154,0.08473135471343994,0.08587700128555298,0.09278188467025757,0.09194589853286743,0.08245014667510986,0.08316044092178344,0.08203778743743896,0.08146463394165039,0.08562802791595459]))
client_10_results = np.sort(np.array([0.08774211883544922,0.08480201721191406,0.08707178115844727,0.08485225915908813,0.08475277423858643,0.08509614706039428,0.08759010791778564,0.08365188598632813,0.0853391194343567,0.08498922109603882]))
client_20_results = np.sort(np.array([0.10433885097503662,0.13091939687728882,0.13558193683624267,0.13369532823562622,0.15238126516342163,0.13460572719573974,0.13728002786636354,0.13150697231292724,0.10247092485427857,0.08511529207229614]))

# client_1_results = np.sort(np.array([0.08191919485727946,0.08107703447341919,0.09367217143376669,0.08754304806391398,0.08041301727294922,0.08855239868164062,0.08103891770044963,0.08118125041325887,0.08024929602940878,0.08082588434219361]))
# client_5_results = np.sort(np.array([.08171642223993937,0.07989707628885905,0.07909732262293498,0.0795569920539856,0.08028261343638102,0.07959422985712687,0.0794249947865804,0.07995285828908284,0.08684597969055176,0.07987314065297445]))
# client_10_results = np.sort(np.array([0.09257877588272095,0.08246130466461182,0.08239046335220337,0.08205686489741007,0.08241153081258137,0.08335765759150188,0.09056569735209147,0.08463888088862101,0.08211934248606365,0.08191694657007853]))
# client_20_results = np.sort(np.array([0.11782043059666951,0.1395312261581421,0.13144502798716226,0.13334881862004597,0.1325148336092631,0.1295691990852356,0.13255439043045045,0.13383296807607015,0.13366057793299357,0.11767470757166544]))

print("===== ZMQ - CouchDB Round Trip Times =====")
print(client_1_results)
print(client_5_results)
print(client_10_results)
print(client_20_results)
print("===================================")

plt.title("ZMQ - CouchDB Round Trip Time ")
plt.xlabel("Avg Time for 100 requests")
plt.ylabel("Iteration")

# plt.plot(client_1_results, iterations, color = "blue", label = "1 client", marker = "o")
# plt.plot(client_5_results, iterations, color = "green", label = "5 clients", marker = "o")
# plt.plot(client_10_results, iterations, color = "pink", label = "10 clients", marker = "o")
# plt.plot(client_20_results, iterations, color = 'purple', label = "20 clients", marker = "o")
# plt.axhline(y = 9, color = "yellow", linestyle = "dashed", label = "90%")
# plt.axhline(y = 9.5, color = "orange", linestyle = "dashed", label = "95%")
# plt.axhline(y = 9.9, color = "red", linestyle = "dashed", label = "99%")

plt.plot(iterations, client_1_results, color = "blue", label = "1 client", marker = "o")
plt.plot(iterations, client_5_results, color = "green", label = "5 clients", marker = "o")
plt.plot(iterations, client_10_results, color = "pink", label = "10 clients", marker = "o")
plt.plot(iterations, client_20_results, color = 'purple', label = "20 clients", marker = "o")

plt.legend(loc = "best")
plt.show()
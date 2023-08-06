import numpy as np
import time


class BayesianAvg:
    def __init__(self, freq_s_seq, freq_e_seq):
        self.begin_freq_arr = np.array(freq_s_seq)
        self.end_freq_arr = np.array(freq_e_seq)
        self.total_freq = np.add(self.begin_freq_arr, self.end_freq_arr)
        self.end_freq_weight = self.end_freq_arr / self.total_freq
        self.global_freq = self.globalAvgFreq()
        self.global_avg_e_weight = self.globalAvgEndWeight()

    def globalAvgFreq(self):
        return np.average(self.total_freq)

    def globalAvgEndWeight(self):
        return np.average(self.end_freq_weight)

    def globalFactor(self):
        return self.global_freq * self.global_avg_e_weight

    def bayesianAvgScore(self):
        NUMR = (self.end_freq_weight * self.total_freq) + self.globalFactor()
        DENR = self.total_freq + self.global_freq
        return NUMR / DENR

    def __repr__(self):
        return """T0 Freq: {}, T1 Freq:{}""".format(self.begin_freq_arr,
                                                    self.end_freq_arr)


if __name__ == '__main__':
    freq_s_seq = np.random.randint(1, 100, size=1000000)
    freq_e_seq = np.random.randint(1, 100, size=1000000)
    start = time.time()
    result = BayesianAvg(freq_s_seq, freq_e_seq)
    r = result.bayesianAvgScore()
    print(time.time() - start)



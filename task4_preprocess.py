import json
import nolds
from numpy import extract
import numpy as np
import matplotlib.pyplot as plt
from preprocessing import remove_outliers,remove_ectopic_beats,is_outlier,_remove_outlier_karlsson,_remove_outlier_acar,interpolate_nan_values,get_nn_intervals,is_valid_sample
from extract_features import get_time_domain_features, get_geometrical_features, get_frequency_domain_features, _get_freq_psd_from_nn_intervals, _create_time_info, _create_interpolation_time, _get_features_from_psd, get_csi_cvi_features, get_poincare_plot_features, DFA, get_sampen
from plot import plot_timeseries, plot_distrib, plot_psd, plot_poincare

json_file = open('Vishakh.json')
main_file = json.load(json_file)

hr_in_bpm=main_file['captured_data']['hr']['HR in BPM']
rr_in_ms = main_file['captured_data']['hr']['RR in ms']
next_rr_int = rr_in_ms
print(type(next_rr_int))
rr_outliers = remove_outliers(rr_in_ms)
print(type(rr_outliers))

rr_ectopic = remove_ectopic_beats(rr_in_ms)
print(rr_ectopic)
newList = list()
for element in rr_ectopic:
    if str(element) != "nan":
        newList.append(element) 
print(newList)

for i in range(len(rr_in_ms)):
  rr_out=is_outlier(i,i)
print(rr_out)
print(type(rr_out))

karl = _remove_outlier_karlsson(rr_in_ms)
print(karl)
print(type(karl))
karl_list = list(karl)
print(type(karl_list))

rr_outlier_acar = _remove_outlier_acar(rr_in_ms)
print(rr_outlier_acar)

rr_inter = interpolate_nan_values(rr_in_ms)
print(rr_inter)

nn_inter = get_nn_intervals(rr_in_ms)
print(nn_inter)

for tup in range(len(karl_list)):
  karl_tup = is_valid_sample(rr_in_ms,tup)
  print(karl_tup)

time_nn = get_time_domain_features(rr_ectopic)
print(time_nn)

time_ect = get_geometrical_features(rr_ectopic)
print(time_ect)

time_freq = get_frequency_domain_features(rr_ectopic)
print(time_freq)

time_freq_psd = _get_freq_psd_from_nn_intervals(rr_ectopic)
print(time_freq_psd)
print(type(time_freq_psd))
time_freq_psd_list = list(time_freq_psd)
print(type(time_freq_psd_list))
print(time_freq_psd_list)

time_info = _create_time_info(rr_ectopic)
print(time_info)

inter_time = _create_interpolation_time(rr_ectopic)
print(inter_time)

feat = _get_features_from_psd(rr_ectopic,time_freq_psd_list)
print(feat)

csi = get_csi_cvi_features(rr_ectopic)
print(csi)

poincare = get_poincare_plot_features(rr_ectopic)
print(poincare)

dfa = DFA(rr_ectopic)
print(dfa)

samp = get_sampen(rr_ectopic)
print(samp)

timeseries = plot_timeseries(rr_ectopic)
plt.show()

distrib = plot_distrib(rr_ectopic)
plt.show()

psd = plot_psd(rr_ectopic)
plt.show()

poincare = plot_poincare(rr_ectopic)
plt.show()

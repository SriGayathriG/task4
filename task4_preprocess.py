import json
from preprocessing import remove_outliers,remove_ectopic_beats,is_outlier,_remove_outlier_karlsson,_remove_outlier_acar,interpolate_nan_values,get_nn_intervals,is_valid_sample

json_file = open('Vishakh.json')
main_file = json.load(json_file)

hr_in_bpm=main_file['captured_data']['hr']['HR in BPM']
rr_in_ms = main_file['captured_data']['hr']['RR in ms']
next_rr_int = rr_in_ms

rr_outliers = remove_outliers(rr_in_ms)
print(type(rr_outliers))
print()

rr_ectopic = remove_ectopic_beats(rr_in_ms)
print(rr_ectopic)

for i in range(len(rr_in_ms)):
  rr_out=is_outlier(i,i)
print(rr_out)

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
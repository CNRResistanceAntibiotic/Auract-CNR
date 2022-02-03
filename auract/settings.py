import os

#base path
script_path = os.path.dirname(os.path.abspath(__file__))
cwd_path = os.getcwd()

microToken = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..E9jj8wSb_cjr7Kim.MPxH1MvIS-u66Dx-NXlYcwoHVOWhAHAY6UmTC8V9Gq2oevRMvnWgGvrAIfK4Jb6yOVLa21JrFWmf6OVdM3xUIY7Hh8lfUGxRbptPsNXnEltXfwdkuwrkO8X4r_FVBUpfmbG9Ts-deqq4JU7grM5XlQ.O9ndD2BYPOnqOtg6Pqk4mA"

#module data path
data_dir = os.path.join(script_path, 'data')

#second file path cwd
#second_file_dir = os.path.join(cwd_path, 'second_file')
second_file_dir = cwd_path
micro_json_dir = os.path.join(second_file_dir, 'microreact')
geo_csv_ll_dir = os.path.join(second_file_dir, 'Geocoding/csv_generate')
auspice_config_dir = os.path.join(second_file_dir, 'auspice/config')
auspice_data_dir = os.path.join(second_file_dir, 'auspice/data')
auspice_refine_dir = os.path.join(second_file_dir, 'auspice/result')

#result file path cwd
resultDir = os.path.join(cwd_path, 'auract_result')
result_Dir_micro = os.path.join(resultDir, 'microreact')
result_Dir_auspice = os.path.join(resultDir, 'auspice')

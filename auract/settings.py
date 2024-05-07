import os

#base path
script_path = os.path.dirname(os.path.abspath(__file__))
cwd_path = os.getcwd()

microToken = "eyJhbGciOiJkaXIiLCJlbmMiOiJBMjU2R0NNIn0..uqBq2HzVd2cg4Dnw.jofulfCiSaJSei7CChHqBeVRkSkCsJzDSjcjiFL_MA7Pc7w_AhCVRuK1KbJ-TGO6NAaTc9CYHj6-e8otMW0QR6VkYkgvb1dCofojiv5q3_PFvJgPDF4GPhzEbqteVbJUvk5SYSvoU8xVnQiCKixU_g.r3yOSNxyPWkt-HIqPXmjSA"

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
result_dir = os.path.join(cwd_path, 'auract_result')
result_dir_micro = os.path.join(result_dir, 'microreact')
result_dir_auspice = os.path.join(result_dir, 'auspice')

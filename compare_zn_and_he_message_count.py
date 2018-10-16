import parse
import pandas as pd 
zn_df = parse.get_df_from_file('~/ZNdata')
he_df = parse.get_df_from_file('~/HEdata')
message_count_df = pd.DataFrame({'ZN': parse.get_message_type_count(zn_df), 'HE': parse.get_message_type_count(he_df)})
message_count_df['ZNoverHEratio'] = message_count_df['ZN']/message_count_df['HE']
message_count_df.index.names = ['message_type']
print message_count_df


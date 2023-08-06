import os
import toml
import pandas as pd

# Load config information, pointing to data sets.  
# Append private config, if available.
path_config = os.path.join(os.path.dirname(__file__), 'configs', 'config.toml')
path_private_config = os.path.join(os.path.dirname(__file__), 'configs', 'private-config.toml')
config = toml.load(path_config)
if os.path.isfile(path_private_config):
    config.update(toml.load(path_private_config))
del path_config
del path_private_config

def get_shortname_dict(config):
    """
    {key:shortname, value: 
        {paths: {dict of paths},
         description: description string}
    }

    """
    shortname_dict = {} 
    # print("Data Sets Found:")
    for dataset in config:
        # print('\t', dataset)
        path_dataset = config[dataset]['path_parentdir'] 
        if not os.path.isabs(path_dataset):
            path_dataset = os.path.join(os.path.dirname(__file__), path_dataset)
        path_shortnames = os.path.join(path_dataset, 'shortnames.txt')


        shortnames = toml.load(path_shortnames)

        while len(shortnames) > 0:
            sname, paths_dict = shortnames.popitem()

            # Append base path to relative paths inside dataset `shortnames` file.
            for key in ['data', 'meta']:
                # Handle nested lists of paths
                if type(paths_dict[key]) == list:
                    for i in range(len(paths_dict[key])):
                        paths_dict[key][i] = os.path.join(path_dataset, paths_dict[key][i])
                else:
                    paths_dict[key] = os.path.join(path_dataset, paths_dict[key])
            shortname_dict[sname] = {}
            shortname_dict[sname]['paths'] = paths_dict
            if 'description' in paths_dict:
                shortname_dict[sname]['description'] = paths_dict['description']

    return shortname_dict

def print_shortnames(description=False):
    """
    Print all shortnames found.  Associated descriptions will be printed
    if `description` set to True.  
    """
    shortname_dict = get_shortname_dict(config)
    for sname in sorted(shortname_dict):
        print('\t',sname)
        if description:
            if 'description' in shortname_dict[sname]:
                print(shortname_dict[sname]['description'])
            else:
                print("(No description available)")


def get_data(shortname=None):
    """
    If no shortname is specified, a sample data set will be returned.
    """
    # TODO: this shouldn't be reloaded everytime.  Or maybe it should?
    shortname_dict = get_shortname_dict(config)
    if shortname == None:
        shortname = list(shortname_dict.keys())[0]
        print('get_data(): No shortname specified so choice will be arbitrary.  Returning: %s' % shortname)

    assert shortname in shortname_dict, 'Requested `shortname` not found.'

    path_meta = shortname_dict[shortname]['paths']['meta']
    meta = toml.load(path_meta)

    path_data_list = shortname_dict[shortname]['paths']['data']
    if type(path_data_list) == str:
        path_data_list = [path_data_list]

    df_list = []
    for path_data in path_data_list:
        # Check if associated zip-file is available.  If so, use that.
        if os.path.isfile(path_data+'.zip'):
            path_data = path_data+'.zip'

        df = pd.read_csv(path_data, skipinitialspace=True)

        # Rename Columns
        if 'columns-rename' in meta:
            df.rename(columns=meta['columns-rename'], inplace=True)

        # Apply Rotations, if present.
        # NOTE: The rotations are applied AFTER any column renaming.
        #       Hence, the key entries should refer to the renamed column names.
        if 'Rsensor2body' in meta:
            Rdict = meta['Rsensor2body']
            for key in Rdict:
                cols = [col for col in df if col.startswith(key)]
                # Sort the columns so that we end up with the order: X->Y->Z
                # where these are in the `sensor` frame.
                cols.sort()
                assert len(cols) == 3, "Invalid number of matching columns found for Rsensor2body.%s" % key

                # Apply transformation:
                #   [x1, x2, ... xm]                   [x1, x2, ... xm]
                #   [y1, y2, ... ym]  =   Rsensor2body [y1, y2, ... ym]
                #   [z1, y3, ... ym]                   [z1, y3, ... ym]
                #                   body                               sensor
                # We transpose the entire expression in order to be able
                # to work with and store the Pandas DataFrame directly.
                Rsensor2body = pd.np.array(Rdict[key],dtype=pd.np.float)
                df[cols] = df[cols] @ Rsensor2body.transpose()

        # Check for time column and attempt to populate if it doesn't exist.
        time_col = 'TimeFromStart (s)'
        if time_col not in df:
            if 'SampleFreq (Hz)' in meta:
                dt_sec = 1.0/meta['SampleFreq (Hz)']

                df[time_col] = df.index * dt_sec
            else:
                print("Unable to index time information.")
        df.set_index(time_col, inplace=True)
        df_list.append(df)
    df = pd.concat(df_list, axis=1)


    return df



if __name__ == '__main__':
    print("Data Shortnames Found:")
    print_shortnames(description=True)




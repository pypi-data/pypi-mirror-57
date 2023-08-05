# ics_ipa_interface

This repo gives users the tools to be able to run scripts as a ipa job and desktop script at the same time.

## Install Process

To install simply run the following command

```sh
pip install ics-ipa-interface
```

## Example

```python
from intrepidcs import ipa_interface as ipa


if __name__ == "__main__":
    # setup the help dialog for the script
    ipa.ipa_init(script_name="my_script_name.py", version="1.0",
                 message="this dose cool things")

    # input data path
    data_file_paths = ipa.get_data_files()

    # config are user defined and are uses as arguments to
    # the script
    config_file_paths = ipa.get_config_files()

    # path to store data
    output_path = ipa.get_output_dir()

    for i, path in enumerate(data_file_paths):
        # do something here

        # get vehicle info for file if provided
        vehicleId = ipa.get_attribute_from_file(path, 'vehicleId')

        # update progress
        ipa.update_progress('filesRead', percent=i/len(data_file_paths))
```

### --help for example

```
        this dose cool things
Usage:
  my_script_name.py
  my_script_name.py <IPA_FILE>
  my_script_name.py [--data_files=<FILE>]... [--config_files=<FILE>]... [--previous_dir=<DIR>] --output_dir=<DIR>
  my_script_name.py (-h | --help)
  my_script_name.py --version

Options:
  -h --help     Show this screen.
  --version     Show version.
  -d FILE --data_files=<FILE>   The data files that are used.
  -c FILE --config_files=<FILE> The config files that are used.
  -o DIR --output_dir=<DIR>   The output directory. This is required if the script output directory.
  -p DIR --previous_dir=<DIR>   The previous run output directory. This is used if you want to use the results of the previous run as an input.
```

## IPA File
The keys shown in the following example are required. as a user you can add more key value pairs at the ... locations shown

```json
{
    "data_files" : [
        {
            "path": "unique_path/to/DataFile1"
            ...
        },
        {
            "path": "unique_path/to/DataFile2"
            ...
        },
    ],
    "config_files" : [
        {
            "path": "unique_path/to/ConfigFile1"
            ...
        },
        {
            "path": "unique_path/to/ConfigFile2"
            ...
        },
    ],
    "previous_dir": "optional_path/to/previous_output_dir",
    "output_dir": "path/to/output_dir"
}
```


## Command Line Args

```sh
    my_script_name.py -d unique_path/to/DataFile1 -d unique_path/to/DataFile2 -c unique_path/to/ConfigFile1 -o output/dir -p previous/dir
```
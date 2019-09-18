# OpenNNG (Work in progress...)

OpenNNG (Open Neural Network Generator) is a general purpose data generator toolkit that uses TensorFlow 2.0. Supported architectures:

- [variational autoencoder](https://arxiv.org/abs/1312.6114)
- [generative adversarial network](https://arxiv.org/abs/1406.2661)

## Key features

OpenNNG focuses on modularity to support advanced modeling and training capabilities:

 - usage of predefined models
 - creation of custom architectures
 - domain adaptation
 
## Installation

### Clone repository

If you want to use OpenNNG as a command line interface:

```
git clone https://github.com/avramandrei/OpenNNG.git
cd OpenNNG/
pip install -r requirements.txt
```

### pip

If you want to use OpenNNG as an API:

```
pip install opennng
```

## Usage

OpenNNG requires:
 - Python >= 3.6
 - TensorFlow >= 2.0.0rc0
 - Pillow >=6.1
 
### Data downloading

OpenNNG offers a veriety of databases that can be downloaded with the `download.py` script. [Here](docs/databases.md) is a list of the available databases.

```
python3 download.py [database]
```
 
### Data processing

Processed data must be saved in Numpy `.npy` files. Data can be automatically processed using the `process.py` script. 

```
python3 process.py [raw_data_path] [processed_data_path] [--from_noise] [--normalize]
```

|  Named Argument | Type | Description |
| -------------------- | --- | -- |
| raw_data_path | str | Path to the raw data. Two(train, valid)/four(train_X, valid_X, train_y, valid_y) folders are expected here. |
| processed_data_path | str | Path where processed data will be saved |
| --from_noise | bool | Whether the generator will produce data from noise or from given data. If set to `True`, two directories are expected in `raw_data_path`, else four directories are expected. Default: `True`. |
| --normalize | bool | Whether to normalize the data. Default: `True`. |

### Train

To train, run the `train.py` script. This script automatically generates 10 samples that shows how the training process evolves at evrey checkpoint.

```
python3 train.py [--model] 
                 [--train_X_path] [--valid_X_path] [--train_y_path] [--valid_y_path] [--from_noise] 
                 [--optimizer] [--learning_rate] [--iterations] [--batch_size] 
                 [--save_checkpoint_steps] [--save_checkpoint_path]
                 [--valid_batch_size] [--valid_steps] 
                 [--generate_train_samples] [--num_train_samples]
```

|  Named Argument | Type | Description |
| --- | --- | -- |
| --model | str | Type of the model. [Here](docs/models.md) is a list of all the available models. |
| --train_X_path | str | Path to the X train data, saved as a `.npy` file. |
| --valid_X_path | str | Path to the X validation data, saved as a `.npy` file. |
| --train_y_path | str | Path to the y train data, saved as a `.npy` file. |
| --valid_y_path | str | Path to the y validation data, saved as a `.npy` file. |
| --optimizer | str | Name of the optimizer, as described in https://keras.io/optimizers/. Default value: `"Adam"` |
| --learning_rate | float | Learning rate of the optimizer. Default: `0.001`. |
| --iterations | int | Number of training steps. Default: `100000`. |
| --batch_size | int | Batch size for training. Defaul: `32`. |
| --save_checkpoint_steps | int | Save a checkpoint every X steps. Default: `1000` |
| --save_checkpoint_path | str | Save the model at this path every `--save_checkpoint_steps`. Default: `trained_model/model` |
| --valid_batch_size | int | Batch size for validation. Defaul: `32`. |
| --valid_steps | int | Perfom validation every X steps. Default: `250`. |
| --generate_train_samples | bool | Whether to generate samples during training. Default: `True`. |
| --num_train_samples | int | Number of generated training samples. Default: `10`. |

### Examples of automatically generated GIF's during training

| Model | Samples |
| --- | --- |
| ConvVAESmall | ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_vae/train_sameple_1.gif?raw=true) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_vae/train_sameple_2.gif?raw=true) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_vae/train_sameple_3.gif?raw=true) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_vae/train_sameple_4.gif?raw=true) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_vae/train_sameple_5.gif?raw=true) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_vae/train_sameple_6.gif?raw=true) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_vae/train_sameple_7.gif?raw=true) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_vae/train_sameple_8.gif?raw=true) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_vae/train_sameple_9.gif?raw=true) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_vae/train_sameple_10.gif?raw=true) |
| ConvGANSmall | ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_gan/train_sameple_1.gif) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_gan/train_sameple_2.gif) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_gan/train_sameple_3.gif) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_gan/train_sameple_4.gif) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_gan/train_sameple_5.gif) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_gan/train_sameple_6.gif) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_gan/train_sameple_7.gif) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_gan/train_sameple_8.gif) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_gan/train_sameple_9.gif) ![alt text](https://github.com/avramandrei/OpenNNG/blob/master/examples/train_samples/conv_gan/train_sameple_10.gif) |


### Generate

To generate a new sample, run `generate.py`.

```
python3 generate.py [model] [model_path] [--num_sample] [--sample_save_path]
```

|  Named Argument | Type | Description |
| --- | --- | -- |
| model | str | Type of the model. [Here](docs/models.md) is a list of all the available models. |
| model_path | str | Load the model from this path. |
| --num_sample | int | Number of samples to generate.Default: `10`. |
| --sample_save_path | str | Save the samples at this path. Default: `samples`. |




from src.util.generator import generate_png_samples, generate_gif_samples
import yaml
import argparse
import src.util.yaml_parser as yaml_parser
import os


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("config_path", type=str)
    args = parser.parse_args()

    with open(args.config_path, "r") as stream:
        try:
            config = yaml.safe_load(stream)

            model, _, _= yaml_parser.parse_model(config)
            print("Model selected: {}\n".format(config["model"]["type"]))
            model.summary()

            num_sample, sample_save_path = yaml_parser.parse_generate(config)
            if not os.path.exists(sample_save_path):
                os.makedirs(sample_save_path)

        except yaml.YAMLError as exc:
            print(exc)
            exit(0)

    generate_png_samples(model, num_sample, sample_save_path)
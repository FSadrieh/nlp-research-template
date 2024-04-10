import wandb
import argparse

import train
from cfgs.sweep_cfgs import sweep_cfgs


def arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "-n",
        "--name",
        type=str,
        help="Name of the sweep configuration. The id will be ignored. Will start a new sweep.",
    )
    parser.add_argument(
        "-id",
        "--sweep_id",
        type=str,
        help="If you want to resume a sweep specify the id. The name will be ignored.",
    )
    parser.add_argument(
        "--config",
        type=str,
        help="Path to the config file, where the default values (not modified by the sweep) are set.",
    )
    parser.add_argument("--count", type=int, default=10)
    return parser.parse_args()


def main():
    """
    Performs a wandb sweep from the sweep_cfgs.py file.
    """
    args = arg_parser()
    if args.name:
        sweep_id = wandb.sweep(
            sweep_cfgs[args.name],
            project=train.WANDB_PROJECT,
            entity=train.WANDB_ENTITY,
        )
    else:
        sweep_id = args.sweep_id
    wandb.agent(
        sweep_id,
        function=lambda: train.main(is_sweep=True, config_path=args.config),
        count=args.count,
    )


if __name__ == "__main__":
    main()

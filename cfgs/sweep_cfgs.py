sweep_cfgs = {
    "Example_sweep": {
        "method": "grid",
        "metric": {"name": "val/loss", "goal": "minimize"},
        "parameters": {
            "batch_size": {"values": [32, 64, 128]},
            "lr": {"values": [0.001, 0.01, 0.1]},
            "dropout": {"values": [0.3, 0.5, 0.7]},
        },
    }
}

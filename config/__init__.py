import yaml


def load_config_to_app(app):
    with open('application.yaml', 'r') as config_file:
        cfg = yaml.safe_load(config_file)
        app.config.update(cfg)

package config

import "github.com/ilyakaznacheev/cleanenv"

type ServerConfig struct {
	Port string `yaml:"port" env:"SERVER_PORT"`
}

type Config struct {
	Server ServerConfig `yaml:"server"`
}

func New(path string) (Config, error) {
	config := Config{}
	err := cleanenv.ReadConfig(path, &config)
	return config, err
}
